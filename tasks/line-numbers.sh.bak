#!/bin/bash
# Add or remove line numbers

REMOVE=0

# Parse arguments
for arg in "$@"; do
    case "$arg" in
        --remove) REMOVE=1 ;;
    esac
done

if [ $REMOVE -eq 1 ]; then
    # Remove line numbers (strip leading digits and spaces)
    printf '%s' "$ZED_SELECTED_TEXT" | sed -E 's/^[[:space:]]*[0-9]+[[:space:]]+//' | curl -X POST -d @- http://localhost:8888/paste -s
else
    # Add line numbers
    printf '%s' "$ZED_SELECTED_TEXT" | nl -ba -w1 -s'. ' | curl -X POST -d @- http://localhost:8888/paste -s
fi
