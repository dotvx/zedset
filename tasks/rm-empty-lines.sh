#!/bin/bash
# Remove or limit consecutive empty lines from ZED_SELECTED_TEXT

# Parse max empty lines argument (default: 0)
MAX_LINES="${1#-}"
[ -z "$MAX_LINES" ] && MAX_LINES=0

# Process input line by line - DON'T capture to variable, pipe directly
empty_count=0
while IFS= read -r line || [ -n "$line" ]; do
    # Check if line is empty or whitespace-only
    if [[ -z "${line// /}" ]]; then
        ((empty_count++))
        if [ $empty_count -le $MAX_LINES ]; then
            echo "$line"
        fi
    else
        empty_count=0
        echo "$line"
    fi
done <<< "$ZED_SELECTED_TEXT" | curl -X POST -d @- http://localhost:8888/paste -s
