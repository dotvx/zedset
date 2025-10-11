#!/bin/bash
# Align CSV/TSV/PSV columns as markdown table (auto-detects delimiter: , | ;)

DEBUG_FILE="/tmp/align-csv-debug.log"
exec 2>>"$DEBUG_FILE"

echo "=== DEBUG LOG $(date) ===" >&2
echo "ZED_SELECTED_TEXT length: ${#ZED_SELECTED_TEXT}" >&2
echo "First 200 chars of input: ${ZED_SELECTED_TEXT:0:200}" >&2

# Use Python to auto-detect delimiter and create markdown table
printf '%s' "$ZED_SELECTED_TEXT" | python3 << 'PYTHON_EOF' | tee -a "$DEBUG_FILE" | curl -X POST --data-binary @- http://localhost:8888/paste -s
import csv
import sys
from io import StringIO

# Read input from stdin
input_data = sys.stdin.read()
print(f"DEBUG: Read {len(input_data)} chars from stdin", file=sys.stderr)

if not input_data.strip():
    print("DEBUG: No data to process", file=sys.stderr)
    sys.exit(0)

# Auto-detect delimiter by counting occurrences in first line
first_line = input_data.split('\n')[0]
delimiters = {
    ',': first_line.count(','),
    '|': first_line.count('|'),
    ';': first_line.count(';'),
    '\t': first_line.count('\t')
}

# Choose delimiter with highest count
delimiter = max(delimiters, key=delimiters.get)
if delimiters[delimiter] == 0:
    delimiter = ','  # Default fallback

print(f"DEBUG: Auto-detected delimiter: {repr(delimiter)}", file=sys.stderr)

# Parse CSV with detected delimiter
reader = csv.reader(StringIO(input_data), delimiter=delimiter)
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
            col_widths[i] = max(col_widths[i], len(cell.strip()))

print(f"DEBUG: Column widths: {col_widths}", file=sys.stderr)

# Print markdown table
for idx, row in enumerate(rows):
    aligned_row = []
    for i, cell in enumerate(row):
        if i < len(col_widths):
            aligned_row.append(' ' + cell.strip().ljust(col_widths[i]) + ' ')
        else:
            aligned_row.append(' ' + cell.strip() + ' ')
    print('|' + '|'.join(aligned_row) + '|')

    # Add separator after first row (header)
    if idx == 0:
        separators = []
        for width in col_widths:
            separators.append(' ' + '-' * width + ' ')
        print('|' + '|'.join(separators) + '|')
PYTHON_EOF

echo "Script completed" >&2
