"""A tiny tour of the stellar_relativity package.

Run with:  python examples/demo.py
"""

from stellar_relativity.catalog import load_catalog
from stellar_relativity.report import report
from stellar_relativity.compare import comparison_table


def main() -> None:
    print("Nearest stars on file:")
    for star in load_catalog()[:5]:
        print(f"  - {star.name} ({star.distance_ly} ly)")
    print()

    print(report("Proxima Centauri", beta=0.9))
    print()
    print(report("Sirius A", beta=0.5))
    print()
    print(comparison_table(beta=0.5))


if __name__ == "__main__":
    main()
