#!/bin/bash

set -e

echo "File IO Setup is running..."

# Determine the directory of this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Move up two levels to get the project root
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Define the CSV output path
CSV_OUTPUT="$PROJECT_ROOT/CSVOutput"

# Create the directory if it doesn't exist
mkdir -p "$CSV_OUTPUT"

echo "CSV output folder created: $CSV_OUTPUT"
