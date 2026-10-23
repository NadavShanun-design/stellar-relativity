"""Relativistic Doppler shift for light along the line of sight.

Sign convention: positive ``beta`` means the source and observer are
*receding* (moving apart) -> redshift. Negative ``beta`` means approaching
-> blueshift.
"""

from __future__ import annotations

import math


def _check(beta: float) -> float:
    if not -1 < beta < 1:
        raise ValueError(f"beta must satisfy -1 < beta < 1, got {beta}")
    return beta


def wavelength_ratio(beta: float) -> float:
    """Observed / emitted wavelength ratio for purely radial motion.

    ratio = sqrt((1 + beta) / (1 - beta)); >1 for recession (redshift).
    """
    b = _check(beta)
    return math.sqrt((1.0 + b) / (1.0 - b))


def redshift_z(beta: float) -> float:
    """Dimensionless redshift z = (lambda_obs - lambda_emit) / lambda_emit."""
    return wavelength_ratio(beta) - 1.0


def frequency_ratio(beta: float) -> float:
    """Observed / emitted frequency ratio (inverse of the wavelength ratio)."""
    return 1.0 / wavelength_ratio(beta)


def shifted_wavelength_nm(rest_wavelength_nm: float, beta: float) -> float:
    """Shift a spectral line (given in nanometres) by the Doppler factor."""
    if rest_wavelength_nm <= 0:
        raise ValueError("rest_wavelength_nm must be positive")
    return rest_wavelength_nm * wavelength_ratio(beta)


__all__ = [
    "wavelength_ratio",
    "redshift_z",
    "frequency_ratio",
    "shifted_wavelength_nm",
]
