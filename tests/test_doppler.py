import pytest

from stellar_relativity.doppler import (
    frequency_ratio,
    redshift_z,
    shifted_wavelength_nm,
    wavelength_ratio,
)


def test_no_shift_at_rest():
    assert wavelength_ratio(0.0) == pytest.approx(1.0)
    assert redshift_z(0.0) == pytest.approx(0.0)


def test_recession_redshifts():
    assert wavelength_ratio(0.5) > 1.0
    assert redshift_z(0.5) > 0.0


def test_approach_blueshifts():
    assert wavelength_ratio(-0.5) < 1.0
    assert redshift_z(-0.5) < 0.0


def test_frequency_is_inverse_of_wavelength():
    assert frequency_ratio(0.3) == pytest.approx(1.0 / wavelength_ratio(0.3))


def test_shifted_line():
    # H-alpha at 656.28 nm receding at 0.1c.
    shifted = shifted_wavelength_nm(656.28, 0.1)
    assert shifted == pytest.approx(656.28 * wavelength_ratio(0.1))
    assert shifted > 656.28


def test_superluminal_rejected():
    with pytest.raises(ValueError):
        wavelength_ratio(1.0)
