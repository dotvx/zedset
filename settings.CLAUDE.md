# Zed Settings Configuration Expert Guide

> Comprehensive knowledge base for configuring `settings.json` with only valid options

## Settings File Location
- User settings: `~/.config/zed/settings.json`
- Project settings: `.zed/settings.json` (in project root)
- Access via: `cmd-alt-,` (macOS) or `ctrl-alt-,` (Linux/Windows)

## Settings Hierarchy (Cascade Order)
1. **Global defaults** (built-in Zed defaults)
2. **User-level settings** (`~/.config/zed/settings.json`)
3. **Project-specific settings** (`.zed/settings.json`)
4. **Language-specific overrides** (within `"languages": {}`)

Later settings override earlier ones.

## File Format
- JSON with comments support (`//` and `/* */`)
- Must be valid JSON structure
- Keys are case-sensitive and must match exact valid option names

## Major Configuration Categories

### 1. UI/Appearance
```json
{
  "theme": {
    "mode": "system" | "light" | "dark",
    "light": "theme-name",
    "dark": "theme-name"
  },
  "icon_theme": "icon-theme-name",
  "ui_font_family": ".SystemUIFont" | "font-name",
  "ui_font_size": 16,
  "ui_font_weight": 100-900,
  "ui_font_features": { "calt": true|false }
}
```

**Valid theme modes**: `"system"`, `"light"`, `"dark"`

### 2. Editor Font & Display
```json
{
  "buffer_font_family": "font-name",
  "buffer_font_size": 15,
  "buffer_font_weight": 100.0-900.0,
  "buffer_font_features": { "calt": true|false },
  "buffer_line_height": "comfortable" | "standard" | { "custom": 1.5 }
}
```

**Valid line heights**: `"comfortable"` (1.618), `"standard"` (1.3), or `{"custom": number}`

### 3. Editor Behavior
```json
{
  "cursor_blink": true|false,
  "cursor_shape": "bar" | "block" | "underline" | "hollow",
  "vim_mode": true|false,
  "helix_mode": true|false,
  "base_keymap": "VSCode" | "Atom" | "JetBrains" | "None" | "SublimeText" | "TextMate",
  "multi_cursor_modifier": "alt" | "cmd_or_ctrl" | "cmd" | "ctrl",
  "relative_line_numbers": true|false
}
```

### 4. Soft Wrap & Line Length
```json
{
  "soft_wrap": "none" | "editor_width" | "preferred_line_length" | "bounded",
  "preferred_line_length": 100,
  "show_wrap_guides": true|false,
  "wrap_guides": [80, 120]
}
```

**Wrap modes**:
- `"none"`: No wrapping (prefer single lines)
- `"editor_width"`: Wrap at editor width
- `"preferred_line_length"`: Wrap at preferred_line_length
- `"bounded"`: Wrap at smaller of editor width or preferred_line_length

### 5. Whitespace & Indentation
```json
{
  "show_whitespaces": "selection" | "none" | "all" | "boundary" | "trailing",
  "whitespace_map": {
    "space": "•",
    "tab": "→"
  },
  "hard_tabs": true|false,
  "tab_size": 4,
  "auto_indent": true|false,
  "auto_indent_on_paste": true|false
}
```

### 6. Line Highlighting & Selection
```json
{
  "current_line_highlight": "none" | "gutter" | "line" | "all",
  "selection_highlight": true|false,
  "rounded_selection": true|false,
  "minimum_contrast_for_highlights": 0-106
}
```

**APCA contrast values**:
- `0`: No adjustment
- `45`: Large fluent text (36px+)
- `60`: Content text
- `75`: Body text minimum
- `90`: Body text preferred

### 7. Completions & Code Intelligence
```json
{
  "show_completions_on_input": true|false,
  "show_completion_documentation": true|false,
  "auto_signature_help": true|false,
  "show_signature_help_after_edits": true|false,
  "snippet_sort_order": "top" | "inline" | "bottom" | "none",
  "completions": {
    "words": "enabled" | "disabled",
    "words_min_length": 5,
    "lsp": true|false,
    "lsp_fetch_timeout_ms": 5000,
    "lsp_insert_mode": "replace_suffix" | "insert"
  }
}
```

