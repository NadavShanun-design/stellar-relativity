# 🌌 stellar-relativity

**How the nearest star systems relate to Earth through the lens of special relativity.**

Light you see from another star left it years ago. If you tried to *travel* there,
time would pass differently for you than for everyone you left behind. This project
turns the real catalog of our stellar neighbourhood into concrete, computed answers:

- ⏳ **Light-travel time** — the image of Proxima Centauri in your telescope tonight
  left it **4.2 years ago**. What year did the light leave each star?
- 🚀 **Relativistic travel time** — fly to a star at 90% of light speed and the
  galaxy ages differently than your wristwatch. How much younger do *you* arrive?
- 🌈 **Relativistic Doppler shift** — how much a star's light would blue/red-shift
  at a given velocity.
- 📐 **3D geometry** — real positions (RA/Dec/distance) projected into a cartesian
  map centred on the Sun.

Everything is computed from first principles (special relativity) over a catalog of
real nearby stars. No magic numbers in the physics — only the published astronomical
measurements in [`data/stars.json`](data/stars.json).

## Quick start

```bash
pip install -e .
stellar-relativity report "Proxima Centauri" --speed 0.9
stellar-relativity table
```

## Why

Relativity is usually taught with abstract spaceships. This makes it *tangible*: the
stars are real, the distances are measured, and the numbers are the ones you'd actually
experience. It's a small engine for building intuition about how space and time knit
together at the scale of our cosmic backyard.

## Status

Built incrementally, one feature per pull request — see the
[closed PRs](https://github.com/NadavShanun-design/stellar-relativity/pulls?q=is%3Apr+is%3Amerged).

## License

MIT — see [LICENSE](LICENSE).
