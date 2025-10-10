#!/bin/bash
# Keep only unique lines (remove duplicates)

SORT=0

# Parse arguments
for arg in "$@"; do
    case "$arg" in
        --sort) SORT=1 ;;
    esac
done

if [ $SORT -eq 1 ]; then
    # Sort and remove duplicates
    printf '%s' "$ZED_SELECTED_TEXT" | sort -u | curl -X POST -d @- http://localhost:8888/paste -s
else
    # Just remove duplicates (keep first occurrence)
    printf '%s' "$ZED_SELECTED_TEXT" | awk '!seen[$0]++' | curl -X POST -d @- http://localhost:8888/paste -s
fi
