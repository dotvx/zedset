#!/bin/bash
# Shuffle lines randomly

printf '%s\n' "$ZED_SELECTED_TEXT" | shuf | curl -X POST --data-binary @- http://localhost:8888/paste -s
