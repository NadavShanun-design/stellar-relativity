"""Relativistic aberration of starlight.

When you travel fast, the stars appear to crowd toward the direction you're
heading (the "headlight" / stellar-aberration effect). A star seen at angle
``theta`` from your direction of motion in the rest frame appears at ``theta'``:

    cos(theta') = (cos(theta) + beta) / (1 + beta * cos(theta))
"""

from __future__ import annotations

import math


def aberrated_angle_deg(theta_deg: float, beta: float) -> float:
    """Apparent angle (degrees from heading) of a star while moving at ``beta``.

    ``theta_deg`` is the star's true angle from the direction of motion
    (0 deg = straight ahead, 180 deg = directly behind).
    """
    if not 0.0 <= beta < 1.0:
        raise ValueError(f"beta must satisfy 0 <= beta < 1, got {beta}")
    theta = math.radians(theta_deg)
    cos_t = math.cos(theta)
    cos_tp = (cos_t + beta) / (1.0 + beta * cos_t)
    cos_tp = max(-1.0, min(1.0, cos_tp))  # guard floating-point drift
    return math.degrees(math.acos(cos_tp))


def forward_hemisphere_fraction(beta: float) -> float:
    """Fraction of the full sky that collapses into the forward hemisphere.

    At rest this is 0.5; as beta -> 1 it approaches 1.0 (the whole sky bunches
    ahead). Derived from the aberration of the theta = 90 deg boundary.
    """
    if not 0.0 <= beta < 1.0:
        raise ValueError(f"beta must satisfy 0 <= beta < 1, got {beta}")
    # Stars with true angle up to theta_max map into the forward hemisphere,
    # where cos(theta_max) = -beta (the ring that aberrates to exactly 90 deg).
    theta_max = math.acos(-beta)
    # Solid angle of a cone of half-angle theta_max, as a fraction of 4*pi.
    return (1.0 - math.cos(theta_max)) / 2.0


__all__ = ["aberrated_angle_deg", "forward_hemisphere_fraction"]