### 8. Inlay Hints
```json
{
  "inlay_hints": {
    "enabled": true|false,
    "show_type_hints": true|false,
    "show_parameter_hints": true|false,
    "show_value_hints": true|false,
    "show_other_hints": true|false,
    "show_background": true|false,
    "edit_debounce_ms": 200,
    "scroll_debounce_ms": 50,
    "toggle_on_modifiers_press": {
      "control": true|false,
      "shift": true|false,
      "alt": true|false,
      "platform": true|false,
      "function": true|false
    }
  }
}
```

### 9. Diagnostics
```json
{
  "diagnostics_max_severity": "off" | "error" | "warning" | "info" | "hint" | "all",
  "diagnostics": {
    "button": true|false,
    "include_warnings": true|false,
    "lsp_pull_diagnostics": {
      "enabled": true|false,
      "debounce_ms": 50
    },
    "inline": {
      "enabled": true|false,
      "update_debounce_ms": 150,
      "padding": 4,
      "min_column": 0,
      "max_severity": null | "error" | "warning" | "info" | "hint"
    }
  }
}
```

### 10. Scrollbar
```json
{
  "scrollbar": {
    "show": "auto" | "system" | "always" | "never",
    "cursors": true|false,
    "git_diff": true|false,
    "search_results": true|false,
    "selected_text": true|false,
    "selected_symbol": true|false,
    "diagnostics": "all" | "error" | "warning" | "information" | "none" | true | false,
    "axes": {
      "horizontal": true|false,
      "vertical": true|false
    }
  }
}
```

### 11. Minimap
```json
{
  "minimap": {
    "show": "always" | "never",
    "display_in": "active_editor" | "all_editors",
    "thumb": "always" | "on_hover" | "never",
    "thumb_border": "left_open" | "closed" | "none",
    "current_line_highlight": "all" | "gutter" | "line" | "none",
    "max_width_columns": 60
  }
}
```

### 12. Gutter
```json
{
  "gutter": {
    "line_numbers": true|false,
    "runnables": true|false,
    "breakpoints": true|false,
    "folds": true|false,
    "min_line_number_digits": 4
  }
}
```

### 13. Indent Guides
```json
{
  "indent_guides": {
    "enabled": true|false,
    "line_width": 1,
    "active_line_width": 4,
    "coloring": "fixed" | "rainbow" | "disabled",
    "background_coloring": "disabled" | "rainbow"
  }
}
```

### 14. Scrolling
```json
{
  "scroll_beyond_last_line": "off" | "one_page" | "half_page",
  "vertical_scroll_margin": 12.0,
  "horizontal_scroll_margin": 5,
  "scroll_sensitivity": 1.0,
  "fast_scroll_sensitivity": 16.0,
  "autoscroll_on_clicks": true|false
}
```

### 15. Format & Save Behavior
```json
{
  "format_on_save": "on" | "off" | "prettier" | "language_server",
  "formatter": "auto" | "prettier" | "language_server" | {
    "external": {
      "command": "prettier",
      "arguments": ["--stdin-filepath", "{buffer_path}"]
    }
  },
  "remove_trailing_whitespace_on_save": true|false,
  "ensure_final_newline_on_save": true|false,
  "extend_comment_on_newline": true|false
}
```

### 16. Autosave
```json
{
  "autosave": "off" | "on_window_change" | "on_focus_change" | {
    "after_delay": { "milliseconds": 500 }
  }
}
```

**Autosave modes**:
- `"off"`: Never autosave
- `"on_window_change"`: Save when changing focus away from Zed window
- `"on_focus_change"`: Save when changing focus away from buffer
- `{"after_delay": {"milliseconds": N}}`: Save after N ms of idle time

### 17. Git Integration
```json
{
  "git": {
    "git_gutter": "tracked_files" | "hide",
    "inline_blame": {
      "enabled": true|false,
      "delay_ms": 0,
      "padding": 7,
      "show_commit_summary": true|false,
      "min_column": 0
    },
    "blame": {
      "show_avatar": true|false
    },
    "branch_picker": {
      "show_author_name": true|false
    },
    "hunk_style": "staged_hollow" | "unstaged_hollow"
  }
}
```

### 18. Search
```json
{
  "search_wrap": true|false,
  "search": {
    "button": true|false,
    "whole_word": true|false,
    "case_sensitive": true|false,
    "include_ignored": true|false,
    "regex": true|false
  },
  "seed_search_query_from_cursor": "always" | "selection" | "never",
  "use_smartcase_search": true|false
}
```

