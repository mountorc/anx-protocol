# Filter Configuration Guide

## Overview

In ANX frontend interaction protocol, `filter` is used to filter data based on specific conditions. It supports multiple formats for different use cases.

## Format 1: where

### Basic Usage

```json
{
  "where": {
    "name1": "value1"
  }
}
```

### Examples

1. **Single condition**: Filter rows where `name1` equals `value1`
   ```json
   { "name1": "value1" }
   ```

2. **Multiple values**: Filter rows where `name1` equals either `value1` or `value2`
   ```json
   { "name1": ["value1", "value2"] }
   ```

3. **Multiple conditions**: Filter rows where `name1` equals `value1` AND `name2` equals `value2`
   ```json
   { "name1": "value1", "name2": "value2" }
   ```

## Format 2: filters

### Basic Structure

```json
{
  "filters": [
    {
      "nick": "name1",
      "value": "value1"
    },
    {
      "name": "name2",
      "value": "value2"
    }
  ]
}
```

### Examples

1. **Multiple conditions with nick**: Filter rows where `name1` equals `value1` AND `name2` equals `value2`
   ```json
   [
     { "nick": "name1", "value": "value1" },
     { "nick": "name2", "value": "value2" }
   ]
   ```

2. **Multiple conditions with name**: Filter rows where `name1` equals `value1` AND `name2` equals `value2`
   ```json
   [
     { "name": "name1", "value": "value1" },
     { "name": "name2", "value": "value2" }
   ]
   ```

3. **With operator type**: Filter rows where `name1` equals `value1`
   ```json
   [
     { "name": "name1", "type": "=", "value": "value1" }
   ]
   ```

4. **With named operator**: Filter rows where `name1` equals `value1`
   ```json
   [
     { "name": "name1", "type": "EQ", "value": "value1" }
   ]
   ```

5. **Multiple values with operator**: Filter rows where `name1` equals either `value1` or `value2`
   ```json
   [
     { "name": "name1", "type": "EQ", "value": ["value1", "value2"] }
   ]
   ```

6. **Greater than operator**: Filter rows where `name1` is greater than `value1`
   ```json
   [
     { "name": "name1", "type": ">", "value": "value1" }
   ]
   ```

7. **Greater than or equal operator**: Filter rows where `name1` is greater than or equal to `value1`
   ```json
   [
     { "name": "name1", "type": ">=", "value": "value1" }
   ]
   ```

## Field Aliases

- **Field name**: Can be either `nick` or `name`
- **Operator**: Can be either `type` or `filterType`
- **Value**: Can be either `value` or `filterValue`

## Supported Operators

| Operator | Description |
|----------|-------------|
| `=`      | Equals |
| `>`      | Greater than |
| `>=`     | Greater than or equal |
| `<`      | Less than |
| `<=`     | Less than or equal |
| `!=`     | Not equal |
| `EQ`     | Equals |
| `IN`     | In array |
| `NOT IN` | Not in array |
| `CONTAIN` | Contains substring |
| `NOT CONTAIN` | Does not contain substring |
| `STARTSWITH` | Starts with substring |
| `ENDSWITH` | Ends with substring |

## Value Types

- **String**: `"value"`
- **Number**: `123`
- **Array**: `["value1", "value2"]`

## Usage Examples

### Example 1: Simple where filter

```json
{
  "where": {
    "status": "active",
    "category": ["electronics", "clothing"]
  }
}
```

### Example 2: Complex filters with operators

```json
{
  "filters": [
    {
      "name": "price",
      "type": ">=",
      "value": 100
    },
    {
      "name": "price",
      "type": "<=",
      "value": 1000
    },
    {
      "name": "category",
      "type": "IN",
      "value": ["electronics", "home"]
    },
    {
      "name": "name",
      "type": "CONTAIN",
      "value": "smart"
    }
  ]
}
```

## Best Practices

- Use `where` for simple equality conditions
- Use `filters` for complex conditions with operators
- Be consistent with field names (use either `nick` or `name` throughout)
- Use appropriate value types for different operators
- Test filters with various data types to ensure compatibility
