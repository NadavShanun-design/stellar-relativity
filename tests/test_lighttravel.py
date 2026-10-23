import pytest

from stellar_relativity.constants import SECONDS_PER_YEAR
from stellar_relativity.lighttravel import (
    departure_year,
    light_travel_seconds,
    light_travel_years,
)


def test_light_travel_years_equals_distance():
    assert light_travel_years(4.2465) == pytest.approx(4.2465)


def test_light_travel_seconds():
    assert light_travel_seconds(1.0) == pytest.approx(SECONDS_PER_YEAR)


def test_departure_year():
    # Light from 4.25 ly away, observed in 2026, left in ~2021.75.
    assert departure_year(4.25, 2026) == pytest.approx(2021.75)


def test_negative_distance_rejected():
    with pytest.raises(ValueError):
        light_travel_years(-1.0)
