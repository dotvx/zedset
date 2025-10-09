#!/bin/bash
# Sort JSON keys alphabetically

# Use jq to sort keys recursively
printf '%s' "$ZED_SELECTED_TEXT" | jq --sort-keys . | curl -X POST -d @- http://localhost:8888/paste -s