### 19. Tabs & Tab Bar
```json
{
  "max_tabs": 16 | null,
  "tab_bar": {
    "show": true|false,
    "show_nav_history_buttons": true|false,
    "show_tab_bar_buttons": true|false
  },
  "tabs": {
    "git_status": true|false,
    "close_position": "right" | "left",
    "file_icons": true|false,
    "show_close_button": "hidden" | "always" | "on_hover",
    "activate_on_close": "history" | "next" | "previous",
    "show_diagnostics": "off" | "error" | "warning" | "all"
  }
}
```

### 20. Preview Tabs
```json
{
  "preview_tabs": {
    "enabled": true|false,
    "enable_preview_from_file_finder": true|false,
    "enable_preview_from_code_navigation": true|false
  }
}
```

### 21. Toolbar
```json
{
  "toolbar": {
    "breadcrumbs": true|false,
    "quick_actions": true|false,
    "selections_menu": true|false,
    "agent_review": true|false,
    "code_actions": true|false
  }
}
```

### 22. Title Bar
```json
{
  "title_bar": {
    "show_branch_icon": true|false,
    "show_branch_name": true|false,
    "show_project_items": true|false,
    "show_onboarding_banner": true|false,
    "show_user_picture": true|false,
    "show_sign_in": true|false,
    "show_menus": true|false
  }
}
```

### 23. Project Panel
```json
{
  "project_panel": {
    "button": true|false,
    "hide_gitignore": true|false,
    "default_width": 240,
    "dock": "left" | "right",
    "entry_spacing": "comfortable" | "compact",
    "file_icons": true|false,
    "folder_icons": true|false,
    "git_status": true|false,
    "indent_size": 20,
    "auto_reveal_entries": true|false,
    "starts_open": true|false,
    "auto_fold_dirs": true|false,
    "scrollbar": { "show": null | "auto" | "always" | "never" },
    "show_diagnostics": "all" | "error" | "warning" | "off",
    "sticky_scroll": true|false,
    "indent_guides": { "show": "always" | "on_hover" | "never" },
    "drag_and_drop": true|false,
    "hide_root": true|false
  }
}
```

### 24. Outline Panel
```json
{
  "outline_panel": {
    "button": true|false,
    "default_width": 300,
    "dock": "left" | "right",
    "file_icons": true|false,
    "folder_icons": true|false,
    "git_status": true|false,
    "indent_size": 20,
    "auto_reveal_entries": true|false,
    "auto_fold_dirs": true|false,
    "indent_guides": { "show": "always" | "on_hover" | "never" },
    "scrollbar": { "show": null | "auto" | "always" | "never" },
    "expand_outlines_with_depth": 12
  }
}
```

### 25. Git Panel
```json
{
  "git_panel": {
    "button": true|false,
    "dock": "left" | "right",
    "default_width": 360,
    "status_style": "icon" | "label_color",
    "fallback_branch_name": "main",
    "sort_by_path": true|false,
    "collapse_untracked_diff": true|false,
    "scrollbar": { "show": null | "auto" | "always" | "never" }
  }
}
```

### 26. Terminal
```json
{
  "terminal": {
    "shell": "system" | { "program": "/bin/zsh", "args": ["-l"] },
    "dock": "bottom" | "left" | "right",
    "default_width": 640,
    "default_height": 320,
    "working_directory": "current_project_directory" | "first_project_directory" | "always_home",
    "blinking": "on" | "off" | "terminal_controlled",
    "cursor_shape": "bar" | "block" | "underline" | "hollow",
    "alternate_scroll": "on" | "off",
    "option_as_meta": true|false,
    "copy_on_select": true|false,
    "keep_selection_on_copy": true|false,
    "button": true|false,
    "env": {},
    "line_height": { "custom": 1.15 } | "comfortable" | "standard",
    "detect_venv": {
      "on": {
        "directories": [".env", "env", ".venv", "venv"],
        "activate_script": "default" | "csh" | "fish"
      }
    } | "off",
    "toolbar": { "breadcrumbs": true|false },
    "scrollbar": { "show": null | "auto" | "always" | "never" },
    "font_family": "font-name",
    "font_size": 11.0,
    "font_weight": 100-900,
    "max_scroll_history_lines": 10000,
    "minimum_contrast": 0-106
  }
}
```

