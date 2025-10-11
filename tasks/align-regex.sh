#!/bin/bash
# Align columns by regex pattern or specific characters

DEBUG_FILE="/tmp/align-regex-debug.log"
exec 2>>"$DEBUG_FILE"

echo "=== DEBUG LOG $(date) ===" >&2
echo "ZED_SELECTED_TEXT length: ${#ZED_SELECTED_TEXT}" >&2
echo "Args: $@" >&2

# Prompt for delimiter if not provided
if [ -z "$1" ]; then
    DELIMITER=$(osascript -e 'Tell application "System Events" to display dialog "Enter regex pattern or delimiter:" default answer "=" buttons {"Cancel", "OK"} default button "OK"' -e 'text returned of result' 2>/dev/null)
    if [ -z "$DELIMITER" ]; then
        echo "ERROR: No delimiter provided" >&2
        exit 1
    fi
else
    DELIMITER="$1"
fi

echo "Using delimiter: $DELIMITER" >&2

# Use Python for flexible regex-based alignment
printf '%s' "$ZED_SELECTED_TEXT" | python3 -c "
import sys
import re

# Read input
input_data = sys.stdin.read()
delimiter = sys.argv[1] if len(sys.argv) > 1 else ','

print(f'DEBUG: Delimiter pattern: {delimiter}', file=sys.stderr)
print(f'DEBUG: Input length: {len(input_data)}', file=sys.stderr)

lines = input_data.splitlines()
print(f'DEBUG: Number of lines: {len(lines)}', file=sys.stderr)

if not lines:
    print('DEBUG: No lines to process', file=sys.stderr)
    sys.exit(0)

# Split each line by the delimiter pattern
rows = []
for line in lines:
    # Split by delimiter but keep the delimiter
    parts = re.split(f'({delimiter})', line)
    # Group parts: text before delimiter + delimiter itself
    row = []
    i = 0
    while i < len(parts):
        if i + 1 < len(parts) and re.match(delimiter, parts[i + 1]):
            # Combine text + delimiter
            row.append(parts[i] + parts[i + 1])
            i += 2
        else:
            # Last part (no delimiter after)
            row.append(parts[i])
            i += 1
    rows.append(row)

print(f'DEBUG: Max columns: {max(len(row) for row in rows)}', file=sys.stderr)

# Calculate column widths (width of text before delimiter)
max_cols = max(len(row) for row in rows)
col_widths = [0] * max_cols

for row in rows:
    for i, cell in enumerate(row):
        if i < len(col_widths):
            # For columns with delimiter, calculate width without the delimiter
            if i < len(row) - 1:  # Not the last column
                # Extract text before delimiter
                match = re.match(f'(.*?)({delimiter})$', cell)
                if match:
                    text_width = len(match.group(1))
                else:
                    text_width = len(cell)
            else:
                text_width = len(cell)
            col_widths[i] = max(col_widths[i], text_width)

print(f'DEBUG: Column widths: {col_widths}', file=sys.stderr)

# Print aligned rows
for row in rows:
    aligned_parts = []
    for i, cell in enumerate(row):
        if i < len(row) - 1:  # Not the last column
            # Split cell into text and delimiter
            match = re.match(f'(.*?)({delimiter})$', cell)
            if match:
                text = match.group(1)
                delim = match.group(2)
                aligned_parts.append(text.ljust(col_widths[i]) + delim)
            else:
                aligned_parts.append(cell.ljust(col_widths[i]))
        else:
            # Last column - no padding needed
            aligned_parts.append(cell)
    print(''.join(aligned_parts))
" "$DELIMITER" | curl -X POST --data-binary @- http://localhost:8888/paste -s

echo "Script completed" >&2
