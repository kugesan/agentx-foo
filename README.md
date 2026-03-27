# agentx-foo

Native compiled Python agent framework using Nuitka.

## Installation

### From PyPI (source distribution)
```bash
pip install agentx-foo
```

### Pre-built Binaries
Download native binaries from [Releases](https://github.com/kugesan/agentx-foo/releases):

- `agentx-linux-x86_64` - Linux (x64)
- `agentx-macos-x86_64` - macOS Intel
- `agentx-macos-arm64` - macOS Apple Silicon
- `agentx-windows-x86_64.exe` - Windows

## Usage

```bash
agentx --version
agentx run
```

## Development

### Build from source
```bash
pip install -e ".[dev]"
```

### Build native binary locally
```bash
./scripts/build_nuitka.sh
```

## Release Process

1. Update version in `src/agentx/__init__.py` and `pyproject.toml`
2. Create and push a tag:
   ```bash
   git tag v0.1.0
   git push origin v0.1.0
   ```
3. GitHub Actions will:
   - Build Nuitka binaries for Linux, macOS, Windows
   - Create a GitHub Release with binaries
   - Publish source distribution to PyPI

## License

MIT
