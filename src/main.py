import argparse
from pathlib import Path
import tomllib
from typing import Any, Dict
from pprint import pprint
from etf_scraper import ETFScraper  # type: ignore[attr-defined]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="icicle plot generator for hierarchical data"
    )
    parser.add_argument(
        "--input",
        type=lambda s: Path(s).resolve(strict=True),
        required=True,
        help="Path to the input TOML for the icicle plot",
    )
    parser.add_argument(
        "--output",
        type=lambda p: Path(p).resolve(),
        required=True,
        help="Path to save the output icicle plot",
    )
    return parser.parse_args()


def ingest_input(input_path: Path) -> Dict[str, Any]:
    """Load the input TOML file."""
    with input_path.open("rb") as f:
        d = tomllib.load(f)
        pprint(f"Loaded input from {input_path}:")
        pprint(d)
        return d


def main() -> None:
    args = parse_args()

    d: Dict[str, Any] = ingest_input(args.input)
    if not isinstance(d, dict):
        raise ValueError(f"Expected a dictionary from {args.input}, got {type(d)}")

    etf = ETFScraper()
    ivv = etf.query_holdings(ticker="IVV", holdings_date=None)
    pprint(ivv)

    _output_path: Path = args.output
    print("Hello from icicle-plot!")


if __name__ == "__main__":
    main()
