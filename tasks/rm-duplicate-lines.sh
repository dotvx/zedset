#!/bin/bash
# Remove duplicate lines (keep first or last occurrence)

KEEP_LAST=0

# Parse arguments
for arg in "$@"; do
    case "$arg" in
        --last) KEEP_LAST=1 ;;
    esac
done

if [ $KEEP_LAST -eq 1 ]; then
    # Keep last occurrence: reverse, dedupe, reverse back
    printf '%s' "$ZED_SELECTED_TEXT" | tac | awk '!seen[$0]++' | tac | curl -X POST --data-binary @- http://localhost:8888/paste -s
else
    # Keep first occurrence: use awk directly
    printf '%s' "$ZED_SELECTED_TEXT" | awk '!seen[$0]++' | curl -X POST --data-binary @- http://localhost:8888/paste -s
fi
