"""Command-line configuration for the P0 bookmark manager.

``parse_args`` is the only place that reads process arguments and turns them
into an immutable :class:`Config`:

* ``--host`` -- interface to bind.  Defaults to ``127.0.0.1`` (loopback) so a
  normal local run is never exposed; the managed container delivery passes the
  literal ``--host 0.0.0.0`` because the container port is published on the
  host as ``127.0.0.1`` only.
* ``--port`` -- TCP port.  Defaults to ``8000`` and must be an integer in the
  ``1024``-``65535`` range.
* ``--data-dir`` -- directory holding all mutable state.  Defaults to
  ``./state`` and is created when it does not already exist.

This module never opens the database itself.  ``app.server.run`` receives the
returned :class:`Config` for binding and to locate ``library.sqlite3`` inside
the data directory.  Importing this module has no side effects.
"""

import argparse
import os
from dataclasses import dataclass

__all__ = [
    "Config",
    "parse_args",
    "validate_port",
    "DEFAULT_HOST",
    "DEFAULT_PORT",
    "DEFAULT_DATA_DIR",
]

#: Default bind interface: loopback, so local use stays private.
DEFAULT_HOST = "127.0.0.1"

#: Default TCP port for the local server.
DEFAULT_PORT = 8000

#: Default mutable-state directory, relative to the current working directory.
DEFAULT_DATA_DIR = "./state"

#: Lowest and highest accepted TCP port numbers.
MIN_PORT = 1024
MAX_PORT = 65535

#: SQLite file name created directly beneath the data directory.
DB_FILENAME = "library.sqlite3"


def validate_port(value):
    """Return ``value`` as an ``int`` in the ``1024``-``65535`` range.

    Used as the argparse ``type`` for ``--port`` so a bad value produces a
    usage error (``argparse.ArgumentTypeError``).  Called directly it raises
    the same exception type for non-numeric or out-of-range input.
    """

    try:
        port = int(value)
    except (TypeError, ValueError):
        raise argparse.ArgumentTypeError(
            "port must be an integer, got {0!r}".format(value)
        )
    if port < MIN_PORT or port > MAX_PORT:
        raise argparse.ArgumentTypeError(
            "port must be between {0} and {1}, got {2}".format(
                MIN_PORT, MAX_PORT, port
            )
        )
    return port


@dataclass(frozen=True)
class Config:
    """Resolved, immutable server configuration.

    Instances are hashable and cannot be mutated after construction, so the
    values handed to the storage and HTTP layers cannot change underneath them.
    ``db_path`` names the on-disk SQLite file inside ``data_dir``.
    """

    host: str = DEFAULT_HOST
    port: int = DEFAULT_PORT
    data_dir: str = DEFAULT_DATA_DIR

    def __post_init__(self):
        host = str(self.host).strip()
        data_dir = str(self.data_dir).strip()
        try:
            port = int(self.port)
        except (TypeError, ValueError):
            raise ValueError(
                "port must be an integer, got {0!r}".format(self.port)
            )
        if not host:
            raise ValueError("host must be a non-empty interface name")
        if not data_dir:
            raise ValueError("data_dir must be a non-empty directory path")
        if port < MIN_PORT or port > MAX_PORT:
            raise ValueError(
                "port must be between {0} and {1}, got {2}".format(
                    MIN_PORT, MAX_PORT, port
                )
            )
        object.__setattr__(self, "host", host)
        object.__setattr__(self, "data_dir", data_dir)
        object.__setattr__(self, "port", port)

    @property
    def db_path(self):
        """Path of the SQLite library file, ``<data_dir>/library.sqlite3``."""

        return os.path.join(self.data_dir, DB_FILENAME)


def parse_args(argv=None):
    """Parse ``argv`` (defaulting to ``sys.argv[1:]``) into a :class:`Config`.

    ``--host`` defaults to loopback, ``--port`` defaults to ``8000`` and is
    validated to the ``1024``-``65535`` range, and ``--data-dir`` defaults to
    ``./state`` and is created when absent.  The managed container delivery
    supplies the literal ``0.0.0.0`` / ``8000`` / ``/state/data`` values.
    """

    parser = argparse.ArgumentParser(
        prog="app",
        description="Serve the private single-user bookmark library.",
    )
    parser.add_argument(
        "--host",
        default=DEFAULT_HOST,
        metavar="HOST",
        help="interface to bind; default %(default)s keeps a local run on loopback.",
    )
    parser.add_argument(
        "--port",
        type=validate_port,
        default=DEFAULT_PORT,
        metavar="PORT",
        help="TCP port in the 1024-65535 range; default %(default)s.",
    )
    parser.add_argument(
        "--data-dir",
        dest="data_dir",
        default=DEFAULT_DATA_DIR,
        metavar="DIR",
        help="directory for mutable state, created if absent; default %(default)s.",
    )

    args = parser.parse_args(argv)

    try:
        os.makedirs(args.data_dir, exist_ok=True)
    except OSError as error:
        parser.error(
            "cannot create data directory {0!r}: {1}".format(args.data_dir, error)
        )

    return Config(host=args.host, port=args.port, data_dir=args.data_dir)
