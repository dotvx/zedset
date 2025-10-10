#!/bin/bash
# Wrap text at specified width

WIDTH=80

# Parse arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --width) WIDTH="$2"; shift 2 ;;
        *) shift ;;
    esac
done

# Use fold to wrap text
printf '%s' "$ZED_SELECTED_TEXT" | fold -s -w "$WIDTH" | curl -X POST -d @- http://localhost:8888/paste -s
