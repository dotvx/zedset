#!/bin/bash
# Align CSV columns for better readability

DEBUG_FILE="/tmp/align-csv-debug.log"
exec 2>>"$DEBUG_FILE"

echo "=== DEBUG LOG $(date) ===" >&2
echo "ZED_SELECTED_TEXT length: ${#ZED_SELECTED_TEXT}" >&2
echo "First 200 chars of input: ${ZED_SELECTED_TEXT:0:200}" >&2
echo "csvlook available: $(command -v csvlook &> /dev/null && echo yes || echo no)" >&2

# Check if csvlook is available (from csvkit)
if command -v csvlook &> /dev/null; then
    echo "Using csvlook method" >&2
    # Use csvlook for proper CSV alignment
    printf '%s' "$ZED_SELECTED_TEXT" | csvlook | tee -a "$DEBUG_FILE" | curl -X POST --data-binary @- http://localhost:8888/paste -s
else
    echo "Using Python method" >&2
    # Fallback: Use Python with csv module for proper handling
    printf '%s' "$ZED_SELECTED_TEXT" | python3 << 'PYTHON_EOF' | tee -a "$DEBUG_FILE" | curl -X POST --data-binary @- http://localhost:8888/paste -s
import csv
import sys
from io import StringIO

# Read CSV from stdin
input_data = sys.stdin.read()
print(f"DEBUG: Read {len(input_data)} chars from stdin", file=sys.stderr)
reader = csv.reader(StringIO(input_data))
rows = list(reader)
print(f"DEBUG: Parsed {len(rows)} rows", file=sys.stderr)

if not rows:
    print("DEBUG: No rows to process", file=sys.stderr)
    sys.exit(0)

# Calculate column widths
col_widths = [0] * len(rows[0])
for row in rows:
    for i, cell in enumerate(row):
        if i < len(col_widths):
            col_widths[i] = max(col_widths[i], len(cell))

print(f"DEBUG: Column widths: {col_widths}", file=sys.stderr)

# Print aligned CSV
for row in rows:
    aligned_row = []
    for i, cell in enumerate(row):
        if i < len(col_widths):
            aligned_row.append(cell.ljust(col_widths[i]))
        else:
            aligned_row.append(cell)
    print(','.join(aligned_row))
PYTHON_EOF
fi

echo "Script completed" >&2
