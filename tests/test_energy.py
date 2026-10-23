import pytest

from stellar_relativity.energy import (
    antimatter_fuel_kg,
    kinetic_energy_in_mc2,
    kinetic_energy_joules,
    rest_energy_joules,
)


def test_rest_energy_of_one_kg():
    # ~8.99e16 J — the famous E = mc^2 value for 1 kg.
    assert rest_energy_joules(1.0) == pytest.approx(8.9875e16, rel=1e-3)


def test_kinetic_energy_in_mc2_near_zero_at_rest():
    assert kinetic_energy_in_mc2(0.0) == pytest.approx(0.0)


def test_kinetic_energy_at_gamma_two():
    # gamma = 2 exactly at beta = sqrt(3)/2; KE = (gamma-1) mc^2 = 1 mc^2.
    assert kinetic_energy_in_mc2(0.8660254037844386) == pytest.approx(1.0, abs=1e-6)


def test_kinetic_energy_joules_scales_with_mass():
    assert kinetic_energy_joules(2.0, 0.5) == pytest.approx(2.0 * kinetic_energy_joules(1.0, 0.5))


def test_antimatter_fuel_floor():
    # Perfect-efficiency fuel mass equals (gamma - 1) * payload mass.
    assert antimatter_fuel_kg(1000.0, 0.8660254037844386) == pytest.approx(1000.0, abs=1e-3)
