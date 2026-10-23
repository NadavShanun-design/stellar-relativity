"""Side-by-side comparison of every star in the catalog."""

from __future__ import annotations

from typing import List, Optional
from pathlib import Path

from .catalog import load_catalog
from .lighttravel import light_travel_years
from .travel import travel_times


def comparison_rows(beta: float = 0.9, path: Optional[Path] = None) -> List[dict]:
    """Return one dict per star with the key relativistic quantities."""
    rows = []
    for star in load_catalog(path):
        trip = travel_times(star.distance_ly, beta)
        rows.append(
            {
                "name": star.name,
                "distance_ly": star.distance_ly,
                "light_years_ago": light_travel_years(star.distance_ly),
                "earth_trip_years": trip.earth_time_years,
                "onboard_trip_years": trip.proper_time_years,
                "years_saved": trip.years_saved,
            }
        )
    return rows


def comparison_table(beta: float = 0.9, path: Optional[Path] = None) -> str:
    """Return a fixed-width ASCII table comparing all stars at speed ``beta``."""
    rows = comparison_rows(beta=beta, path=path)
    header = (
        f"{'Star':22} {'Dist(ly)':>9} {'LightAgo':>9} "
        f"{'Earth(yr)':>10} {'Onboard(yr)':>12} {'Saved(yr)':>10}"
    )
    sep = "-" * len(header)
    lines = [f"Travel at {beta*100:.1f}% the speed of light", "", header, sep]
    for r in rows:
        lines.append(
            f"{r['name']:22} {r['distance_ly']:>9.3f} {r['light_years_ago']:>9.3f} "
            f"{r['earth_trip_years']:>10.3f} {r['onboard_trip_years']:>12.3f} "
            f"{r['years_saved']:>10.3f}"
        )
    return "\n".join(lines)


__all__ = ["comparison_rows", "comparison_table"]
