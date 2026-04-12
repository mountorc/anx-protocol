# Chart Component Guide

## Overview

This guide describes the `chart` component in ANX frontend interaction protocol, which is used to display various types of charts and visualizations.

## Component Structure

The `chart` component is defined with `kind: "chart"` and supports the following properties:

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `kind`   | string | Yes | Must be "chart" to indicate this is a chart component |
| `title`  | string | No | Optional title for the chart |
| `type`   | string | Yes | Chart type, such as "pie", "line", "bar", "scatter", "radar", etc. |
| `dataset` | object | Yes | Dataset configuration for the chart |
| `options` | object | No | Additional chart options and configurations |
| `height` | string | No | Optional height for the chart container (e.g., "400px") |
| `width`  | string | No | Optional width for the chart container (e.g., "100%") |

## Dataset Configuration

The `dataset` property is required and defines the data source for the chart. It supports two formats:

### 1. Direct Data Array

```json
{
  "dataset": {
    "data": [
      { "name": "Category 1", "value": 100 },
      { "name": "Category 2", "value": 200 },
      { "name": "Category 3", "value": 150 }
    ]
  }
}
```

### 2. Dataset UUID

```json
{
  "dataset": {
    "uuid_dataset": "chart_data_dataset"
  }
}
```

### 3. URL Dataset

```json
{
  "dataset": {
    "url_dataset": "https://api.example.com/chart-data"
  }
}
```

## Chart Types

The `type` property specifies the chart type. Supported types include:

| Type | Description |
|------|-------------|
| `pie` | Pie chart for showing proportions |
| `line` | Line chart for showing trends over time |
| `bar` | Bar chart for comparing categories |
| `scatter` | Scatter plot for showing relationships between variables |
| `radar` | Radar chart for showing multiple dimensions |
| `doughnut` | Doughnut chart (similar to pie chart) |
| `polarArea` | Polar area chart |
| `bubble` | Bubble chart |
| `area` | Area chart |

## Basic Usage

### Pie Chart Example

```json
{
  "kind": "chart",
  "title": "Sales Distribution",
  "type": "pie",
  "dataset": {
    "data": [
      { "name": "Electronics", "value": 35 },
      { "name": "Clothing", "value": 25 },
      { "name": "Home Goods", "value": 20 },
      { "name": "Food", "value": 15 },
      { "name": "Other", "value": 5 }
    ]
  },
  "height": "400px"
}
```

### Line Chart Example

```json
{
  "kind": "chart",
  "title": "Monthly Sales Trend",
  "type": "line",
  "dataset": {
    "data": [
      { "month": "Jan", "sales": 1000 },
      { "month": "Feb", "sales": 1200 },
      { "month": "Mar", "sales": 1500 },
      { "month": "Apr", "sales": 1300 },
      { "month": "May", "sales": 1800 },
      { "month": "Jun", "sales": 2000 }
    ]
  },
  "options": {
    "xAxis": "month",
    "yAxis": "sales"
  },
  "height": "400px"
}
```

### Bar Chart Example with Dataset UUID

```json
{
  "kind": "chart",
  "title": "Product Categories",
  "type": "bar",
  "dataset": {
    "uuid_dataset": "product_categories_dataset"
  },
  "options": {
    "xAxis": "category",
    "yAxis": "count"
  },
  "height": "400px"
}
```

## Options Configuration

The `options` property allows for additional chart configurations:

```json
{
  "options": {
    "xAxis": "category",       // Field to use for x-axis
    "yAxis": "value",          // Field to use for y-axis
    "colors": ["#FF6384", "#36A2EB", "#FFCE56"], // Custom colors
    "legend": true,             // Show legend
    "tooltip": true,            // Show tooltips
    "animation": true,          // Enable animations
    "responsive": true,         // Make chart responsive
    "maintainAspectRatio": false // Allow custom aspect ratio
  }
}
```

## Formula Support

The `chart` component supports formula substitution in its properties:

```json
{
  "kind": "chart",
  "title": "Sales for {{year}}",
  "type": "bar",
  "dataset": {
    "data": "{{salesData}}"
  },
  "height": "{{chartHeight}}"
}
```

## Best Practices

- Choose the appropriate chart type based on your data and visualization needs
- Keep chart titles clear and descriptive
- Use consistent colors across charts in your application
- Ensure datasets are properly formatted for the selected chart type
- Test charts with different screen sizes to ensure responsiveness
- Consider performance implications when working with large datasets

## Performance Considerations

- Large datasets may impact rendering performance
- Consider data aggregation for large datasets
- Use appropriate chart types for large datasets (e.g., avoid pie charts with too many slices)
- Consider lazy-loading charts that are not initially visible

## Error Handling

- If the dataset is invalid or unavailable, the chart may not render
- If the chart type is not supported, a fallback may be used
- Ensure proper error handling for dataset loading failures
- Test charts with various data scenarios to ensure robustness