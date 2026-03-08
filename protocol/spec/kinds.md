# Kinds Usage Guide

## Overview

In ANX frontend interaction protocol, `kinds` and `kind` fields are used to define component structures:

- **kinds**: Represents sub-components, typically in array format `kinds: []`
- **kind**: Represents component type, typically in string format `kind: "input"`

## Component Types

Components are divided into two main categories: **item** and **card**, with no duplicate names between categories.

### 1. Item Components

Item components are primarily input-focused elements:

| Component Type | Description |
|----------------|-------------|
| `input`        | Single-line input field |
| `textarea`     | Multi-line input field |
| `options`      | Single selection (radio buttons or dropdown) |
| `checkbox`     | Multiple selection (checkboxes) |
| `button`       | Action button |
| `text`         | Static text display |

### 2. Card Components

Card components are more complex, container-like elements:

| Component Type | Description |
|----------------|-------------|
| `table`        | Data table |
| `box`          | Card container |
| `form`         | Form container |
| `json`         | JSON display and editing |
| `list`         | JSON format list display and editing |
