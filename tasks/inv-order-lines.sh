#!/bin/bash
# Wrapper to safely pipe ZED_SELECTED_TEXT to reverseOrder.py and auto-paste via Hammerspoon
printf '%s' "$ZED_SELECTED_TEXT" | /Users/risenowrise/v/py/zed/reverseOrder.py | curl -X POST -d @- http://localhost:8888/paste -s
