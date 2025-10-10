#!/bin/bash
# Reverse the order of lines

printf '%s\n' "$ZED_SELECTED_TEXT" | tac | curl -X POST --data-binary @- http://localhost:8888/paste -s
