from __future__ import annotations

EXACT_MATCH_COLUMN = "Includes exact match(es)"


def highlight_exact_matches(cell: str) -> str | None:
    if "Y" in str(cell):
        return "background-color: green"

    return None
