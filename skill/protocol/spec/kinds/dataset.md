# Dataset Configuration Guide

## Overview

In ANX frontend interaction protocol, datasets are used to store and manage structured data. By using `uuid_dataset`, you can reference specific datasets in components like tables to fetch data from them.

## Dataset Structure

A dataset is identified by its unique UUID. You can reference a dataset in table components by adding the `uuid_dataset` field.

## Usage in Table Components

To use a dataset as the data source for a table, you can use either `uuid_dataset` or `url_dataset`:

### Using uuid_dataset

```json
{
  "kind": "table",
  "nick": "users_table",
  "title": "Users",
  "dataset": {
    "uuid_dataset": "数据集UUID"
  },
  "titles": [
    {
      "title": "ID",
      "nick": "id",
      "kind": "text",
      "type": "number"
    },
    {
      "title": "Name",
      "nick": "name",
      "kind": "text",
      "type": "string"
    }
  ]
}
```

### Using url_dataset

```json
{
  "kind": "table",
  "nick": "users_table",
  "title": "Users",
  "dataset": {
    "url_dataset": "https://api.example.com/users"
  },
  "titles": [
    {
      "title": "ID",
      "nick": "id",
      "kind": "text",
      "type": "number"
    },
    {
      "title": "Name",
      "nick": "name",
      "kind": "text",
      "type": "string"
    }
  ]
}
```

## Field Descriptions

| Field | Description | Required |
|-------|-------------|----------|
| `dataset` | Dataset configuration object | No |
| `dataset.uuid_dataset` | UUID of the dataset to fetch data from | No |
| `dataset.url_dataset` | URL to fetch data from (alternative to uuid_dataset) | No |

> Note: You can use either `dataset.uuid_dataset` or `dataset.url_dataset`, but not both. If both are provided, `dataset.uuid_dataset` takes precedence.

## Example Table Configuration with Dataset

```json
{
  "kind": "table",
  "nick": "products_table",
  "title": "Products",
  "dataset": {
    "uuid_dataset": "product_dataset_123"
  },
  "titles": [
    {
      "title": "Product ID",
      "nick": "id",
      "kind": "text",
      "type": "string"
    },
    {
      "title": "Product Name",
      "nick": "name",
      "kind": "text",
      "type": "string"
    },
    {
      "title": "Price",
      "nick": "price",
      "kind": "text",
      "type": "number"
    },
    {
      "title": "Stock",
      "nick": "stock",
      "kind": "text",
      "type": "number"
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

## Dataset API

To fetch data from a dataset, you can use the following API endpoint:

```
/anx/dataset/{uuid_dataset}
```

### Example API Response

```json
{
  "data": [
    [
      { "nick": "id", "value": "P001" },
      { "nick": "name", "value": "Product 1" },
      { "nick": "price", "value": 100 },
      { "nick": "stock", "value": 50 }
    ],
    [
      { "nick": "id", "value": "P002" },
      { "nick": "name", "value": "Product 2" },
      { "nick": "price", "value": 200 },
      { "nick": "stock", "value": 30 }
    ]
  ],
  "total": 100,
  "pageSize": 20,
  "pageNum": 1
}
```

## Best Practices

- Use descriptive UUIDs for datasets
- Ensure datasets are properly configured with the correct structure
- Use `dataset.uuid_dataset` for static or pre-configured data
- Use `dataset.url_dataset` for dynamic data that needs to be fetched from an API
- Implement proper error handling for dataset retrieval
- Consider caching dataset data for better performance

## Dataset Management

Datasets can be managed through the ANX admin interface, where you can:

1. Create new datasets
2. Import data into datasets
3. Edit dataset structure
4. Manage dataset permissions
5. View dataset usage statistics
