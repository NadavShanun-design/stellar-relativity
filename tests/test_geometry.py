import math

import pytest

from stellar_relativity.geometry import (
    angular_separation_deg,
    cartesian,
    separation_ly,
)


def test_cartesian_magnitude_equals_distance():
    x, y, z = cartesian(14.4959, -62.6794, 4.2465)
    assert math.sqrt(x * x + y * y + z * z) == pytest.approx(4.2465)


def test_pole_points_along_z():
    x, y, z = cartesian(0.0, 90.0, 10.0)
    assert z == pytest.approx(10.0)
    assert x == pytest.approx(0.0, abs=1e-9)
    assert y == pytest.approx(0.0, abs=1e-9)


def test_angular_separation_identity_is_zero():
    assert angular_separation_deg(6.0, 10.0, 6.0, 10.0) == pytest.approx(0.0, abs=1e-6)


def test_angular_separation_symmetric():
    a = angular_separation_deg(6.75, -16.7, 14.5, -62.7)
    b = angular_separation_deg(14.5, -62.7, 6.75, -16.7)
    assert a == pytest.approx(b)


def test_separation_ly_between_alpha_cen_components_is_small():
    # Alpha Cen A and B are at essentially the same spot in our catalog.
    d = separation_ly(14.66, -60.8356, 4.365, 14.66, -60.8389, 4.365)
    assert d < 0.01
