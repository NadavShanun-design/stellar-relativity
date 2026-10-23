"""The energy price of relativistic travel.

Reaching speed beta costs kinetic energy KE = (gamma - 1) * m * c**2. Expressed
as a multiple of the ship's own rest energy, that is simply (gamma - 1) — which
is why relativistic travel is so staggeringly expensive.
"""

from __future__ import annotations

from .constants import C_M_PER_S
from .lorentz import lorentz_factor


def rest_energy_joules(mass_kg: float) -> float:
    """E = m c**2."""
    if mass_kg < 0:
        raise ValueError("mass_kg must be non-negative")
    return mass_kg * C_M_PER_S * C_M_PER_S


def kinetic_energy_in_mc2(beta: float) -> float:
    """Kinetic energy to reach ``beta``, in units of the rest energy m*c**2."""
    return lorentz_factor(beta) - 1.0


def kinetic_energy_joules(mass_kg: float, beta: float) -> float:
    """Kinetic energy (joules) to accelerate ``mass_kg`` to speed ``beta``."""
    if mass_kg < 0:
        raise ValueError("mass_kg must be non-negative")
    return kinetic_energy_in_mc2(beta) * rest_energy_joules(mass_kg)


def antimatter_fuel_kg(mass_kg: float, beta: float) -> float:
    """Mass of perfect (100%-efficient) matter-antimatter fuel to supply the KE.

    This is a thermodynamic floor: fuel_mass = KE / c**2 = (gamma - 1) * mass.
    A real rocket needs far more because it must also accelerate its own fuel.
    """
    return kinetic_energy_in_mc2(beta) * mass_kg


__all__ = [
    "rest_energy_joules",
    "kinetic_energy_in_mc2",
    "kinetic_energy_joules",
    "antimatter_fuel_kg",
]
