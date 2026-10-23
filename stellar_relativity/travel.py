"""Relativistic travel times between Earth and a star.

Uses the constant-velocity "cruise" idealisation: the traveller is assumed to
move at a fixed fraction of light speed for the whole trip (no acceleration /
deceleration phase). This cleanly isolates the time-dilation effect, which is
what we want to build intuition about.
"""

from __future__ import annotations

from dataclasses import dataclass

from .lighttravel import light_travel_years
from .lorentz import lorentz_factor


@dataclass(frozen=True)
class TravelResult:
    distance_ly: float
    beta: float
    gamma: float
    earth_time_years: float
    proper_time_years: float

    @property
    def years_saved(self) -> float:
        """How many fewer years the traveller ages vs. an Earth observer."""
        return self.earth_time_years - self.proper_time_years


def travel_times(distance_ly: float, beta: float) -> TravelResult:
    """Compute Earth-frame and traveller (proper) trip durations.

    * Earth frame: time = distance / speed = distance_ly / beta  (years).
    * Traveller:   proper time = Earth time / gamma  (years) — the moving
      clock runs slow, so the traveller ages less.
    """
    if beta <= 0:
        raise ValueError("beta must be > 0 to make the trip in finite time")
    gamma = lorentz_factor(beta)
    earth_time = light_travel_years(distance_ly) / beta
    proper_time = earth_time / gamma
    return TravelResult(
        distance_ly=float(distance_ly),
        beta=float(beta),
        gamma=gamma,
        earth_time_years=earth_time,
        proper_time_years=proper_time,
    )


__all__ = ["TravelResult", "travel_times"]
