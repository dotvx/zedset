#!/bin/bash
# Add prefix or suffix to each line

PREFIX=""
SUFFIX=""
BULLET=""

# Parse arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --prefix)
            PREFIX="$2"
            shift 2
            ;;
        --suffix)
            SUFFIX="$2"
            shift 2
            ;;
        --bullet)
            # Bullet mode: smart indentation
            BULLET="$2"
            shift 2
            ;;
        *)
            shift
            ;;
    esac
done

# Process and pipe directly
while IFS= read -r line || [ -n "$line" ]; do
    if [ -n "$BULLET" ]; then
        # Bullet mode: preserve indentation, add bullet
        indent="${line%%[! ]*}"
        content="${line#"$indent"}"
        echo "${indent}${BULLET}${content}"
    else
        # Simple prefix/suffix
        echo "${PREFIX}${line}${SUFFIX}"
    fi
done <<< "$ZED_SELECTED_TEXT" | curl -X POST -d @- http://localhost:8888/paste -s