### 27. Agent/AI
```json
{
  "agent": {
    "enabled": true|false,
    "preferred_completion_mode": "normal" | "minimal",
    "button": true|false,
    "dock": "left" | "right" | "bottom",
    "default_width": 640,
    "default_height": 320,
    "default_view": "thread" | "text_thread",
    "default_model": {
      "provider": "zed.dev" | "anthropic" | "openai" | "google" | "ollama",
      "model": "model-name"
    },
    "model_parameters": [],
    "always_allow_tool_actions": true|false,
    "stream_edits": true|false,
    "single_file_review": true|false,
    "enable_feedback": true|false,
    "default_profile": "write" | "ask" | "minimal",
    "profiles": {
      "profile-name": {
        "name": "Profile Name",
        "enable_all_context_servers": true|false,
        "tools": {
          "tool-name": true|false
        }
      }
    },
    "notify_when_agent_waiting": "primary_screen" | "all_screens" | "off",
    "play_sound_when_agent_done": true|false,
    "expand_edit_card": true|false,
    "expand_terminal_card": true|false,
    "use_modifier_to_send": true|false,
    "message_editor_min_lines": 4,
    "agent_font_size": null | number
  },
  // Feature-specific model overrides (global level)
  "inline_assistant_model": {
    "provider": "provider-name",
    "model": "model-name"
  },
  "commit_message_model": {
    "provider": "provider-name",
    "model": "model-name"
  },
  "thread_summary_model": {
    "provider": "provider-name",
    "model": "model-name"
  },
  "inline_alternatives": [
    {
      "provider": "provider-name",
      "model": "model-name"
    }
  ]
}
```

### 28. File Finder
```json
{
  "file_finder": {
    "file_icons": true|false,
    "modal_max_width": "small" | "medium" | "large" | "xlarge" | "full",
    "skip_focus_for_active_in_search": true|false,
    "git_status": true|false,
    "include_ignored": true | false | null
  }
}
```

### 29. Status Bar
```json
{
  "status_bar": {
    "active_language_button": true|false,
    "cursor_position_button": true|false
  }
}
```

### 30. Window & Workspace
```json
{
  "confirm_quit": true|false,
  "restore_on_startup": "last_session" | "last_workspace" | "none",
  "restore_on_file_reopen": true|false,
  "close_on_file_delete": true|false,
  "when_closing_with_no_tabs": "platform_default" | "close_window" | "keep_window_open",
  "on_last_window_closed": "platform_default" | "quit_app",
  "use_system_window_tabs": true|false,
  "zoomed_padding": true|false,
  "use_system_path_prompts": true|false,
  "use_system_prompts": true|false
}
```

### 31. Pane Behavior
```json
{
  "drop_target_size": 0.0-0.5,
  "pane_split_direction_horizontal": "up" | "down",
  "pane_split_direction_vertical": "left" | "right",
  "centered_layout": {
    "left_padding": 0.2,
    "right_padding": 0.2
  },
  "active_pane_modifiers": {
    "border_size": 0.0,
    "inactive_opacity": 0.0-1.0
  },
  "bottom_dock_layout": "contained" | "full" | "left_aligned" | "right_aligned",
  "resize_all_panels_in_dock": ["left", "right", "bottom"]
}
```

### 32. LSP & Language Servers
```json
{
  "enable_language_server": true|false,
  "linked_edits": true|false,
  "language_servers": ["..."],
  "lsp_highlight_debounce": 75,
  "lsp_document_colors": "none" | "inlay" | "border" | "background",
  "global_lsp_settings": {
    "button": true|false
  },
  "lsp": {
    "language-server-name": {
      "initialization_options": {}
    }
  }
}
```

### 33. Tasks
```json
{
  "tasks": {
    "variables": {},
    "enabled": true|false,
    "prefer_lsp": true|false
  }
}
```

### 34. Debugger
```json
{
  "debugger": {
    "stepping_granularity": "line" | "instruction" | "statement",
    "save_breakpoints": true|false,
    "timeout": 2000,
    "dock": "bottom" | "left" | "right",
    "log_dap_communications": true|false,
    "format_dap_log_messages": true|false,
    "button": true|false
  },
  "debuggers": ["debugger-name"]
}
```

### 35. Edit Predictions (Copilot-style)
```json
{
  "show_edit_predictions": true|false,
  "edit_predictions_disabled_in": ["string", "comment"],
  "edit_predictions": {
    "disabled_globs": ["**/.env*", "**/*.key"],
    "mode": "eager" | "lazy",
    "enabled_in_text_threads": true|false,
    "copilot": {
      "enterprise_uri": null | "uri",
      "proxy": null | "proxy-url",
      "proxy_no_verify": null | true|false
    }
  },
  "features": {
    "edit_prediction_provider": "zed" | "copilot" | "none"
  }
}
```

