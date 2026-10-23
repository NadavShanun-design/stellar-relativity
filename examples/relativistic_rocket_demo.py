"""Compare the constant-velocity cruise with a realistic 1 g flip-and-burn.

Run with:  python examples/relativistic_rocket_demo.py
"""

from stellar_relativity.catalog import load_catalog
from stellar_relativity.relativistic_rocket import flip_and_burn


def main() -> None:
    print("Flip-and-burn trips at a constant, comfortable 1 g:\n")
    print(f"{'Star':22}{'Dist(ly)':>10}{'Ship(yr)':>10}{'Earth(yr)':>11}{'PeakSpeed':>11}")
    print("-" * 64)
    for star in load_catalog():
        t = flip_and_burn(star.distance_ly, g_force=1.0)
        print(
            f"{star.name:22}{star.distance_ly:>10.2f}{t.ship_time_years:>10.2f}"
            f"{t.earth_time_years:>11.2f}{t.peak_beta:>10.3f}c"
        )
    print("\nAt 1 g you could cross our entire stellar neighbourhood within a")
    print("human lifetime of *ship* time — while centuries pass back on Earth.")


if __name__ == "__main__":
    main()
