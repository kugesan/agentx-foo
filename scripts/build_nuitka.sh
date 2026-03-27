#!/bin/bash
# Build native binary with Nuitka
# Usage: ./scripts/build_nuitka.sh

set -e

echo "Installing Nuitka..."
pip install nuitka ordered-set zstandard

echo "Building native binary..."
python -m nuitka \
    --standalone \
    --onefile \
    --assume-yes-for-download \
    --enable-plugin=tk-inter \
    --include-package=agentx_core \
    --output-filename=agentx \
    --output-dir=dist \
    src/agentx_core/main.py

echo "Build complete!"
echo "Binary located at: dist/agentx"
ls -lh dist/agentx
