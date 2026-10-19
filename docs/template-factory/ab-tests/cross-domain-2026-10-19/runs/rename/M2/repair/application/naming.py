"""Pure filename helpers: literal replacement and safe bare-name checks."""

import os
import string

# Characters that must never appear in a single generated file name.
_FORBIDDEN = ("/", "\\")

# Conservative allow-list for values that may be turned into a file-name
# component of durable state (plan ids). Generated ids are hex, so this only
# rejects tampered or unexpected values.
_TOKEN_CHARS = frozenset(string.ascii_letters + string.digits + "._-")


def is_bare_name(name):
    """Return True only for a single, safe, relative file name.

    Rejects empty names, "." / "..", names containing path separators, names
    containing NUL, and anything that is not identical to its own basename.
    """
    if not isinstance(name, str):
        return False
    if name == "" or name in (".", ".."):
        return False
    if "\x00" in name:
        return False
    for ch in _FORBIDDEN:
        if ch in name:
            return False
    if os.altsep and os.altsep in name:
        return False
    if os.sep in name:
        return False
    if os.path.basename(name) != name:
        return False
    return True


def is_state_token(value):
    """Return True only for a safe single-segment token usable as a file name.

    Used for untrusted plan fields (such as the plan ``id``) before they are
    turned into a durable state path. Rejects empty values, ``.``/``..``, any
    path separator, and any character outside a conservative allow-list, so an
    absolute or traversal value can never act as a path component.
    """
    if not isinstance(value, str) or value == "":
        return False
    if value in (".", ".."):
        return False
    return all(ch in _TOKEN_CHARS for ch in value)


def compute_replacements(names, find, replace):
    """Return [(old, new)] for names containing the literal ``find``.

    Matching is plain literal substring matching (never regex). No-op entries
    where the name is unchanged are dropped.
    """
    operations = []
    for name in names:
        if find in name:
            new = name.replace(find, replace)
            if new != name:
                operations.append((name, new))
    return operations
