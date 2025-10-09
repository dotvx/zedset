# Paste via Hammerspoon HTTP server (port 8888)

# Basic usage - paste text to active window:
curl -X POST http://localhost:8888/paste -d "text to paste"

# Paste with variable:
TEXT="your content here"
curl -X POST http://localhost:8888/paste -d "$TEXT"

# Paste from file:
curl -X POST http://localhost:8888/paste -d @/path/to/file.txt

# Paste from clipboard:
pbpaste | curl -X POST http://localhost:8888/paste -d @-

# Paste multiline:
curl -X POST http://localhost:8888/paste -d "line 1
line 2
line 3"