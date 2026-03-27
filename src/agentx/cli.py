"""CLI entry point - downloads and runs the native binary."""

import subprocess
import sys

from agentx import __version__
from agentx.downloader import ensure_binary, get_binary_path, get_latest_release_url, download_binary


def main() -> int:
    """Download binary if needed, then execute it with all arguments."""
    # Handle stub-specific commands
    if len(sys.argv) > 1:
        if sys.argv[1] == "--upgrade":
            return upgrade_binary()
        if sys.argv[1] == "--stub-version":
            print(f"agentx-foo stub version: {__version__}")
            return 0

    try:
        binary_path = ensure_binary()
    except Exception as e:
        print(f"Error: Failed to get agentx binary: {e}", file=sys.stderr)
        return 1

    # Execute the binary with all passed arguments
    try:
        result = subprocess.run([str(binary_path)] + sys.argv[1:])
        return result.returncode
    except KeyboardInterrupt:
        return 130
    except Exception as e:
        print(f"Error executing binary: {e}", file=sys.stderr)
        return 1


def upgrade_binary() -> int:
    """Force download the latest binary."""
    print("Upgrading agentx binary...")
    binary_path = get_binary_path()

    # Remove existing binary
    if binary_path.exists():
        binary_path.unlink()
        print(f"Removed old binary: {binary_path}")

    # Download fresh
    url = get_latest_release_url()
    try:
        download_binary(url, binary_path)
        print("Upgrade complete!")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
