"""Structured (JSON-serialisable) export of relativity data.

Useful for feeding the web visualisation or any downstream consumer.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

from .catalog import Star, load_catalog
from .doppler import redshift_z
from .geometry import cartesian
from .lighttravel import departure_year, light_travel_years
from .travel import travel_times
from .report import DEFAULT_OBSERVATION_YEAR


def star_payload(star: Star, beta: float, observation_year: int) -> dict:
    """Build the full data dictionary for a single star."""
    trip = travel_times(star.distance_ly, beta)
    x, y, z = cartesian(star.ra_hours, star.dec_deg, star.distance_ly)
    return {
        "name": star.name,
        "spectral_type": star.spectral_type,
        "constellation": star.constellation,
        "apparent_magnitude": star.apparent_magnitude,
        "distance_ly": star.distance_ly,
        "distance_pc": star.distance_parsecs,
        "position_ly": {"x": x, "y": y, "z": z},
        "light_travel_years": light_travel_years(star.distance_ly),
        "light_departed_year": departure_year(star.distance_ly, observation_year),
        "travel": {
            "beta": beta,
            "gamma": trip.gamma,
            "earth_time_years": trip.earth_time_years,
            "proper_time_years": trip.proper_time_years,
            "years_saved": trip.years_saved,
        },
        "approach_blueshift_z": redshift_z(-beta),
    }


def export_catalog(
    beta: float = 0.9,
    observation_year: int = DEFAULT_OBSERVATION_YEAR,
    path: Optional[Path] = None,
) -> dict:
    """Return a dict describing every star, ready to ``json.dumps``."""
    return {
        "observation_year": observation_year,
        "beta": beta,
        "stars": [star_payload(s, beta, observation_year) for s in load_catalog(path)],
    }


def export_json(beta: float = 0.9, observation_year: int = DEFAULT_OBSERVATION_YEAR, indent: int = 2) -> str:
    """Return the catalog export as a JSON string."""
    return json.dumps(export_catalog(beta, observation_year), indent=indent)


__all__ = ["star_payload", "export_catalog", "export_json"]
