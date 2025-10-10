#!/bin/bash
# Shuffle lines randomly

printf '%s' "$ZED_SELECTED_TEXT" | shuf | curl -X POST -d @- http://localhost:8888/paste -s
