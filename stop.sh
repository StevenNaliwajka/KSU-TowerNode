#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR" && pwd)"
PID_FILE="$PROJECT_ROOT/.soil_manager.pid"

if [[ -f "$PID_FILE" ]]; then
    PID=$(cat "$PID_FILE")
    if kill -0 "$PID" > /dev/null 2>&1; then
        echo "Stopping soil_manager (PID $PID)..."
        kill "$PID"
        rm "$PID_FILE"
    else
        echo "No process found with PID $PID. Cleaning up PID file."
        rm "$PID_FILE"
    fi
else
    echo "No PID file found. Is soil_manager running?"
fi
