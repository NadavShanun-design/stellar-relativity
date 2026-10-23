import pytest

from stellar_relativity.aberration import (
    aberrated_angle_deg,
    forward_hemisphere_fraction,
)


def test_no_aberration_at_rest():
    assert aberrated_angle_deg(90.0, 0.0) == pytest.approx(90.0)
    assert aberrated_angle_deg(45.0, 0.0) == pytest.approx(45.0)


def test_stars_shift_forward_when_moving():
    # A star at 90 deg appears pulled toward the front (smaller angle).
    assert aberrated_angle_deg(90.0, 0.5) < 90.0


def test_straight_ahead_stays_ahead():
    assert aberrated_angle_deg(0.0, 0.7) == pytest.approx(0.0, abs=1e-9)


def test_forward_hemisphere_grows_with_speed():
    assert forward_hemisphere_fraction(0.0) == pytest.approx(0.5)
    assert forward_hemisphere_fraction(0.9) > 0.5
    assert forward_hemisphere_fraction(0.99) > forward_hemisphere_fraction(0.9)


def test_beta_out_of_range():
    with pytest.raises(ValueError):
        aberrated_angle_deg(90.0, 1.0)
