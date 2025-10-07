#!/bin/bash
# Wrapper to safely pipe ZED_SELECTED_TEXT to emptyLines.py and auto-paste via Hammerspoon

# Extract numeric value from flag (e.g., "-1" -> "1", "-2" -> "2")
# Default to 0 if no argument provided
if [ -z "$1" ]; then
	MAX_LINES=0
else
	MAX_LINES="${1#-}"  # Remove leading dash
fi

printf '%s' "$ZED_SELECTED_TEXT" | /Users/risenowrise/v/py/zed/emptyLines.py "$MAX_LINES" | curl -X POST -d @- http://localhost:8888/paste -s
