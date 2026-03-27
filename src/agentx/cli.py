"""CLI entry point for AgentX."""

import argparse
import sys

from agentx import __version__


def main() -> int:
    """Main entry point for the AgentX CLI."""
    parser = argparse.ArgumentParser(
        prog="agentx",
        description="AgentX - Native compiled Python agent framework",
    )
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"agentx {__version__}",
    )
    parser.add_argument(
        "command",
        nargs="?",
        default="run",
        help="Command to execute (default: run)",
    )

    args = parser.parse_args()

    print(f"AgentX v{__version__}")
    print(f"Running command: {args.command}")

    # Add your core logic here

    return 0


if __name__ == "__main__":
    sys.exit(main())
