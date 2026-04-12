# List Component Specification

## Overview

The list component is used to display a series of related data items, supporting multiple layouts and interaction methods. It is typically used in conjunction with the form component to display and manage list data within forms.

## Basic Structure

```json
{
  "kind": "list",
  "nick": "list_name",
  "title": "List Title",
  "itemList": [
    {
      "nick": "field_name",
      "title": "Field Title",
      "kind": "input",
      "type": "string",
      "lineEdit": "2",
      "defaultValue": ""
    }
  ],
  "addButton": {
    "iitemPre": -1
  },
  "moveButton": true,
  "autoDataKey": "data_source_key"
}
```

## Field Descriptions

### Basic Fields

| Field Name | Type | Required | Description |
|------------|------|----------|-------------|
| kind | string | Yes | Component type, fixed as "list" |
| nick | string | Yes | Unique identifier for the list |
| title | string | Yes | List title displayed to users |
| itemList | array | Yes | List of fields, defining the structure of each column |
| addButton | object | No | Add button configuration |
| moveButton | boolean | No | Whether to show move up/down buttons, default is false |
| autoDataKey | string | No | Data source key, used to automatically load data from API |

### itemList Field Configuration

| Field Name | Type | Required | Description |
|------------|------|----------|-------------|
| nick | string | Yes | Field name, used for data binding |
| title | string | Yes | Field title displayed to users |
| kind | string | Yes | Field type: input, options, checkbox, progress, text |
| type | string | No | Data type: string, number, boolean, etc. |
| lineEdit | string/number | No | Edit mode: 0=hidden, 1=read-only, 2=editable |
| defaultValue | any | No | Default value |
| placeholder | string | No | Input placeholder text |
| optionsItem | array | No | Option list for select type fields |
| valueNick | string | No | Value field name in options |
| titleNick | string | No | Display field name in options |
| nickSet | object | No | Mapping configuration, automatically fill other fields when selecting |
| autoMerge | boolean | No | Whether to enable automatic merge of identical cells |
| updateSet | object | No | Configuration for automatically submitting data to backend when updating |

### addButton Configuration

| Field Name | Type | Required | Description |
|------------|------|----------|-------------|
| iitemPre | number | No | Add mode: -1=direct add, 0=quick add row, >0=pre-fill mode |

## Data Operations

### Add Item

The list component supports multiple ways to add items:

1. **Direct Add** (iitemPre: -1): Directly add a blank row
2. **Quick Add Row** (iitemPre: 0): Display a quick add row, users input the first field value and then add
3. **Pre-fill Mode** (iitemPre > 0): Automatically fill data based on configuration

### Delete Item

Each row has a delete button to remove that row.

### Move Item

When `moveButton` is true, each row displays up/down move buttons to adjust the order.

### Edit Item

Supports inline editing:
- **Input Mode**: Direct input of text
- **Select Mode**: Dropdown selection, supports single and multiple selection
- **Progress Mode**: Display progress bar
- **Read-only Mode**: Only display, not editable

### Cell Merge

When `autoMerge` is true, adjacent cells with the same value in that column are automatically merged.

## Example

### Basic List

```json
{
  "kind": "list",
  "nick": "userList",
  "title": "User List",
  "itemList": [
    {
      "nick": "username",
      "title": "Username",
      "kind": "input",
      "type": "string",
      "lineEdit": "2",
      "defaultValue": ""
    },
    {
      "nick": "age",
      "title": "Age",
      "kind": "input",
      "type": "number",
      "lineEdit": "2",
      "defaultValue": 0
    }
  ],
  "addButton": {
    "iitemPre": -1
  }
}
```

### List with Select Fields

```json
{
  "kind": "list",
  "nick": "productList",
  "title": "Product List",
  "itemList": [
    {
      "nick": "productName",
      "title": "Product Name",
      "kind": "input",
      "type": "string",
      "lineEdit": "2"
    },
    {
      "nick": "category",
      "title": "Category",
      "kind": "options",
      "type": "string",
      "lineEdit": "2",
      "optionsItem": [
        { "value": "electronics", "title": "Electronics" },
        { "value": "clothing", "title": "Clothing" }
      ]
    },
    {
      "nick": "status",
      "title": "Status",
      "kind": "options",
      "type": "string",
      "lineEdit": "2",
      "optionsItem": [
        { "value": "active", "title": "Active" },
        { "value": "inactive", "title": "Inactive" }
      ]
    }
  ],
  "addButton": {
    "iitemPre": 0
  },
  "moveButton": true
}
```

### List with Data Mapping

```json
{
  "kind": "list",
  "nick": "orderList",
  "title": "Order List",
  "itemList": [
    {
      "nick": "productId",
      "title": "Product",
      "kind": "options",
      "type": "string",
      "lineEdit": "2",
      "optionsItem": [
        { "value": "P001", "title": "Product A", "data": { "price": 100, "stock": 50 } },
        { "value": "P002", "title": "Product B", "data": { "price": 200, "stock": 30 } }
      ],
      "nickSet": {
        "price": "price",
        "stock": "stock"
      }
    },
    {
      "nick": "price",
      "title": "Price",
      "kind": "text",
      "type": "number",
      "lineEdit": "1"
    },
    {
      "nick": "stock",
      "title": "Stock",
      "kind": "text",
      "type": "number",
      "lineEdit": "1"
    }
  ],
  "addButton": {
    "iitemPre": 0
  }
}
```

### List with Cell Merge

```json
{
  "kind": "list",
  "nick": "categoryList",
  "title": "Category Statistics",
  "itemList": [
    {
      "nick": "category",
      "title": "Category",
      "kind": "text",
      "type": "string",
      "lineEdit": "1",
      "autoMerge": true
    },
    {
      "nick": "productName",
      "title": "Product Name",
      "kind": "text",
      "type": "string",
      "lineEdit": "1"
    },
    {
      "nick": "sales",
      "title": "Sales",
      "kind": "text",
      "type": "number",
      "lineEdit": "1"
    }
  ],
  "addButton": {
    "iitemPre": -1
  }
}
```

### List with Auto Data Loading

```json
{
  "kind": "list",
  "nick": "dataList",
  "title": "Data List",
  "autoDataKey": "user_data_key",
  "itemList": [
    {
      "nick": "name",
      "title": "Name",
      "kind": "text",
      "type": "string",
      "lineEdit": "1"
    },
    {
      "nick": "email",
      "title": "Email",
      "kind": "text",
      "type": "string",
      "lineEdit": "1"
    }
  ]
}
```

## Data Format

The data format of the list component is an array of objects, each object representing a row of data:

```json
[
  {
    "username": "Zhang San",
    "age": 25
  },
  {
    "username": "Li Si",
    "age": 30
  }
]
```

## Best Practices

1. **Reasonable Field Configuration**: Choose appropriate field types and edit modes based on business needs
2. **Default Value Setting**: Set reasonable default values for new rows
3. **Data Mapping**: Use nickSet to achieve automatic filling of associated data
4. **Cell Merge**: Use autoMerge for display optimization of category data
5. **Sorting Function**: Enable moveButton to allow users to adjust the order of data
6. **Data Loading**: Use autoDataKey to achieve automatic loading of initial data
