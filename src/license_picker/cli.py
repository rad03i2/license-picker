from __future__ import annotations

import argparse
import json
import sys

from .core import LICENSES, compare, get_license, recommend


def _print_license(item) -> None:
    print(f"{item.name} ({item.id})")
    print(f"  Copyleft: {item.copyleft}")
    print(f"  Patent grant: {'yes' if item.patent_grant else 'no'}")
    print(f"  Permissions: {', '.join(item.permissions)}")
    print(f"  Conditions: {', '.join(item.conditions) or 'none'}")
    print(f"  Limitations: {', '.join(item.limitations)}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="license-picker", description="Compare common open-source licenses and narrow choices by practical requirements.")
    parser.add_argument("--version", action="version", version="license-picker 1.0.0 — Radwan Abdulhadi Ahmed / @rad03i2")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list", help="List the built-in license catalog")
    show = sub.add_parser("show", help="Show one license")
    show.add_argument("license")
    cmp_parser = sub.add_parser("compare", help="Compare two or more licenses")
    cmp_parser.add_argument("licenses", nargs="+")
    pick = sub.add_parser("pick", help="Filter licenses by requirements")
    pick.add_argument("--patent-grant", action="store_true", help="Require an explicit patent grant")
    pick.add_argument("--copyleft", choices=("any", "none", "file", "library", "strong"), default="any")
    notice = pick.add_mutually_exclusive_group()
    notice.add_argument("--require-notice", action="store_true")
    notice.add_argument("--no-notice", action="store_true")
    for p in (sub.choices["list"], show, cmp_parser, pick):
        p.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "list":
            items = list(LICENSES)
        elif args.command == "show":
            items = [get_license(args.license)]
        elif args.command == "compare":
            items = compare(args.licenses)
        else:
            notice = True if args.require_notice else False if args.no_notice else None
            items = recommend(patent_grant=args.patent_grant, copyleft=args.copyleft, notice_required=notice)
        if args.json:
            print(json.dumps([x.to_dict() for x in items], ensure_ascii=False, indent=2))
        elif not items:
            print("No built-in license matches those filters.")
        else:
            for index, item in enumerate(items):
                if index:
                    print()
                _print_license(item)
        return 0
    except (ValueError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
