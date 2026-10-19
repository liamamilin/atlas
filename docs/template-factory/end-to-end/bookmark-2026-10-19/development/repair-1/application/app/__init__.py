"""Application package for the P0 bookmark manager.

The package exposes a single module-level constant, ``__version__``, so the
launch path and operator tooling can report which release is running. Importing
this package has no side effects: it opens no files, creates no directories and
contacts no network or database resources.
"""

__all__ = ["__version__"]

__version__ = "0.1.0"
