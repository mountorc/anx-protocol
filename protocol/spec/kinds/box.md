# Box Component Guide

## Overview

The `box` kind is a container component in ANX frontend interaction protocol that can display content with a title. It supports data binding and dynamic content rendering.

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `dataset` | Object | No | Data source configuration, used to fetch data for the box |
| `title` | String | No | Title text to display at the top of the box |
| `html` | String | No | HTML content following the content processing rules |
| `template` | String | No | Template content following the content processing rules (alternative to `html` field) |

## Content Processing

Both the `html` and `template` fields follow the same content processing rules as defined in [content.md](../utils/content.md). They support:

- **Variable substitution**: `{{variable}}` or `${variable}`
- **Formula evaluation**: `{{formula}}` or `${formula}`
- **Nested properties**: `{{object.property}}`
- **Array access**: `{{array[0]}}`

## Basic Usage

```json
{
  "kind": "box",
  "title": "Welcome",
  "html": "<p>Hello, {{user.name}}!</p>"
}
```

## With Dataset

When using the `dataset` parameter, the box component will:
1. Fetch data from the specified dataset
2. Use either the `html` or `template` field as a template (if both are provided, `template` takes precedence)
3. Assign variables from the dataset to the template
4. Render the template for each item in the dataset, creating a list

```json
{
  "kind": "box",
  "title": "User Profile",
  "dataset": {
    "uuid_dataset": "dataset_uuid_here"
  },
  "html": "<div><h1>{{user.name}}</h1><p>{{user.email}}</p></div>"
}
```

### Dataset as List

When the dataset returns multiple items, the box will render the html or template for each item:

```json
{
  "kind": "box",
  "title": "Product List",
  "dataset": {
    "uuid_dataset": "products_dataset_001"
  },
  "html": "<div class='product'><h2>{{product.name}}</h2><p class='price'>${{product.price}}</p></div>"
}
```

This will generate a list of product items, each rendered using the html template with the corresponding product data.

## Dynamic Content

Both the `html` and `template` fields can contain dynamic content using formula substitution:

```json
{
  "kind": "box",
  "title": "Order Summary",
  "html": "<p>Total: ${{order.total}}</p><p>Items: {{order.itemCount}}</p>"
}
```

## Example

### Using html field

```json
{
  "kind": "box",
  "title": "Product Details",
  "dataset": {
    "uuid_dataset": "product_dataset_001"
  },
  "html": "<div class='product'><h2>{{product.name}}</h2><p class='price'>${{product.price}}</p><p class='desc'>{{product.description}}</p></div>"
}
```

### Using template field

```json
{
  "kind": "box",
  "title": "Product Details",
  "dataset": {
    "uuid_dataset": "product_dataset_001"
  },
  "template": "<div class='product'><h2>{{product.name}}</h2><p class='price'>${{product.price}}</p><p class='desc'>{{product.description}}</p></div>"
}
```

## Best Practices

- Use the `title` parameter to provide a clear header for the box content
- Use the `dataset` parameter when the content needs to be fetched from a data source
- Use either `html` or `template` field for content (not both)
- Follow the content processing rules for dynamic content in both `html` and `template` fields
- Keep the HTML structure simple and semantic for better accessibility
