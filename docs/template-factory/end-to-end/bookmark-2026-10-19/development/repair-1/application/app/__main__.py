"""Executable module entry point for ``python -m app``.

All runtime configuration comes from the command line: ``app.config.parse_args``
reads ``--host`` (which defaults to loopback for normal local use), ``--port``
and ``--data-dir``, and ``app.server.run`` opens the SQLite library and serves
the HTML interface. This module holds only that glue so argument parsing and the
HTTP wiring stay in their own modules and remain independently testable.
"""

import sys

from app import config, server

__all__ = ["main"]


def main(argv=None):
    """Parse command-line arguments and serve the bookmark library.

    When ``argv`` is omitted the process arguments (``sys.argv[1:]``) are used,
    matching ``python -m app``. The managed container delivery passes the host,
    port and data directory literally, e.g.
    ``--host 0.0.0.0 --port 8000 --data-dir /state/data``; omitting ``--host``
    keeps the server bound to loopback for a private local run.
    """
    arguments = sys.argv[1:] if argv is None else list(argv)
    settings = config.parse_args(arguments)
    server.run(settings)


if __name__ == "__main__":
    raise SystemExit(main())
