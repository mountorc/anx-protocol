# Formula Usage Guide

## Overview

In ANX frontend interaction protocol, `formula` is a text-based formula format used for calculating field values.

## Syntax Rules

- **Variables**: No special symbols needed for variables (e.g., `age`, `price`)
- **Non-variables**: Should be wrapped in single quotes (e.g., `'constant'`, `'fixed value'`)
- **Operators**: Supports `+`, `-`, `*`, `/` operators
- **Parentheses**: Supports `()` for grouping operations
- **Conditional statements**: Supports `case when then else end` syntax (reference SQL syntax)
  - **Variables in conditions**: Use variables directly in conditions (e.g., `case when age >= 18 then 'Adult' else 'Minor' end`)
  - **Multiple conditions**: Support multiple `when` clauses for different conditions
  - **Nested conditions**: Support nested `case` statements

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

### Conditional Statements (case when) - SQL syntax

```sql
-- Basic case when (SQL syntax)
case when age >= 18 then 'Adult' else 'Minor' end

-- Multiple conditions (SQL syntax)
case when score >= 90 then 'A' 
     when score >= 80 then 'B' 
     when score >= 70 then 'C' 
     else 'D' end

-- Nested conditions (SQL syntax)
case when age >= 18 then 
    case when age >= 65 then 'Senior' else 'Adult' end
else 'Minor' end
```

### Notes:
- Variables can be used directly in conditions without special symbols
- String constants must be wrapped in single quotes
- Conditions are evaluated in order, and the first matching condition is used
- The `else` clause is optional, but recommended to handle all cases

## Usage in Form Fields

### Basic Calculation

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

### Using case when Syntax

```json
{
  "kind": "input",
  "type": "text",
  "nick": "ageGroup",
  "title": "Age Group",
  "formula": "case when age >= 18 then 'Adult' else 'Minor' end",
  "defaultValue": "Minor"
}
```

```json
{
  "kind": "input",
  "type": "text",
  "nick": "grade",
  "title": "Grade",
  "formula": "case when score >= 90 then 'A' when score >= 80 then 'B' when score >= 70 then 'C' else 'D' end",
  "defaultValue": "D"
}
```
