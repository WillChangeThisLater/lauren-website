#!/bin/bash

set -euo pipefail

cd ..
uv run python -m http.server --bind 0.0.0.0 7777
