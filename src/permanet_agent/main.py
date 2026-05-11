from __future__ import annotations

import argparse

from permanet_agent.radio.mock_radio import MockRadio
from permanet_agent.routing.router import MeshRouter


def run_mock_message(message_text: str) -> str:
    radio = MockRadio()
    router = MeshRouter()
    incoming = radio.receive_text(message_text)
    outgoing = router.route(incoming)
    if outgoing is None:
        return ""
    radio.send(outgoing)
    return outgoing.text


def cli() -> None:
    parser = argparse.ArgumentParser(description="PermaNet Mesh Agent")
    parser.add_argument("--mock", action="store_true", help="Run a single mock radio message.")
    parser.add_argument("--message", default="@permanet help", help="Mock message text to route.")
    args = parser.parse_args()

    if args.mock:
        response = run_mock_message(args.message)
        if response:
            print(response)
        return

    raise SystemExit("Only --mock mode is implemented in v0.1 scaffold.")


if __name__ == "__main__":
    cli()
