# UpdateData Configuration Guide

## Overview

In ANX frontend interaction protocol, `updateData` is an action type used to update data in a dataset. It provides a unified way to handle both data updates and inserts based on unique identifiers.

## UpdateData Configuration Structure

```json
{
  "updateData": {
    "tableName": "table_name",
    "paramMap": {
      "table_field1": "source_field1",
      "table_field2": "source_field2"
    },
    "uniqueMap": {
      "table_unique_field": "source_unique_field"
    }
  }
}
```

## Field Descriptions

| Field | Description | Required |
|-------|-------------|----------|
| `tableName` | Name of the table where data will be updated or inserted (e.g., "table_name") | Yes |
| `paramMap` | Mapping of table field names to source field names (e.g., {"table_field1": "source_field1"}) | Yes |
| `uniqueMap` | Mapping of table unique identifier field names to source field names (e.g., {"table_unique_field": "source_unique_field"}) | Yes |

## Working Principle

The `updateData` action follows this logic:

1. **Check Existence**: Uses the `uniqueMap` (e.g., {"table_unique_field": "source_unique_field"}) to map source field names to table field names and query if a record with these values already exists
2. **Update or Insert**: 
   - If the record exists, it updates the fields specified in `paramMap` (e.g., {"table_field1": "source_field1"}) using the mapped source values
   - If the record doesn't exist, it inserts a new record using both the `paramMap` and `uniqueMap` mappings

## Usage Examples

### Example 1: Updating User Information

```json
{
  "updateData": {
    "tableName": "table_name",
    "paramMap": {
      "table_field1": "source_field1",
      "table_field2": "source_field2",
      "table_field3": "source_field3"
    },
    "uniqueMap": {
      "table_unique_field": "source_unique_field"
    }
  }
}
```

### Example 2: Inserting New Product

```json
{
  "updateData": {
    "tableName": "table_name",
    "paramMap": {
      "table_field1": "source_field1",
      "table_field2": "source_field2",
      "table_field3": "source_field3"
    },
    "uniqueMap": {
      "table_unique_field": "source_unique_field"
    }
  }
}
```

### Example 3: Updating Order Status

```json
{
  "updateData": {
    "tableName": "table_name",
    "paramMap": {
      "table_field1": "source_field1",
      "table_field2": "source_field2"
    },
    "uniqueMap": {
      "table_unique_field": "source_unique_field"
    }
  }
}
```

## Best Practices

- **Use Meaningful Table Names**: Ensure `tableName` accurately reflects the data it contains
- **Choose Appropriate Unique Fields**: Select fields that uniquely identify records in the table
- **Include All Necessary Fields**: Make sure `paramMap` includes all fields that need to be updated
- **Consistent Naming**: Use consistent naming conventions for fields across the application
- **Clear Mapping**: Ensure `paramMap` and `uniqueMap` clearly map table fields to source fields
- **Validation**: Validate data before using it in `updateData` to ensure data integrity
- **Error Handling**: Implement error handling for cases where the update/insert operation fails

## Use Cases

`updateData` is particularly useful in scenarios where:

1. **Form Submissions**: When users submit forms that may either create new records or update existing ones
2. **User Profiles**: When updating user information where the user ID is the unique identifier
3. **Product Management**: When adding or updating product information
4. **Order Processing**: When updating order status or details

## Implementation Notes

- The `uniqueMap` can contain multiple fields to create a composite unique identifier
- The `paramMap` can include any number of fields to update
- The actual implementation of the update/insert logic depends on the backend system being used
- It's important to ensure that the backend properly handles the logic for checking existence and performing the appropriate operation