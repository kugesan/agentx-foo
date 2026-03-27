"""Main entry point for the compiled AgentX binary."""

import sys


def main() -> int:
    """Launch the AgentX application."""
    from agentx.app import main as run_app
    run_app()
    return 0


if __name__ == "__main__":
    sys.exit(main())
