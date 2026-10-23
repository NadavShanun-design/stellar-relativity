"""Command-line interface for stellar-relativity.

    stellar-relativity list
    stellar-relativity report "Proxima Centauri" --speed 0.9
    stellar-relativity table --speed 0.5
    stellar-relativity export --speed 0.9 > catalog.json
"""

from __future__ import annotations

import argparse
import sys

from .catalog import load_catalog
from .compare import comparison_table
from .exporter import export_json
from .report import DEFAULT_OBSERVATION_YEAR, report


def _add_speed(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--speed",
        type=float,
        default=0.9,
        metavar="BETA",
        help="cruise speed as a fraction of light speed (0 < beta < 1); default 0.9",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="stellar-relativity",
        description="How the nearest stars relate to Earth through special relativity.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("list", help="list every star in the catalog")

    p_report = sub.add_parser("report", help="full relativity report for one star")
    p_report.add_argument("star", help="star name, e.g. 'Proxima Centauri'")
    _add_speed(p_report)
    p_report.add_argument(
        "--year", type=int, default=DEFAULT_OBSERVATION_YEAR,
        help=f"observation year (default {DEFAULT_OBSERVATION_YEAR})",
    )

    p_table = sub.add_parser("table", help="comparison table across all stars")
    _add_speed(p_table)

    p_export = sub.add_parser("export", help="emit the full catalog as JSON")
    _add_speed(p_export)

    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)

    if args.command == "list":
        for star in load_catalog():
            print(f"{star.name:22} {star.distance_ly:>8.3f} ly  {star.spectral_type}")
        return 0

    if args.command == "report":
        try:
            print(report(args.star, beta=args.speed, observation_year=args.year))
        except KeyError as exc:
            print(str(exc), file=sys.stderr)
            return 1
        except ValueError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2
        return 0

    if args.command == "table":
        print(comparison_table(beta=args.speed))
        return 0

    if args.command == "export":
        print(export_json(beta=args.speed))
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
