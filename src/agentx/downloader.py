"""Download and manage the native agentx binary."""

import os
import platform
import stat
import sys
import urllib.request
from pathlib import Path

GITHUB_REPO = "kugesan/agentx-foo"
BINARY_NAME = "agentx"


def get_cache_dir() -> Path:
    """Get the cache directory for storing the binary."""
    if sys.platform == "win32":
        base = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local"))
    else:
        base = Path(os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache"))
    return base / "agentx" / "bin"


def get_platform_info() -> tuple[str, str]:
    """Detect current platform and architecture."""
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Normalize platform
    if system == "darwin":
        plat = "macos"
    elif system == "windows":
        plat = "windows"
    else:
        plat = "linux"

    # Normalize architecture
    if machine in ("x86_64", "amd64"):
        arch = "x86_64"
    elif machine in ("arm64", "aarch64"):
        arch = "arm64"
    else:
        arch = machine

    return plat, arch


def get_binary_name(plat: str, arch: str) -> str:
    """Get the binary filename for this platform."""
    name = f"agentx-{plat}-{arch}"
    if plat == "windows":
        name += ".exe"
    return name


def get_binary_path() -> Path:
    """Get the path where the binary should be stored."""
    plat, arch = get_platform_info()
    cache_dir = get_cache_dir()
    binary_name = BINARY_NAME
    if plat == "windows":
        binary_name += ".exe"
    return cache_dir / binary_name


def get_latest_release_url() -> str:
    """Get the download URL for the latest release binary."""
    plat, arch = get_platform_info()
    binary_name = get_binary_name(plat, arch)
    return f"https://github.com/{GITHUB_REPO}/releases/latest/download/{binary_name}"


def download_binary(url: str, dest: Path) -> None:
    """Download the binary from the given URL."""
    dest.parent.mkdir(parents=True, exist_ok=True)

    print(f"Downloading agentx binary from {url}...")
    try:
        urllib.request.urlretrieve(url, dest)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            plat, arch = get_platform_info()
            print(f"Error: No binary available for {plat}-{arch}")
            print(f"Check releases at: https://github.com/{GITHUB_REPO}/releases")
            sys.exit(1)
        raise

    # Make executable on Unix
    if sys.platform != "win32":
        dest.chmod(dest.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

    print(f"Binary installed to: {dest}")


def ensure_binary() -> Path:
    """Ensure the binary is downloaded and return its path."""
    binary_path = get_binary_path()

    if not binary_path.exists():
        url = get_latest_release_url()
        download_binary(url, binary_path)

    return binary_path
