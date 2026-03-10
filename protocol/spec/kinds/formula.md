# Formula Usage Guide

## Overview

In ANX frontend interaction protocol, `formula` is a text-based formula format used for calculating field values.

## Syntax Rules

- **Variables**: No special symbols needed for variables (e.g., `age`, `price`)
- **Non-variables**: Should be wrapped in single quotes (e.g., `'constant'`, `'fixed value'`)
- **Operators**: Supports `+`, `-`, `*`, `/` operators
- **Parentheses**: Supports `()` for grouping operations

## Examples

### Basic Calculations

```
# Addition
price + tax

# Subtraction
total - discount

# Multiplication
quantity * price

# Division
total / count
```

### Complex Expressions

```
# With parentheses
(price + tax) * quantity

# Mixing variables and constants
price * '0.9'  # 10% discount

# Multiple operations
total - (tax + fee)
```

## Usage in Form Fields

```json
{
  "kind": "input",
  "type": "number",
  "nick": "total",
  "title": "Total",
  "formula": "price * quantity + tax",
  "defaultValue": 0
}
```
