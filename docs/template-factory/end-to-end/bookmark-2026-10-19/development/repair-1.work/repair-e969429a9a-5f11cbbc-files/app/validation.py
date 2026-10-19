"""Pure validation helpers shared by the HTTP and storage layers.

The P0 library stores only absolute ``http``/``https`` URLs (D04). These
helpers are side-effect free and import nothing from ``sqlite3`` or
``http.server``, so ``app/server.py`` can call them to answer ``400`` before
touching storage and ``app/storage.py`` can reuse them as a last line of
defence.

Two URL helpers share one rule set:

* ``is_valid_http_url(value)`` returns a ``bool`` and never raises.
* ``normalize_url(value)`` returns the cleaned URL string or raises
  ``ValueError`` -- the convention this codebase already uses for rejected
  input (see ``Storage.create_collection``).

A URL is accepted only when it is absolute, uses the ``http`` or ``https``
scheme and carries a host. Empty input, plain text such as ``not a url``,
host-less strings such as ``http://``, unparsable authorities and any other
scheme (``javascript:``, ``data:``, ``ftp:``, ...) are rejected. A URL that
carries a raw control character -- a CR or LF above all, but any C0/C1 control
or DEL -- is rejected outright rather than having the dangerous character
stripped and the remaining text accepted, because an accepted URL is persisted
verbatim and later copied into the ``Location`` header by ``GET /go/<id>``.
An accepted URL is returned verbatim except for surrounding whitespace, so what
is stored and shown is exactly what the user submitted.

``clean_title`` implements D05: a manual title is trimmed and a blank title
falls back to the URL. ``validate_collection_name`` guarantees a collection is
never created without a name.
"""

import urllib.parse

__all__ = [
    "normalize_url",
    "is_valid_http_url",
    "clean_title",
    "validate_collection_name",
]

#: Schemes the library is willing to store. Everything else (``javascript:``,
#: ``data:``, ``ftp:``, ``mailto:``, ``file:`` ...) is refused before it can
#: reach the database.
_ALLOWED_SCHEMES = ("http", "https")


def _contains_control_characters(value):
    """Return ``True`` when ``value`` carries a raw control character.

    C0 controls (``U+0000``-``U+001F``), DEL (``U+007F``) and the C1 controls
    (``U+0080``-``U+009F``) are refused. A raw CR or LF in a submitted URL
    would be persisted and later copied into the ``Location`` header by
    ``GET /go/<id>``, allowing response-header injection; rejecting the input
    here stops such a value before it can be parsed, normalized or saved.
    """
    for character in str(value):
        codepoint = ord(character)
        if codepoint < 0x20 or 0x7F <= codepoint <= 0x9F:
            return True
    return False


def _split(value):
    """Return ``(parts, text)`` for a candidate URL, or ``(None, "")``.

    ``text`` is the candidate with surrounding whitespace removed. ``None``
    is returned when the value is missing, blank, unparsable or carries raw
    whitespace inside its authority -- all of which make it malformed. The
    raw control-character test runs on the input before any whitespace is
    trimmed, so a dangerous CR or LF is rejected rather than silently stripped
    and a different value accepted in its place.
    """
    if value is None:
        return None, ""
    raw = str(value)
    if _contains_control_characters(raw):
        return None, ""
    text = raw.strip()
    if not text:
        return None, ""
    try:
        parts = urllib.parse.urlsplit(text)
    except ValueError:
        # e.g. an unclosed IPv6 literal in the authority.
        return None, ""
    if not parts.netloc:
        return None, ""
    if any(character.isspace() for character in parts.netloc):
        return None, ""
    return parts, text


def is_valid_http_url(value):
    """Return ``True`` only for an absolute ``http``/``https`` URL with a host.

    Never raises. ``None``, empty or whitespace-only input, host-less strings
    such as ``http://``, malformed text such as ``not a url``, any input
    carrying a raw control character and every non-``http(s)`` scheme
    (``javascript:``, ``data:``, ``ftp:``, ...) all return ``False``.
    """
    parts, _text = _split(value)
    if parts is None:
        return False
    if parts.scheme.lower() not in _ALLOWED_SCHEMES:
        return False
    if not parts.hostname:
        return False
    try:
        # Touching ``port`` validates it, so ``http://host:bad`` is refused.
        parts.port
    except ValueError:
        return False
    return True


def normalize_url(value):
    """Return ``value`` as a storable URL, or raise ``ValueError``.

    The result is the input with surrounding whitespace removed and is
    otherwise unchanged, so an accepted URL is persisted and echoed exactly.
    Invalid input -- including any raw control character, which is never
    stripped and accepted -- raises ``ValueError`` with a message safe to show
    on the frozen ``400`` error page.
    """
    if not is_valid_http_url(value):
        raise ValueError("a valid absolute http(s) URL is required")
    return str(value).strip()


def clean_title(title, url=""):
    """Return the display title for a bookmark (D05).

    A manually entered ``title`` is trimmed; when it is blank the saved
    ``url`` is used instead so a record always has something to show. This
    helper never raises: a missing title and URL simply yield ``""``.
    """
    text = "" if title is None else str(title).strip()
    if text:
        return text
    return "" if url is None else str(url).strip()


def validate_collection_name(name):
    """Return a collection name trimmed, or raise ``ValueError`` when blank.

    A collection must carry a non-empty name; the caller turns the
    ``ValueError`` into the frozen ``400`` response before writing to
    storage.
    """
    text = "" if name is None else str(name).strip()
    if not text:
        raise ValueError("collection name is required")
    return text