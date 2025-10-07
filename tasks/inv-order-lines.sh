#!/bin/bash
# Wrapper to safely pipe ZED_SELECTED_TEXT to inv-order-lines.py and auto-paste via Hammerspoon
printf '%s' "$ZED_SELECTED_TEXT" | "$ZED/tasks/inv-order-lines.py" | curl -X POST -d @- http://localhost:8888/paste -s
