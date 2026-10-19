"""HTTP layer for the private P0 bookmark library.

``Application`` is a :class:`http.server.ThreadingHTTPServer` subclass that
carries the two collaborators every request needs -- the SQLite
:class:`app.storage.Storage` and the ``app.views`` module -- so the request
handler can reach them as ``self.server.storage`` and ``self.server.views``
without importing either layer itself.

``RequestHandler`` is a :class:`http.server.BaseHTTPRequestHandler` that
implements the frozen P0 route and error contract:

* ``GET /`` (with ``?collection=`` and ``?q=``) renders the library and the
  collection sidebar. ``inbox``/``default`` is accepted as an alias for the
  default inbox; an unknown collection id yields ``404``.
* ``POST /bookmarks`` validates the URL, stores the record and redirects with
  ``303`` to ``/?collection=<id|inbox>``; a rejected submission returns ``400``
  and re-renders the input for correction.
* ``POST /collections`` creates a collection and redirects with ``303`` to
  ``/``; an empty or duplicate name returns ``400``.
* ``POST /bookmarks/<id>/move`` moves a record and redirects with ``303`` to the
  target collection; an unknown record or collection returns ``404``.
* ``GET /go/<id>`` answers ``302`` with ``Location`` set to the stored URL. The
  target page is never fetched or proxied.
* every other public path (``/share``, ``/public`` and any other undefined
  route) returns ``404`` without exposing stored data.

``GET`` requests never mutate state and every ``POST`` ends in a ``303``
redirect (POST/Redirect/GET) so a refresh cannot resubmit. ``run(config)``
creates the data directory, builds :class:`app.storage.Storage`, wires the
storage and views into :func:`make_server` and serves on
``(config.host, config.port)``.

This module keeps no mutable module-level state and imports no third-party
package: only the Python standard library plus the sibling ``app`` modules.
"""

import http.server
import urllib.parse
from http import HTTPStatus

from app import config as app_config
from app import storage as app_storage
from app import validation
from app import views

__all__ = ["Application", "RequestHandler", "make_server", "run"]

#: Query/alias tokens that name the built-in default inbox.
_INBOX_ALIASES = ("inbox", "default")


def _path_segments(path):
    """Split a request path into its non-empty segments."""
    return [segment for segment in str(path).split("/") if segment]


def _first_value(mapping, key):
    """Return the first value for ``key`` in a parsed query/form mapping."""
    values = mapping.get(key)
    if not values:
        return ""
    return values[0]


def _collection_location(collection_id):
    """Return the POST/Redirect/GET target that browses one collection."""
    return "/?collection=" + urllib.parse.quote(str(collection_id), safe="")


