# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a personal Zed editor configuration repository containing:
- `settings.json`: Zed editor settings with custom fonts, keybindings, theme preferences, etc.
- `keymap.json`: Custom keybindings for Zed
- `themes/`: Custom theme extensions, currently includes zed-catppuccin-blur
- `prompts/`: Prompts library database (prompts-library-db.0.mdb)
- `conversations/`: Conversation storage directory

## Configuration Details

**Editor Settings:**
- Base keymap: VSCode
- Vim mode: Disabled
- Font: .ZedMono (buffer), .SystemUIFont (UI)
- Theme: Catppuccin variants (Latte for light, Espresso Blur for dark)
- Hard tabs with tab size 4
- Autosave on focus change
- Telemetry disabled

**Custom Keybindings:**
- `shift shift`: Toggle file finder
- `cmd-shift-c`: Copy file path
- `ctrl-left`: Fold code

## Theme Development

The `themes/zed-catppuccin-blur/` directory contains a custom Zed theme extension with:
- `sync_theme.py`: Theme synchronization script (use `uv run sync_theme.py`)
- `theme_overrides.py`: Theme customization overrides
- `extension.toml`: Theme extension configuration
- `themes/`: Generated theme files

When working with themes, use `uv run` for Python scripts.

## File Type Associations

Custom file type mappings are configured in settings.json for CSV, env files, JSON/JSONC, shell scripts, YAML, Markdown, and more.
