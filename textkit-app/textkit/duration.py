import re

_UNITS = {"h": 3600, "m": 60, "s": 1}
_DURATION_PART = re.compile(r"(\d+)([hms])")


def parse_duration(text: str) -> int:
    """Parse durations like "90s", "5m", "2h" or "1h30m" into seconds."""
    normalized = text.strip().lower()
    parts = list(_DURATION_PART.finditer(normalized))
    if not parts or "".join(part.group(0) for part in parts) != normalized:
        raise ValueError(f"not a duration: {text!r}")
    return sum(int(value) * _UNITS[unit] for value, unit in (part.groups() for part in parts))
