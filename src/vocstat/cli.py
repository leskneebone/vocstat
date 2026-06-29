from __future__ import annotations

import argparse
import json
from pathlib import Path

from rdflib import Graph

from vocstat.stats import skos_statistics


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="vocstat")
    subparsers = parser.add_subparsers(dest="command", required=True)

    stats = subparsers.add_parser("stats", help="Generate SKOS vocabulary statistics")
    stats.add_argument("path", type=Path, help="RDF file to analyse")
    stats.add_argument(
        "--format",
        default=None,
        help="RDF parser format. Defaults to rdflib format guessing.",
    )
    stats.add_argument(
        "--indent",
        type=int,
        default=2,
        help="JSON indentation level.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "stats":
        graph = Graph()
        graph.parse(args.path, format=args.format)
        print(json.dumps(skos_statistics(graph), indent=args.indent, sort_keys=True))


if __name__ == "__main__":
    main()

