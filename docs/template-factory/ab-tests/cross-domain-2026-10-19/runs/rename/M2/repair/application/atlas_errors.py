"""Shared error type for the rename CLI.

An AtlasError represents an operational refusal. It is surfaced to stderr and
causes a nonzero exit; it never produces success JSON on stdout.
"""


class AtlasError(Exception):
    """A refusal that must be reported on stderr with a nonzero exit code."""
