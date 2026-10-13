"""Small text helpers."""

import re


def slugify(text):
    """Turn text into a lowercase, hyphen-separated slug.

    >>> slugify("Hello, World!")
    'hello-world'
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")
