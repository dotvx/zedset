# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a personal Zed editor configuration repository containing:
- `settings.json`: Zed editor settings with custom fonts, keybindings, theme preferences, etc.
- `keymap.json`: Custom keybindings for Zed
- `themes/`: vx.{themename}.json files are autoloaded into Zed
- `themes/vx.desert.json`: My custom theme, containing all subthemes I use. Default!
- `conversations/`: Conversation storage directory

## Configuration Details

@settings.json
@keymap.json

## Theme Development

The `themes/vx.desert` directory contains a custom Zed theme extension with:
- `sync_theme.py`: Theme synchronization script (use `uv run sync_theme.py`)
- `theme_overrides.py`: Theme customization overrides
- `extension.toml`: Theme extension configuration
- `themes/`: Generated theme files
