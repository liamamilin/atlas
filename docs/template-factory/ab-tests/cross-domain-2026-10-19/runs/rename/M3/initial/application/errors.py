"""User-facing error type for the batch renamer CLI.

Any AppError means: the request is refused or failed, so the process must
exit nonzero, print the message on stderr, and never emit a success JSON on
stdout.
"""


class AppError(Exception):
    """A refusal or failure that must exit nonzero with a stderr message."""
