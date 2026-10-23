import pytest

from stellar_relativity import constants as k


def test_light_year_definition():
    assert k.LIGHT_YEAR_M == pytest.approx(k.C_M_PER_S * k.SECONDS_PER_YEAR)


def test_parsec_in_light_years():
    assert k.PARSEC_IN_LY == pytest.approx(3.2615638, abs=1e-4)


def test_seconds_per_year_is_julian():
    assert k.SECONDS_PER_YEAR == pytest.approx(31_557_600.0)
