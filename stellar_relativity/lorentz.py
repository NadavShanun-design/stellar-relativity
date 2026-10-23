"""The Lorentz factor — the heart of special-relativistic kinematics."""

from __future__ import annotations

import math


def validate_beta(beta: float) -> float:
    """Return ``beta`` (v/c) after checking it is physically travellable.

    ``beta`` must satisfy 0 <= beta < 1. A value of exactly 1 (light speed)
    or above is rejected because a massive traveller can never reach it.
    """
    if beta < 0:
        raise ValueError(f"beta must be non-negative, got {beta}")
    if beta >= 1:
        raise ValueError(f"beta must be < 1 (slower than light), got {beta}")
    return beta


def lorentz_factor(beta: float) -> float:
    """Return the Lorentz factor gamma = 1 / sqrt(1 - beta**2)."""
    b = validate_beta(beta)
    return 1.0 / math.sqrt(1.0 - b * b)


def rapidity(beta: float) -> float:
    """Return the rapidity (arctanh of beta) — the additive velocity measure."""
    return math.atanh(validate_beta(beta))


__all__ = ["validate_beta", "lorentz_factor", "rapidity"]
