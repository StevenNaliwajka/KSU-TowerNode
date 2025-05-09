#!/bin/bash

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR" && pwd)"
VENV_DIR="$PROJECT_ROOT/.venv"
BRAIN_FOLDER="$PROJECT_ROOT/Codebase/DataCollection/Brain"
SOIL_MANAGER="$BRAIN_FOLDER/soil_manager.py"
PID_FILE="$PROJECT_ROOT/.soil_manager.pid"

source "$VENV_DIR/bin/activate"

# Start the Python script in the background
python "$SOIL_MANAGER" &
echo $! > "$PID_FILE"
