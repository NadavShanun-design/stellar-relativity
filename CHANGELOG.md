# Changelog

All notable changes to this project are documented here. The project was built
incrementally, one feature per pull request.

## [0.1.0]

### Added
- Nearby-star catalog (`data/stars.json`) with real published positions and distances.
- Physical constants module (`constants.py`).
- Catalog loader with case-insensitive lookup (`catalog.py`).
- Light-travel-time calculations (`lighttravel.py`).
- Lorentz factor and rapidity (`lorentz.py`).
- Relativistic travel times with time dilation (`travel.py`).
- Relativistic Doppler shift (`doppler.py`).
- 3D cartesian geometry and angular/true separations (`geometry.py`).
- Per-star relativity report (`report.py`).
- All-star comparison table (`compare.py`).
- JSON export of the full catalog (`exporter.py`).
- Command-line interface (`cli.py`).
- Test suite covering every physics module.
- Interactive web visualisation (`web/`).
- Continuous integration across Python 3.9–3.12.
- Physics documentation (`docs/PHYSICS.md`) and a runnable demo (`examples/demo.py`).
