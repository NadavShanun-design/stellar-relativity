import math

import pytest

from stellar_relativity.lorentz import lorentz_factor, rapidity, validate_beta


def test_gamma_at_rest_is_one():
    assert lorentz_factor(0.0) == pytest.approx(1.0)


def test_gamma_known_values():
    # At 0.6c, gamma is exactly 1.25; at 0.8c it is exactly 1/0.6 = 1.6667.
    assert lorentz_factor(0.6) == pytest.approx(1.25)
    assert lorentz_factor(0.8) == pytest.approx(5.0 / 3.0)


def test_gamma_grows_without_bound_near_c():
    assert lorentz_factor(0.999) > 22.0


def test_beta_must_be_subluminal():
    with pytest.raises(ValueError):
        validate_beta(1.0)
    with pytest.raises(ValueError):
        validate_beta(-0.1)


def test_rapidity_zero_at_rest():
    assert rapidity(0.0) == pytest.approx(0.0)
    assert rapidity(0.5) == pytest.approx(math.atanh(0.5))