class RequestHandler(http.server.BaseHTTPRequestHandler):
    """Serve the frozen P0 routes over the shared storage and views."""

    # -- collaborators ----------------------------------------------------

    @property
    def storage(self):
        """The :class:`app.storage.Storage` shared by all request threads."""
        return getattr(self.server, "storage", None)

    @property
    def view_module(self):
        """The ``app.views`` module used to render every page."""
        return getattr(self.server, "views", views)

    # -- response helpers -------------------------------------------------

    def _send_html(self, status, body):
        """Send an HTML document with an accurate ``Content-Length``."""
        payload = str(body).encode("utf-8")
        self.send_response(int(status))
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(payload)

    def _redirect(self, status, location):
        """Send a redirect (303 after a POST, 302 when opening the original)."""
        self.send_response(int(status))
        self.send_header("Location", location)
        self.send_header("Content-Length", "0")
        self.end_headers()

    def _send_400(self, message, form_state=None):
        """Render the frozen ``400`` page that echoes the rejected input."""
        body = self.view_module.render_error(
            int(HTTPStatus.BAD_REQUEST), message, form_state
        )
        return self._send_html(HTTPStatus.BAD_REQUEST, body)

    def _send_404(self, message="page not found"):
        """Render the uniform ``404`` page without leaking stored data."""
        body = self.view_module.render_error(
            int(HTTPStatus.NOT_FOUND), message, None
        )
        return self._send_html(HTTPStatus.NOT_FOUND, body)

    def _read_form(self):
        """Read and decode an ``application/x-www-form-urlencoded`` body."""
        header = self.headers.get("Content-Length")
        try:
            length = int(header)
        except (TypeError, ValueError):
            length = 0
        if length <= 0:
            return {}
        raw = self.rfile.read(length)
        text = raw.decode("utf-8", "replace")
        parsed = urllib.parse.parse_qs(text, keep_blank_values=True)
        return {
            key: values[0]
            for key, values in parsed.items()
            if values
        }

    # -- routing ----------------------------------------------------------

    def do_GET(self):
        """Handle every read-only route; unknown paths return ``404``."""
        parsed = urllib.parse.urlsplit(self.path)
        path = parsed.path or "/"
        if path == "/":
            return self._handle_index(parsed)
        segments = _path_segments(path)
        if len(segments) == 2 and segments[0] == "go":
            return self._handle_go(segments[1])
        return self._send_404()

    do_HEAD = do_GET

    def do_POST(self):
        """Handle every mutation; undefined paths return ``404``."""
        parsed = urllib.parse.urlsplit(self.path)
        path = parsed.path or "/"
        if path == "/bookmarks":
            return self._handle_create_bookmark()
        if path == "/collections":
            return self._handle_create_collection()
        segments = _path_segments(path)
        if (
            len(segments) == 3
            and segments[0] == "bookmarks"
            and segments[2] == "move"
        ):
            return self._handle_move(segments[1])
        return self._send_404()

    # -- GET routes -------------------------------------------------------

    def _handle_index(self, parsed):
        """Render ``GET /`` scoped by ``?collection=`` and ``?q=``."""
        query = urllib.parse.parse_qs(parsed.query, keep_blank_values=True)
        token = _first_value(query, "collection")
        resolved_id = None
        if token:
            if token.strip().lower() in _INBOX_ALIASES:
                default = self.storage.get_default_collection()
                if default is None:
                    return self._send_404("default collection not found")
                resolved_id = default["id"]
            else:
                collection = self.storage.get_collection(token)
                if collection is None:
                    return self._send_404("collection not found")
                resolved_id = collection["id"]
        keyword = _first_value(query, "q")
        collections = self.storage.list_collections()
        bookmarks = self.storage.list_bookmarks(resolved_id, keyword)
        body = self.view_module.render_index(
            collections, bookmarks, token, keyword
        )
        return self._send_html(HTTPStatus.OK, body)

    def _handle_go(self, raw_id):
        """Answer ``302`` with the stored URL; unknown ids return ``404``."""
        bookmark = self.storage.get_bookmark(urllib.parse.unquote(raw_id))
        if bookmark is None:
            return self._send_404("bookmark not found")
        return self._redirect(HTTPStatus.FOUND, bookmark["url"])

    # -- POST routes ------------------------------------------------------

    def _handle_create_bookmark(self):
        """Validate and store a record, then redirect with ``303``."""
        fields = self._read_form()
        url = fields.get("url", "")
        title = fields.get("title", "")
        collection_id = fields.get("collection_id", "")
        form_state = {
            "url": url,
            "title": title,
            "collection_id": collection_id,
        }
        try:
            clean_url = validation.normalize_url(url)
        except ValueError as error:
            return self._send_400(str(error), form_state)
        clean_title = validation.clean_title(title, clean_url)
        try:
            bookmark = self.storage.create_bookmark(
                clean_url, clean_title, "", collection_id
            )
        except ValueError as error:
            return self._send_400(str(error), form_state)
        return self._redirect(
            HTTPStatus.SEE_OTHER, _collection_location(bookmark["collection_id"])
        )

    def _handle_create_collection(self):
        """Create a collection, then redirect with ``303`` to ``/``."""
        fields = self._read_form()
        name = fields.get("name", "")
        form_state = {"name": name}
        try:
            clean_name = validation.validate_collection_name(name)
        except ValueError as error:
            return self._send_400(str(error), form_state)
        try:
            self.storage.create_collection(clean_name)
        except ValueError as error:
            return self._send_400(str(error), form_state)
        return self._redirect(HTTPStatus.SEE_OTHER, "/")

    def _handle_move(self, raw_id):
        """Move a record between collections, answering ``303`` or ``404``."""
        fields = self._read_form()
        moved = self.storage.move_bookmark(
            urllib.parse.unquote(raw_id), fields.get("collection_id", "")
        )
        if moved is None:
            return self._send_404("bookmark or collection not found")
        return self._redirect(
            HTTPStatus.SEE_OTHER, _collection_location(moved["collection_id"])
        )


class Application(http.server.ThreadingHTTPServer):
    """Threaded HTTP server carrying the storage and views collaborators."""

    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, server_address, storage, view_module=None, handler_class=None):
        """Bind the server and remember what each request handler needs."""
        super().__init__(server_address, handler_class or RequestHandler)
        self.storage = storage
        self.views = views if view_module is None else view_module


def make_server(config: app_config.Config, storage: app_storage.Storage):
    """Build (but do not start) an :class:`Application` for ``config``.

    The socket is bound to ``(config.host, config.port)`` but not yet served;
    the caller drives it with ``serve_forever()`` or ``handle_request()``.
    """
    return Application((config.host, config.port), storage)


def run(config: app_config.Config):
    """Create the data directory and Storage, then serve until interrupted.

    :class:`app.storage.Storage` creates ``config.data_dir`` when it is absent
    and opens ``library.sqlite3`` inside it, so all mutable state stays in the
    writable data directory while the source tree stays read-only. The server
    binds ``(config.host, config.port)`` -- loopback by default, or the literal
    managed-container host supplied on the command line.
    """
    storage = app_storage.Storage(config.data_dir)
    server = make_server(config, storage)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        storage.close()
