import argparse

from app.application import commands

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog = "document-ai",
        description = "Document AI CLI"
    )

    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("run")
    subparsers.add_parser("version")
    subparsers.add_parser("doctor")

    return parser

def run() -> None:
    parser = create_parser()
    args = parser.parse_args()

    if args.command in (None, "run"):
        commands.run()
    elif args.command == "version":
        commands.version()
    elif args.command == "doctor":
        commands.doctor()