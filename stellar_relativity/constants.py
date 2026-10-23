"""Physical and astronomical constants used throughout the package.

Values are the exact defined / CODATA / IAU figures so every downstream
calculation is traceable to a known source rather than a magic number.
"""

# Speed of light in vacuum — exact by definition (SI).
C_M_PER_S = 299_792_458.0

# A Julian year is exactly 365.25 days of 86400 SI seconds.
SECONDS_PER_YEAR = 365.25 * 86_400.0  # 31_557_600.0

# A light year is the distance light travels in one Julian year — exact.
LIGHT_YEAR_M = C_M_PER_S * SECONDS_PER_YEAR  # 9.4607304725808e15 m

# IAU 2012 definition of the parsec.
PARSEC_M = 3.0856775814913673e16
PARSEC_IN_LY = PARSEC_M / LIGHT_YEAR_M  # ~3.2615638

# IAU 2012 definition of the astronomical unit (exact).
AU_M = 1.495978707e11

# Newtonian gravitational constant (CODATA 2018).
G = 6.674_30e-11

__all__ = [
    "C_M_PER_S",
    "SECONDS_PER_YEAR",
    "LIGHT_YEAR_M",
    "PARSEC_M",
    "PARSEC_IN_LY",
    "AU_M",
    "G",
]
