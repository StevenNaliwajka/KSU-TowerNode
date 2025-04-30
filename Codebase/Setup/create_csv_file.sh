#!/bin/bash

set -euo pipefail

# Input arguments
COLLECTION_TYPE="$1"
NUMBER="$2"

# Get current date and time
DATE=$(date +"%Y-%m-%d")
TIME=$(date +"%H-%M-%S")

# Determine project root (assume script is in /Codebase/Setup)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Set output folder and filename
CSV_OUTPUT_FOLDER="$PROJECT_ROOT/CSVOutput"
FILENAME="${COLLECTION_TYPE}_instance${NUMBER}_${DATE}_${TIME}.csv"
FILE_PATH="$CSV_OUTPUT_FOLDER/$FILENAME"

# Ensure output folder exists
mkdir -p "$CSV_OUTPUT_FOLDER"

# Create the CSV file
touch "$FILE_PATH"

echo "CSV created at: $FILE_PATH"
