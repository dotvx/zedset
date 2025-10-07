#!/bin/bash
# Wrapper to pipe ZED_SELECTED_TEXT to json-yaml.py and auto-paste via Hammerspoon

# Default to auto-detect and convert, or pass --to-json/--to-yaml
ARGS="${1:---to-yaml}"

printf '%s' "$ZED_SELECTED_TEXT" | "$ZED/tasks/json-yaml.py" "$ARGS" | curl -X POST -d @- http://localhost:8888/paste -s