### 36. File Scanning
```json
{
  "file_scan_exclusions": ["**/.git", "**/.DS_Store"],
  "file_scan_inclusions": ["/path/to/include/**"],
  "private_files": ["**/.env*", "**/*.key"],
  "redact_private_values": true|false
}
```

### 37. File Types
```json
{
  "file_types": {
    "LanguageName": ["*.ext", "filename"],
    "JavaScript": ["*.mjs"],
    "TOML": ["Cargo.lock"]
  }
}
```

### 38. Telemetry & Updates
```json
{
  "telemetry": {
    "diagnostics": true|false,
    "metrics": true|false
  },
  "disable_ai": true|false,
  "auto_update": true|false
}
```

### 39. Autoclose & Surround
```json
{
  "use_autoclose": true|false,
  "use_auto_surround": true|false,
  "always_treat_brackets_as_autoclosed": true|false,
  "use_on_type_format": true|false,
  "jsx_tag_auto_close": {
    "enabled": true|false
  }
}
```

### 40. Code Actions
```json
{
  "inline_code_actions": true|false,
  "go_to_definition_fallback": "none" | "find_all_references",
  "code_actions_on_format": {
    "source.organizeImports": true|false
  }
}
```

### 41. Miscellaneous
```json
{
  "hover_popover_enabled": true|false,
  "hover_popover_delay": 100,
  "drag_and_drop_selection": {
    "enabled": true|false,
    "delay": 300
  },
  "double_click_in_multibuffer": "select" | "open",
  "expand_excerpt_lines": 5,
  "excerpt_context_lines": 2,
  "middle_click_paste": true|false,
  "hide_mouse": "never" | "on_typing" | "on_typing_and_movement",
  "allow_rewrap": "in_comments" | "in_selections" | "anywhere",
  "unnecessary_code_fade": 0.0-1.0,
  "line_indicator_format": "short" | "long",
  "load_direnv": "direct" | "shell_hook"
}
```

### 42. Language Models
```json
{
  "language_models": {
    "anthropic": {
      "api_url": "https://api.anthropic.com"
    },
    "openai": {
      "api_url": "https://api.openai.com/v1"
    },
    "ollama": {
      "api_url": "http://localhost:11434"
    }
  }
}
```

### 43. Network & Remote
```json
{
  "proxy": null | "http://proxy-url",
  "ssh_connections": [],
  "read_ssh_config": true|false
}
```

### 44. Context & Agent Servers
```json
{
  "context_servers": {},
  "agent_servers": {}
}
```

### 45. Prettier
```json
{
  "prettier": {
    "allowed": true|false,
    "plugins": ["plugin-name"],
    // Any valid Prettier configuration options:
    "trailingComma": "es5" | "none" | "all",
    "tabWidth": 4,
    "semi": true|false,
    "singleQuote": true|false,
    "parser": "parser-name"
    // See https://prettier.io/docs/en/options.html for all options
  }
}
```

## Language-Specific Settings

Override any global setting for specific languages:

```json
{
  "languages": {
    "LanguageName": {
      "tab_size": 2,
      "hard_tabs": false,
      "soft_wrap": "editor_width",
      "format_on_save": "on",
      "formatter": "prettier" | "language_server" | "auto",
      "language_servers": ["server1", "!disabled-server", "..."],
      "debuggers": ["debugger-name"],
      "prettier": {
        "allowed": true,
        "plugins": ["prettier-plugin-name"]
      },
      "code_actions_on_format": {
        "source.organizeImports": true
      }
    }
  }
}
```

### Language Server Array Syntax
- `"server-name"`: Enable this server
- `"!server-name"`: Explicitly disable this server
- `"..."`: Include default servers

Example:
```json
"language_servers": ["vtsls", "!typescript-language-server", "..."]
```
This enables vtsls, disables typescript-language-server, and includes other defaults.

## Common Language Examples

### JavaScript/TypeScript
```json
"JavaScript": {
  "language_servers": ["!typescript-language-server", "vtsls", "..."],
  "prettier": { "allowed": true }
}
```

### Python
```json
"Python": {
  "formatter": {
    "language_server": { "name": "ruff" }
  },
  "debuggers": ["Debugpy"],
  "tab_size": 4
}
```

### Rust
```json
"Rust": {
  "debuggers": ["CodeLLDB"]
}
```

### Go
```json
"Go": {
  "code_actions_on_format": {
    "source.organizeImports": true
  },
  "debuggers": ["Delve"]
}
```

