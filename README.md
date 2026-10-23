# 🌌 stellar-relativity

**How the nearest star systems relate to Earth through the lens of special relativity.**

Light you see from another star left it years ago. If you tried to *travel* there,
time would pass differently for you than for everyone you left behind. This project
turns the real catalog of our stellar neighbourhood into concrete, computed answers.

## What it computes

- ⏳ **Light-travel time** — the image of Proxima Centauri in your telescope tonight
  left it **4.2 years ago**. What year did the light leave each star?
- 🚀 **Relativistic travel time** — cruise at a fixed fraction of *c*, or do a
  realistic **1 g flip-and-burn** with acceleration and deceleration, and see how
  much younger *you* arrive.
- 🌈 **Relativistic Doppler shift** — how a star's light blue/red-shifts at speed.
- ✴️ **Aberration of starlight** — how the sky bunches toward your heading as you fly.
- ⚡ **Energy cost** — the kinetic-energy price (in units of the ship's own mass) of
  reaching a given speed, and the perfect-fuel floor to pay for it.
- 📐 **3D geometry** — real positions (RA/Dec/distance) projected into a Sun-centred
  cartesian map, plus true and angular separations.

Everything is computed from first principles. No magic numbers in the physics — only
the published astronomical measurements in [`data/stars.json`](data/stars.json).

## Quick start

```bash
pip install -e .
stellar-relativity report "Proxima Centauri" --speed 0.9
stellar-relativity rocket "Sirius A" --g 1.0
stellar-relativity table
stellar-relativity map
```

See [`docs/USAGE.md`](docs/USAGE.md) for the full API and [`docs/PHYSICS.md`](docs/PHYSICS.md)
for the equations behind every module.

## Why

Relativity is usually taught with abstract spaceships. This makes it *tangible*: the
stars are real, the distances are measured, and the numbers are the ones you'd actually
experience travelling our cosmic backyard.

## Install options

```bash
make install && make test      # local dev
docker build -t stellar-relativity . && docker run --rm stellar-relativity
```

## Status

Built incrementally, one feature per pull request — see the
[merged PRs](https://github.com/NadavShanun-design/stellar-relativity/pulls?q=is%3Apr+is%3Amerged).

## License

MIT — see [LICENSE](LICENSE).
