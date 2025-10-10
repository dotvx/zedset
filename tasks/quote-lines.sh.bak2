#!/bin/bash
# Wrap lines in quotes or brackets

QUOTE_TYPE="double"
JOIN=""

# Parse arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --single) QUOTE_TYPE="single"; shift ;;
        --backtick) QUOTE_TYPE="backtick"; shift ;;
        --bracket) QUOTE_TYPE="bracket"; shift ;;
        --paren) QUOTE_TYPE="paren"; shift ;;
        --angle) QUOTE_TYPE="angle"; shift ;;
        --join) JOIN="$2"; shift 2 ;;
        *) shift ;;
    esac
done

# Set quote characters
case "$QUOTE_TYPE" in
    single) OPEN="'"; CLOSE="'" ;;
    backtick) OPEN='`'; CLOSE='`' ;;
    bracket) OPEN='['; CLOSE=']' ;;
    paren) OPEN='('; CLOSE=')' ;;
    angle) OPEN='<'; CLOSE='>' ;;
    *) OPEN='"'; CLOSE='"' ;;
esac

if [ -n "$JOIN" ]; then
    # Join mode: build array on one line
    first=1
    while IFS= read -r line || [ -n "$line" ]; do
        if [ $first -eq 1 ]; then
            printf '%s' "${OPEN}${line}${CLOSE}"
            first=0
        else
            printf '%s' "${JOIN}${OPEN}${line}${CLOSE}"
        fi
    done <<< "$ZED_SELECTED_TEXT" | curl -X POST -d @- http://localhost:8888/paste -s
else
    # Normal mode: each line quoted separately
    while IFS= read -r line || [ -n "$line" ]; do
        echo "${OPEN}${line}${CLOSE}"
    done <<< "$ZED_SELECTED_TEXT" | curl -X POST -d @- http://localhost:8888/paste -s
fi
