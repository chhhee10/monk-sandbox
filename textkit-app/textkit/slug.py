import re


def slugify(title: str) -> str:
    """Lowercase URL slug: letters and digits joined by single dashes."""
    lowered = title.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", lowered)
    return slug.strip("-")
