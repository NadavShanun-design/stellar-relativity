import pytest

from stellar_relativity.relativistic_rocket import flip_and_burn


def test_proxima_at_1g_matches_known_figures():
    # The classic result: ~3.5 yr ship time, ~5.9 yr Earth time to ~4.25 ly at 1 g.
    trip = flip_and_burn(4.2465, g_force=1.0)
    assert trip.ship_time_years == pytest.approx(3.54, abs=0.1)
    assert trip.earth_time_years == pytest.approx(5.87, abs=0.1)


def test_ship_time_is_shorter_than_earth_time():
    trip = flip_and_burn(10.0, g_force=1.0)
    assert trip.ship_time_years < trip.earth_time_years


def test_peak_speed_is_subluminal():
    trip = flip_and_burn(25.0, g_force=1.0)
    assert 0 < trip.peak_beta < 1
    assert trip.peak_gamma > 1


def test_higher_g_is_faster():
    slow = flip_and_burn(10.0, g_force=1.0)
    fast = flip_and_burn(10.0, g_force=3.0)
    assert fast.ship_time_years < slow.ship_time_years


def test_invalid_inputs():
    with pytest.raises(ValueError):
        flip_and_burn(0.0, 1.0)
    with pytest.raises(ValueError):
        flip_and_burn(10.0, 0.0)
