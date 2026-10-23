"""Enable ``python -m stellar_relativity ...`` as an alias for the CLI."""

from .cli import main

if __name__ == "__main__":
    raise SystemExit(main())
