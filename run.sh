#!/bin/bash

set -e

# Get the path of this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Determine the project root (two levels up)
PROJECT_ROOT="$(cd "$SCRIPT_DIR" && pwd)"

# Path to virtual environment
VENV_DIR="$PROJECT_ROOT/.venv"

# Path to brain folder
BRAIN_FOLDER="$PROJECT_ROOT/Codebase/DataCollection/Brain"
SOIL_MANAGER="$BRAIN_FOLDER/soil_manager.py"

# Activate virtual environment
source "$VENV_DIR/bin/activate"

# Run the script with the virtual environment's Python
python "$SOIL_MANAGER"
