# Table Configuration Guide

## Overview

In ANX frontend interaction protocol, table components are used to display structured data in a tabular format. This guide defines the configuration structure for table components.

## Table Structure

A typical table configuration includes the following structure:

```json
{
  "kind": "table",
  "nick": "table_name",
  "title": "Table Title",
  "dataset": {
    "uuid_dataset": "数据集UUID",
    "url_dataset": "数据URL地址"
  },
  "labels": [
    {
      "label": "显示名",
      "nick": "字段名",
      "kind": "列格式",
      "type": "字段类型",
      "formula": "计算公式",
      "width": "列宽（数值，默认px）",
      "hide": "隐藏不显示（true/false）"
    }
  ],
  "pagination": {
    "pageSize": 10,
    "pageNum": 1
  },
  "filter": {
    "where": {
      "status": "active"
    }
  },
  "sort": {
    "field": "created_at",
    "order": "desc"
  }
}
```

## Field Descriptions

| Field | Description | Required |
|-------|-------------|----------|
| `kind` | Component type, must be "table" | Yes |
| `nick` | Unique identifier for the table | Yes |
| `title` | Table title displayed to users | Yes |
| `dataset` | Dataset configuration | No |
| `labels` | Array of column definitions | Yes |
| `data` | Table data (JSON list) | No |
| `pagination` | Pagination configuration | No |
| `filter` | Filter configuration | No |
| `sort` | Sort configuration | No |

## Dataset Structure

For detailed information about dataset configuration, please refer to the [Dataset Configuration Guide](dataset.md).

| Field | Description | Required |
|-------|-------------|----------|
| `uuid_dataset` | UUID of the dataset to fetch data from | No |
| `url_dataset` | URL to fetch data from (alternative to uuid_dataset) | No |

> Note: You must provide either `uuid_dataset` or `url_dataset` in the dataset configuration.

## Label Structure

Each column in the `labels` array includes the following fields:

| Field | Description | Required |
|-------|-------------|----------|
| `label` | Display name | Yes |
| `nick` | Field name | Yes |
| `kind` | Column format | No |
| `type` | Field type | No |
| `formula` | Calculation formula | No |
| `width` | Column width (numeric, default px) | No |
| `hide` | Whether to hide the column (true/false) | No |
| `options` | Array of options for selectable columns | No |
| `optionsSet` | Configuration for loading options from a dataset | No |

## Pagination Structure

| Field | Description | Required |
|-------|-------------|----------|
| `pageSize` | Number of items per page | No |
| `pageNum` | Current page number | No |
| `total` | Total number of items | No |

## Sort Structure

| Field | Description | Required |
|-------|-------------|----------|
| `field` | Field to sort by | No |
| `order` | Sort order: asc, desc | No |

## Example Table Configuration

### Using uuid_dataset

```json
{
  "kind": "table",
  "nick": "users_table",
  "title": "Users",
  "dataset": {
    "uuid_dataset": "users_dataset_123"
  },
  "labels": [
    {
      "label": "ID",
      "nick": "id",
      "kind": "text",
      "type": "number",
      "width": 80,
      "hide": false
    },
    {
      "label": "Name",
      "nick": "name",
      "kind": "text",
      "type": "string",
      "width": 150,
      "hide": false
    },
    {
      "label": "Email",
      "nick": "email",
      "kind": "text",
      "type": "string",
      "width": 200,
      "hide": false
    },
    {
      "label": "Status",
      "nick": "status",
      "kind": "text",
      "type": "string",
      "width": 100,
      "hide": false
    },
    {
      "label": "Category",
      "nick": "category_id",
      "kind": "text",
      "type": "string",
      "width": 150,
      "hide": false,
      "optionsSet": {
        "dataset": {
          "uuid_dataset": "categories_dataset"
        },
        "labelNick": "categoryName",
        "valueNick": "categoryId"
      }
    },
    {
      "label": "Created At",
      "nick": "created_at",
      "kind": "text",
      "type": "datetime",
      "width": 180,
      "hide": false
    },
    {
      "label": "Action",
      "nick": "action",
      "kind": "text",
      "type": "string",
      "width": 120,
      "hide": false
    }
  ],
  "pagination": {
    "pageSize": 10,
    "pageNum": 1
  },
  "filter": {
    "where": {
      "status": "active"
    }
  },
  "sort": {
    "field": "created_at",
    "order": "desc"
  }
}
```

### Using url_dataset

```json
{
  "kind": "table",
  "nick": "products_table",
  "title": "Products",
  "dataset": {
    "url_dataset": "https://api.example.com/products"
  },
  "labels": [
    {
      "label": "Product ID",
      "nick": "id",
      "kind": "text",
      "type": "string",
      "width": 100,
      "hide": false
    },
    {
      "label": "Product Name",
      "nick": "name",
      "kind": "text",
      "type": "string",
      "width": 200,
      "hide": false
    },
    {
      "label": "Price",
      "nick": "price",
      "kind": "text",
      "type": "number",
      "width": 100,
      "hide": false
    },
    {
      "label": "Stock",
      "nick": "stock",
      "kind": "text",
      "type": "number",
      "width": 100,
      "hide": false
    }
  ],
  "pagination": {
    "pageSize": 20,
    "pageNum": 1
  },
  "sort": {
    "field": "name",
    "order": "asc"
  }
}
```

## Example Data Source Response

```json
{
  "data": [
    [
      { "nick": "id", "value": 1 },
      { "nick": "name", "value": "John Doe" },
      { "nick": "email", "value": "john@example.com" },
      { "nick": "status", "value": "active" },
      { "nick": "created_at", "value": "2024-01-01T00:00:00Z" }
    ],
    [
      { "nick": "id", "value": 2 },
      { "nick": "name", "value": "Jane Smith" },
      { "nick": "email", "value": "jane@example.com" },
      { "nick": "status", "value": "inactive" },
      { "nick": "created_at", "value": "2024-01-02T00:00:00Z" }
    ]
  ],
  "total": 100,
  "pageSize": 10,
  "pageNum": 1
}
```

## Best Practices

- Use descriptive `nick` names for tables
- Define clear and concise column titles
- Set appropriate column widths for better readability
- Use `sortable` for columns that users might want to sort
- Implement pagination for large datasets
- Use filters to help users find relevant data
- Consider using custom formatters for complex data types
- Optimize data source endpoints for performance

## Advanced Features

### Custom Formatters

Custom formatters can be used to display data in a more user-friendly way:

```json
{
  "field": "status",
  "label": "Status",
  "formatter": "statusFormatter"
}
```

### Row Actions

You can add action buttons to each row:

```json
{
  "field": "action",
  "label": "Action",
  "formatter": "actionFormatter"
}
```

### Nested Tables

For complex data, you can implement nested tables:

```json
{
  "kind": "table",
  "nick": "orders_table",
  "title": "Orders",
  "dataset": {
    "uuid_dataset": "orders_dataset_123"
  },
  "labels": [
    // Main table columns
  ],
  "expandable": {
    "children": {
      "dataset": {
        "url_dataset": "https://api.example.com/order-items"
      },
      "labels": [
        // Nested table columns
      ]
    }
  }
}
```
