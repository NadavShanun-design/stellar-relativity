"""Loading and querying the nearby-star catalog in ``data/stars.json``."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

_DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "stars.json"


@dataclass(frozen=True)
class Star:
    """A single catalog entry describing a nearby star."""

    name: str
    distance_ly: float
    ra_hours: float
    dec_deg: float
    spectral_type: str
    constellation: str
    apparent_magnitude: float

    @property
    def distance_parsecs(self) -> float:
        from .constants import PARSEC_IN_LY

        return self.distance_ly / PARSEC_IN_LY


def load_catalog(path: Optional[Path] = None) -> List[Star]:
    """Load every star from the JSON catalog, sorted by distance from the Sun."""
    source = Path(path) if path else _DATA_PATH
    with source.open(encoding="utf-8") as fh:
        payload = json.load(fh)
    stars = [
        Star(
            name=entry["name"],
            distance_ly=float(entry["distance_ly"]),
            ra_hours=float(entry["ra_hours"]),
            dec_deg=float(entry["dec_deg"]),
            spectral_type=entry["spectral_type"],
            constellation=entry["constellation"],
            apparent_magnitude=float(entry["apparent_magnitude"]),
        )
        for entry in payload["stars"]
    ]
    return sorted(stars, key=lambda s: s.distance_ly)


def find(name: str, path: Optional[Path] = None) -> Star:
    """Look up a star by name (case-insensitive, whitespace-tolerant).

    Raises ``KeyError`` with the closest suggestions if nothing matches.
    """
    target = name.strip().casefold()
    stars = load_catalog(path)
    for star in stars:
        if star.name.casefold() == target:
            return star
    # Fall back to a forgiving substring match before giving up.
    partial = [s for s in stars if target in s.name.casefold()]
    if len(partial) == 1:
        return partial[0]
    available = ", ".join(s.name for s in stars)
    raise KeyError(f"No star named {name!r}. Known stars: {available}")


__all__ = ["Star", "load_catalog", "find"]
