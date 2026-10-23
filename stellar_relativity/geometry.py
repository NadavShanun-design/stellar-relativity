"""3D geometry of the stellar neighbourhood, Sun at the origin.

Positions are computed in a cartesian equatorial frame (ICRS-aligned):
    +x -> towards RA 0h on the celestial equator
    +y -> towards RA 6h on the celestial equator
    +z -> towards the north celestial pole
with all coordinates in light years.
"""

from __future__ import annotations

import math
from typing import Tuple


def _radians_from_ra_dec(ra_hours: float, dec_deg: float) -> Tuple[float, float]:
    ra_rad = math.radians(ra_hours * 15.0)  # 24h -> 360deg
    dec_rad = math.radians(dec_deg)
    return ra_rad, dec_rad


def cartesian(ra_hours: float, dec_deg: float, distance_ly: float) -> Tuple[float, float, float]:
    """Return (x, y, z) in light years for a star's spherical coordinates."""
    ra, dec = _radians_from_ra_dec(ra_hours, dec_deg)
    x = distance_ly * math.cos(dec) * math.cos(ra)
    y = distance_ly * math.cos(dec) * math.sin(ra)
    z = distance_ly * math.sin(dec)
    return (x, y, z)


def angular_separation_deg(
    ra1_hours: float, dec1_deg: float, ra2_hours: float, dec2_deg: float
) -> float:
    """Great-circle angle (degrees) between two sky positions as seen from Earth."""
    ra1, dec1 = _radians_from_ra_dec(ra1_hours, dec1_deg)
    ra2, dec2 = _radians_from_ra_dec(ra2_hours, dec2_deg)
    cos_sep = (
        math.sin(dec1) * math.sin(dec2)
        + math.cos(dec1) * math.cos(dec2) * math.cos(ra1 - ra2)
    )
    cos_sep = max(-1.0, min(1.0, cos_sep))  # guard floating-point drift
    return math.degrees(math.acos(cos_sep))


def separation_ly(
    ra1_hours: float, dec1_deg: float, dist1_ly: float,
    ra2_hours: float, dec2_deg: float, dist2_ly: float,
) -> float:
    """Actual 3D distance (light years) between two stars."""
    x1, y1, z1 = cartesian(ra1_hours, dec1_deg, dist1_ly)
    x2, y2, z2 = cartesian(ra2_hours, dec2_deg, dist2_ly)
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)


__all__ = ["cartesian", "angular_separation_deg", "separation_ly"]
