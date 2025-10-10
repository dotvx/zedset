#!/bin/bash
# Sort JSON keys alphabetically

# Use jq to sort keys recursively
printf '%s\n' "$ZED_SELECTED_TEXT" | jq --sort-keys . | curl -X POST --data-binary @- http://localhost:8888/paste -s
