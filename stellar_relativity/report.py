"""Human-readable relativity reports for a single star."""

from __future__ import annotations

from typing import List

from .catalog import Star, find
from .doppler import redshift_z, wavelength_ratio
from .lighttravel import departure_year, light_travel_years
from .travel import travel_times

# A reference observation year used when none is supplied.
DEFAULT_OBSERVATION_YEAR = 2026


def report_lines(star: Star, beta: float = 0.9, observation_year: int = DEFAULT_OBSERVATION_YEAR) -> List[str]:
    """Build a list of report lines for ``star`` travelled at speed ``beta``."""
    lt = light_travel_years(star.distance_ly)
    left = departure_year(star.distance_ly, observation_year)
    trip = travel_times(star.distance_ly, beta)
    # Approaching the star blueshifts its light (negative beta convention).
    ratio = wavelength_ratio(-beta)
    z = redshift_z(-beta)

    pct = beta * 100
    lines = [
        f"{star.name}  ({star.spectral_type}, {star.constellation})",
        f"  distance            : {star.distance_ly:.4g} ly  ({star.distance_parsecs:.4g} pc)",
        f"  apparent magnitude  : {star.apparent_magnitude:+.2f}",
        "",
        f"  light-travel time   : {lt:.4g} years",
        f"  light seen in {observation_year} left in : {left:.1f}",
        "",
        f"  cruising at {pct:.1f}% c:",
        f"    Lorentz factor    : {trip.gamma:.4f}",
        f"    Earth-frame trip  : {trip.earth_time_years:.3f} years",
        f"    your onboard trip : {trip.proper_time_years:.3f} years",
        f"    you age {trip.years_saved:.3f} years less than everyone back home",
        "",
        f"  its light, approached at {pct:.1f}% c:",
        f"    wavelength x {ratio:.4f}  (z = {z:+.4f}, blueshifted)",
    ]
    return lines


def report(name: str, beta: float = 0.9, observation_year: int = DEFAULT_OBSERVATION_YEAR) -> str:
    """Return a formatted report for the star named ``name``."""
    star = find(name)
    return "\n".join(report_lines(star, beta=beta, observation_year=observation_year))


__all__ = ["report", "report_lines", "DEFAULT_OBSERVATION_YEAR"]
