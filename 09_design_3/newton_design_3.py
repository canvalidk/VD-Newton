"""Official entry strings for Newton Design 3. Load with VDfirst on the Python path."""

from engine import VDInstance


# Append one (headword, definition) pair per entry, in dictionary order.
NEWTON_ENTRIES: list[tuple[str, str]] = []


def build_newton_instance() -> VDInstance:
    """Build a fresh Design 3 dictionary from the entries in this file."""
    dictionary = VDInstance(name="Newton Design 3")
    dictionary.append_many(NEWTON_ENTRIES)
    return dictionary
