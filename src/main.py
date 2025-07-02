import argparse
from pathlib import Path
import tomllib


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


def main() -> None:
    args = parse_args()
    _input_data = tomllib.loads(args.input.read_text())
    _output_path: Path = args.output
    print("Hello from icicle-plot!")


if __name__ == "__main__":
    main()
