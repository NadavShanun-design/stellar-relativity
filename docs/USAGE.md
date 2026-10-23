# Usage

Install in a virtual environment:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .
```

## Command line

```bash
stellar-relativity list                                 # every star, by distance
stellar-relativity report "Proxima Centauri" --speed 0.9
stellar-relativity table --speed 0.5                    # compare all stars
stellar-relativity rocket "Sirius A" --g 1.0            # 1 g flip-and-burn trip
stellar-relativity map                                  # ASCII sky map
stellar-relativity export --speed 0.9 > catalog.json    # machine-readable
```

## Python API

```python
from stellar_relativity.catalog import find
from stellar_relativity.travel import travel_times
from stellar_relativity.relativistic_rocket import flip_and_burn
from stellar_relativity.energy import kinetic_energy_in_mc2

star = find("Tau Ceti")

cruise = travel_times(star.distance_ly, 0.9)     # constant velocity
print(cruise.proper_time_years, "yr onboard")

rocket = flip_and_burn(star.distance_ly, 1.0)    # realistic 1 g accel
print(rocket.ship_time_years, "yr ship,", rocket.earth_time_years, "yr Earth")

print(kinetic_energy_in_mc2(0.9), "x the ship's rest energy to reach 0.9c")
```

See [`docs/PHYSICS.md`](PHYSICS.md) for the equations behind each module.
