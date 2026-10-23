# The physics behind stellar-relativity

Everything here is **special** relativity (flat spacetime, no gravity). The
formulas are implemented in the modules named in parentheses.

## 1. Light-travel time (`lighttravel.py`)

A light year is *defined* as the distance light covers in one Julian year, so the
time (in years) for light to reach us from a star is numerically equal to its
distance in light years:

```
t_light = d           (d in light years -> t in years)
```

The light you see tonight therefore left the star `t_light` years ago:

```
departure_year = observation_year - d
```

## 2. The Lorentz factor (`lorentz.py`)

For a traveller moving at speed `v`, let `β = v/c`. The Lorentz factor is

```
γ = 1 / sqrt(1 - β²),   0 ≤ β < 1
```

γ is 1 at rest and diverges as β → 1. A massive traveller can never reach β = 1,
which is why the code rejects β ≥ 1.

## 3. Travel time and time dilation (`travel.py`)

Cruising at constant `β` over a distance `d` (light years):

```
t_earth  = d / β               # years elapsed for people on Earth
t_onboard = t_earth / γ         # years elapsed on the traveller's clock
```

Because γ ≥ 1, the traveller always ages **less** than Earth. That difference,
`t_earth − t_onboard`, is the "years saved" — the twin-paradox gap.

> This is the constant-velocity idealisation: it ignores the acceleration and
> deceleration a real ship needs. It isolates the dilation effect, which is the
> point of the tool.

## 4. Relativistic Doppler shift (`doppler.py`)

For motion directly along the line of sight,

```
λ_observed / λ_emitted = sqrt((1 + β) / (1 - β))
```

with the convention that β > 0 is recession (redshift) and β < 0 is approach
(blueshift). The redshift is `z = λ_observed/λ_emitted − 1`.

## 5. 3D positions (`geometry.py`)

Catalog positions are right ascension (hours), declination (degrees) and
distance. Converting to cartesian light-year coordinates with the Sun at the
origin:

```
x = d · cos(dec) · cos(ra)
y = d · cos(dec) · sin(ra)
z = d · sin(dec)
```

where `ra = ra_hours · 15°` and `dec = dec_deg`. From these we get true 3D
separations between stars and great-circle angular separations on the sky.
