import pytest

from stellar_relativity.travel import travel_times


def test_earth_time_is_distance_over_beta():
    r = travel_times(10.0, 0.5)
    assert r.earth_time_years == pytest.approx(20.0)


def test_proper_time_is_shorter_than_earth_time():
    r = travel_times(10.0, 0.8)
    assert r.proper_time_years < r.earth_time_years
    assert r.years_saved > 0


def test_proper_time_matches_gamma():
    r = travel_times(4.2465, 0.9)
    assert r.proper_time_years == pytest.approx(r.earth_time_years / r.gamma)


def test_proxima_at_90pct_c():
    # Proxima is 4.2465 ly; at 0.9c Earth sees ~4.718 yr, traveller ~2.057 yr.
    r = travel_times(4.2465, 0.9)
    assert r.earth_time_years == pytest.approx(4.7183, abs=1e-3)
    assert r.proper_time_years == pytest.approx(2.0572, abs=1e-3)


def test_zero_beta_rejected():
    with pytest.raises(ValueError):
        travel_times(10.0, 0.0)
