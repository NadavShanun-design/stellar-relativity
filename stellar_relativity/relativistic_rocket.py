"""Constant-acceleration ("flip-and-burn") interstellar travel.

A more realistic model than the constant-velocity cruise in ``travel.py``:
the ship accelerates at a constant *proper* acceleration (what the crew feels,
e.g. a comfortable 1 g) for the first half of the trip, flips over, and
decelerates for the second half, arriving at rest.

Formulas are the standard relativistic-rocket equations. For acceleration ``a``
over a half-distance ``x = d/2`` starting from rest:

    gamma_mid = 1 + a*x/c**2
    ship_time  = 2 * (c/a) * arccosh(gamma_mid)
    earth_time = 2 * (c/a) * sqrt(gamma_mid**2 - 1)
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from .constants import C_M_PER_S, LIGHT_YEAR_M, SECONDS_PER_YEAR

STANDARD_GRAVITY = 9.80665  # m/s**2 — one "g"


@dataclass(frozen=True)
class RocketTrip:
    distance_ly: float
    g_force: float
    ship_time_years: float
    earth_time_years: float
    peak_gamma: float
    peak_beta: float


def flip_and_burn(distance_ly: float, g_force: float = 1.0) -> RocketTrip:
    """Compute a flip-and-burn trip at constant proper acceleration.

    ``g_force`` is the acceleration in multiples of Earth gravity (1.0 = 1 g).
    """
    if distance_ly <= 0:
        raise ValueError("distance_ly must be positive")
    if g_force <= 0:
        raise ValueError("g_force must be positive")

    a = g_force * STANDARD_GRAVITY
    c = C_M_PER_S
    half_distance_m = (distance_ly * LIGHT_YEAR_M) / 2.0

    peak_gamma = 1.0 + a * half_distance_m / (c * c)
    peak_beta = math.sqrt(1.0 - 1.0 / (peak_gamma * peak_gamma))

    ship_seconds = 2.0 * (c / a) * math.acosh(peak_gamma)
    earth_seconds = 2.0 * (c / a) * math.sqrt(peak_gamma * peak_gamma - 1.0)

    return RocketTrip(
        distance_ly=float(distance_ly),
        g_force=float(g_force),
        ship_time_years=ship_seconds / SECONDS_PER_YEAR,
        earth_time_years=earth_seconds / SECONDS_PER_YEAR,
        peak_gamma=peak_gamma,
        peak_beta=peak_beta,
    )


__all__ = ["RocketTrip", "flip_and_burn", "STANDARD_GRAVITY"]
