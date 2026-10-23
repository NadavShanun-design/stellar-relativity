"""A tiny ASCII sky map of the catalog (right ascension vs. declination)."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from .catalog import load_catalog


def ascii_sky(width: int = 72, height: int = 22, path: Optional[Path] = None) -> str:
    """Return a multi-line ASCII chart plotting every star by RA (x) and Dec (y)."""
    if width < 10 or height < 6:
        raise ValueError("width >= 10 and height >= 6 required")
    grid = [[" "] * width for _ in range(height)]

    for star in load_catalog(path):
        x = int((star.ra_hours / 24.0) * (width - 1))
        y = int(((90.0 - star.dec_deg) / 180.0) * (height - 1))
        x = max(0, min(width - 1, x))
        y = max(0, min(height - 1, y))
        grid[y][x] = "*"

    rows = ["".join(r) for r in grid]
    ruler = "+" + "-" * (width - 2) + "+"
    header = "RA 0h" + " " * (width - 11) + "RA 24h"
    out = [header, ruler]
    out += ["|" + r[1:-1] + "|" for r in rows]
    out += [ruler, "(north celestial pole at top, south at bottom)"]
    return "\n".join(out)


__all__ = ["ascii_sky"]
