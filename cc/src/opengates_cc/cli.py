from __future__ import annotations

import argparse

import uvicorn


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="opengates-cc")
    subparsers = parser.add_subparsers(dest="command", required=True)

    serve = subparsers.add_parser("serve", help="Run the commercial intake app.")
    serve.add_argument("--host", default="127.0.0.1")
    serve.add_argument("--port", type=int, default=8100)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "serve":
        uvicorn.run("opengates_cc.app:app", host=args.host, port=args.port, reload=False)
        return
    raise SystemExit("unknown command")


if __name__ == "__main__":
    main()