### Markdown
```json
"Markdown": {
  "format_on_save": "off",
  "soft_wrap": "editor_width",
  "prettier": { "allowed": true }
}
```

### Git Commit
```json
"Git Commit": {
  "allow_rewrap": "anywhere",
  "soft_wrap": "editor_width",
  "preferred_line_length": 72
}
```

## Best Practices

1. **Check default settings first** - Run `zed: open default settings` to see all options
2. **Use language-specific overrides** instead of global changes when possible
3. **Set format_on_save per language** - not all languages benefit from it
4. **Configure LSP servers explicitly** - use the `"!"` prefix to disable unwanted servers
5. **Use project settings** for team-specific configurations (`.zed/settings.json`)
6. **Note project setting limitations** - Not all settings work in project files (e.g., theme, vim_mode)
7. **Test one setting at a time** - easier to debug issues
8. **Keep comments** to document why non-obvious settings exist
9. **Use enum values exactly** - they're case-sensitive
10. **Numbers have ranges** - check min/max (e.g., contrast is 0-106)
11. **Font names are case-sensitive** - use exact names from system
12. **Theme names must match installed themes** - check extensions

## Validation Rules

- **Boolean**: Must be `true` or `false` (lowercase, no quotes)
- **Numbers**: Can be integers or floats, no quotes
- **Strings**: Must be quoted with valid enum value
- **Objects**: Must be valid JSON objects `{}`
- **Arrays**: Must be valid JSON arrays `[]`
- **Null**: Use `null` (lowercase, no quotes)

## Common Mistakes to Avoid

❌ `"enabled": "true"` → ✅ `"enabled": true`
❌ `"tab_size": "4"` → ✅ `"tab_size": 4`
❌ `"theme": "System"` → ✅ `"theme": { "mode": "system" }`
❌ `"soft_wrap": true` → ✅ `"soft_wrap": "editor_width"`
❌ `"diagnostics": true` → ✅ `"diagnostics": "all"` (in scrollbar context)
❌ Trailing commas in last array/object item → ✅ No trailing commas

## Special Features

### Profiles
Define temporary settings overlays:
```json
{
  "profiles": {
    "Presenting": {
      "buffer_font_size": 20,
      "ui_font_size": 20,
      "theme": "One Light"
    }
  }
}
```

Activate via: `settings profile selector: toggle`

### Session
```json
{
  "session": {
    "restore_unsaved_buffers": true
  }
}
```

### Journal
```json
{
  "journal": {
    "path": "~",
    "hour_format": "hour12" | "hour24"
  }
}
```

### Image Viewer
```json
{
  "image_viewer": {
    "unit": "binary" | "decimal"
  }
}
```

### Audio (Experimental)
```json
{
  "audio": {
    "experimental.rodio_audio": false,
    "experimental.auto_microphone_volume": false,
    "experimental.auto_speaker_volume": true,
    "experimental.denoise": true,
    "experimental.legacy_audio_compatible": true
  }
}
```

### Message Editor
```json
{
  "message_editor": {
    "auto_replace_emoji_shortcode": true
  }
}
```

## Documentation References

- Official docs: https://zed.dev/docs/configuring-zed
- All actions: https://zed.dev/docs/all-actions
- Key bindings: https://zed.dev/docs/key-bindings
- Themes: https://zed.dev/docs/themes
- Tasks: https://zed.dev/docs/tasks
- Extensions: https://zed.dev/extensions

## Accessing Default Settings

To see ALL of Zed's default settings (complete reference):
1. Open Command Palette: `cmd-shift-p` (macOS) or `ctrl-shift-p` (Linux/Windows)
2. Run command: `zed: open default settings`

This shows every available setting with Zed's default values - the most complete and accurate reference.

## Reading the Current Settings File

Always read the current `settings.json` before making changes to:
1. Understand existing configuration
2. Preserve user customizations
3. Avoid conflicts with current setup
4. Match existing code style (indentation, etc.)

```bash
Read(/Users/risenowrise/v/zed/settings.json)
```

## Making Changes

1. **Read current settings** first
2. **Identify exact setting** to change
3. **Use valid value** from this guide
4. **Preserve surrounding context** (comments, structure)
5. **Test the change** in Zed

## Emergency Reset

If settings become invalid, Zed may not start properly. To reset:
1. Locate `~/.config/zed/settings.json`
2. Rename or backup the file
3. Restart Zed (it will create default settings)
4. Gradually re-add customizations

---

*Generated for Zed editor configuration expertise*
*Last updated: 2025-10-09*
