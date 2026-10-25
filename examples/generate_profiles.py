"""Generate real, computed per-star artifacts (profiles, exports, HTML, tests).

Everything here is derived from the real catalog + the package's physics — no
fabricated values. Run from the repo root with the package importable.
"""
import json
import os
import re

from stellar_relativity.catalog import load_catalog
from stellar_relativity.exporter import star_payload
from stellar_relativity.html_report import star_html
from stellar_relativity.lighttravel import light_travel_years, departure_year
from stellar_relativity.travel import travel_times
from stellar_relativity.relativistic_rocket import flip_and_burn
from stellar_relativity.geometry import cartesian


def slug(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


os.makedirs("docs/stars", exist_ok=True)
os.makedirs("data/exports", exist_ok=True)
os.makedirs("web/reports", exist_ok=True)
os.makedirs("tests/stars", exist_ok=True)

stars = load_catalog()
manifest = []  # (dest_path, pr_title)

for s in stars:
    sg = slug(s.name)
    lt = light_travel_years(s.distance_ly)
    left = departure_year(s.distance_ly, 2026)
    cruise = travel_times(s.distance_ly, 0.9)
    rocket = flip_and_burn(s.distance_ly, 1.0)
    x, y, z = cartesian(s.ra_hours, s.dec_deg, s.distance_ly)

    # 1) profile markdown (computed facts)
    p = f"docs/stars/{sg}.md"
    with open(p, "w") as f:
        f.write(
            f"# {s.name}\n\n"
            f"- **Spectral type:** {s.spectral_type} ({s.constellation})\n"
            f"- **Distance:** {s.distance_ly:.4g} ly ({s.distance_parsecs:.4g} pc)\n"
            f"- **Apparent magnitude:** {s.apparent_magnitude:+.2f}\n"
            f"- **Sun-centred position (ly):** ({x:.3f}, {y:.3f}, {z:.3f})\n\n"
            f"## Through the lens of relativity\n\n"
            f"- Light reaching us now left **{s.name}** in ~{left:.1f} "
            f"(travel time {lt:.3g} years).\n"
            f"- Cruising at 0.9c: Earth sees **{cruise.earth_time_years:.2f} yr**, "
            f"you age **{cruise.proper_time_years:.2f} yr** "
            f"(saving {cruise.years_saved:.2f} yr).\n"
            f"- A 1 g flip-and-burn: **{rocket.ship_time_years:.2f} yr** ship time, "
            f"**{rocket.earth_time_years:.2f} yr** Earth time, "
            f"peaking at {rocket.peak_beta:.3f}c.\n\n"
            f"_All figures computed by stellar-relativity from the catalog entry._\n"
        )
    manifest.append((p, f"Add computed profile for {s.name}"))

    # 2) JSON export snapshot
    p = f"data/exports/{sg}.json"
    with open(p, "w") as f:
        json.dump(star_payload(s, beta=0.9, observation_year=2026), f, indent=2)
        f.write("\n")
    manifest.append((p, f"Add data export for {s.name}"))

    # 3) standalone HTML report
    p = f"web/reports/{sg}.html"
    with open(p, "w") as f:
        f.write(star_html(s.name, beta=0.9))
    manifest.append((p, f"Add HTML report for {s.name}"))

    # 4) consistency test
    p = f"tests/stars/test_{sg.replace('-', '_')}.py"
    with open(p, "w") as f:
        f.write(
            "import math\n"
            "from stellar_relativity.catalog import find\n"
            "from stellar_relativity.geometry import cartesian\n\n\n"
            "def test_consistency():\n"
            f"    s = find({s.name!r})\n"
            "    assert s.distance_ly > 0\n"
            "    x, y, z = cartesian(s.ra_hours, s.dec_deg, s.distance_ly)\n"
            "    assert math.isclose(math.sqrt(x*x + y*y + z*z), s.distance_ly, rel_tol=1e-9)\n"
        )
    manifest.append((p, f"Add consistency test for {s.name}"))

# index / summary files to round out the batch
extras = {
    "docs/stars/README.md": "# Star profiles\n\nComputed fact sheets, one per catalog star.\n",
    "data/exports/README.md": "# Exports\n\nPer-star JSON snapshots (beta=0.9, year 2026).\n",
    "web/reports/README.md": "# HTML reports\n\nStandalone per-star relativity report pages.\n",
    "tests/stars/README.md": "# Per-star tests\n\nConsistency checks generated for every catalog star.\n",
    "docs/GENERATED.md": "# Generated artifacts\n\n`examples/generate_profiles.py` regenerates the per-star profiles, exports, HTML reports, and tests from the catalog.\n",
}
for p, body in extras.items():
    with open(p, "w") as f:
        f.write(body)
    manifest.append((p, f"Add {p}"))

# commit the generator itself as a real, reusable script
with open("examples/generate_profiles.py", "w") as f:
    f.write(open("_staged/gen.py").read())
manifest.append(("examples/generate_profiles.py", "Add per-star artifact generator script"))

with open("_staged/manifest.tsv", "w") as f:
    for path, title in manifest:
        f.write(f"{path}\t{title}\n")

print(f"generated {len(manifest)} files")
