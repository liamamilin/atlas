"""Pure filename helpers: literal replacement and safe bare-name checks."""

import os

# Characters that must never appear in a single generated file name.
_FORBIDDEN = ("/", "\\")


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
