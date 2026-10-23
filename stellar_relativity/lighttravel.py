"""Light-travel time: how old the light is that reaches us from a star."""

from __future__ import annotations

from .constants import SECONDS_PER_YEAR


def light_travel_years(distance_ly: float) -> float:
    """Years for light to travel ``distance_ly`` light years.

    By the definition of the light year this is numerically equal to the
    distance, but expressing it as a function keeps intent explicit.
    """
    if distance_ly < 0:
        raise ValueError("distance_ly must be non-negative")
    return float(distance_ly)


def light_travel_seconds(distance_ly: float) -> float:
    """Seconds for light to travel ``distance_ly`` light years."""
    return light_travel_years(distance_ly) * SECONDS_PER_YEAR


def departure_year(distance_ly: float, observation_year: float) -> float:
    """The year the light now arriving actually left the star.

    e.g. light from a star 4.25 ly away, observed in 2026, left in ~2021.7.
    """
    return observation_year - light_travel_years(distance_ly)


__all__ = ["light_travel_years", "light_travel_seconds", "departure_year"]
