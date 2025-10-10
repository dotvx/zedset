#!/bin/bash
# Trim whitespace from selected text

MODE="both"
NORMALIZE=0
BLANK_LINES=0

# Parse arguments
for arg in "$@"; do
    case "$arg" in
        --leading) MODE="leading" ;;
        --trailing) MODE="trailing" ;;
        --normalize) NORMALIZE=1 ;;
        --blank-lines) BLANK_LINES=1 ;;
    esac
done

# Process and pipe directly to avoid losing newlines
while IFS= read -r line || [ -n "$line" ]; do
    # Skip blank lines if requested
    if [ $BLANK_LINES -eq 1 ] && [[ -z "${line// /}" ]]; then
        continue
    fi

    # Normalize internal whitespace
    if [ $NORMALIZE -eq 1 ]; then
        line=$(echo "$line" | sed -E 's/[[:space:]]+/ /g')
    fi

    # Trim sides
    case "$MODE" in
        both)
            line="${line#"${line%%[![:space:]]*}"}"  # trim leading
            line="${line%"${line##*[![:space:]]}"}"  # trim trailing
            ;;
        leading)
            line="${line#"${line%%[![:space:]]*}"}"
            ;;
        trailing)
            line="${line%"${line##*[![:space:]]}"}"
            ;;
    esac

    echo "$line"
done <<< "$ZED_SELECTED_TEXT" | curl -X POST -d @- http://localhost:8888/paste -s
