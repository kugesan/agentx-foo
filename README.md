# agentx-foo

Native compiled Python agent framework using Nuitka.

## Installation

```bash
pip install agentx-foo
```

On first run, the native binary is automatically downloaded from GitHub Releases.

## Usage

```bash
agentx --version      # Downloads binary on first run, then executes
agentx run            # Run command
agentx --upgrade      # Force download latest binary
agentx --stub-version # Show pip package version
```

## Pre-built Binaries

You can also download binaries directly from [Releases](https://github.com/kugesan/agentx-foo/releases):

- `agentx-linux-x86_64` - Linux (x64)
- `agentx-macos-x86_64` - macOS Intel
- `agentx-macos-arm64` - macOS Apple Silicon
- `agentx-windows-x86_64.exe` - Windows

## How it Works

The PyPI package is a thin stub that:
1. Detects your OS and architecture
2. Downloads the correct native binary from GitHub Releases
3. Executes the binary with your arguments

Your actual code runs as a compiled native binary - no Python source exposed.

## Development

### Build native binary locally
```bash
pip install nuitka ordered-set zstandard
./scripts/build_nuitka.sh
```

## Release Process

1. Update version in `src/agentx/__init__.py` and `pyproject.toml`
2. Create and push a tag:
   ```bash
   git tag v0.2.0
   git push origin v0.2.0
   ```
3. GitHub Actions will:
   - Build Nuitka binaries for Linux, macOS, Windows
   - Create a GitHub Release with binaries
   - Publish stub package to PyPI

## License

MIT
