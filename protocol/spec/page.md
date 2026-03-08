# Page Configuration Guide

## Overview

In ANX frontend interaction protocol, a page configuration defines the structure and behavior of a complete page.

## Page Structure

A typical page configuration includes the following structure:

```json
{
  "page": "page_name",
  "uuid_page": "unique_page_identifier",
  "title": "Page Title",
  "description": "Page description",
  "kinds": [
    // Component configurations
  ]
}
```

## Field Descriptions

| Field | Description | Required |
|-------|-------------|----------|
| `page` | Page name or identifier | Yes |
| `uuid_page` | Unique page identifier | Yes |
| `title` | Page title displayed to users | Yes |
| `description` | Brief description of the page | No |
| `kinds` | Array of components on the page | Yes |

## Component Structure

Each component in the `kinds` array follows the standard ANX component structure:

```json
{
  "kind": "component_type",
  "nick": "unique_field_name",
  "title": "Component Title",
  "type": "data_type",
  "defaultValue": "default_value",
  "formula": "calculation_formula",
  // Additional component-specific fields
}
```

## Example Page Configuration

```json
{
  "page": "dashboard",
  "uuid_page": "dashboard_123",
  "title": "Dashboard",
  "description": "Main dashboard page",
  "kinds": [
    {
      "kind": "box",
      "nick": "overview",
      "title": "Overview",
      "kinds": [
        {
          "kind": "text",
          "nick": "welcome",
          "title": "Welcome",
          "type": "string",
          "defaultValue": "Welcome to the dashboard!"
        },
        {
          "kind": "button",
          "nick": "refresh",
          "title": "Refresh Data",
          "type": "string",
          "action": "refresh"
        }
      ]
    },
    {
      "kind": "table",
      "nick": "recent_activities",
      "title": "Recent Activities",
      "dataSource": "/api/data/activities",
      "columns": [
        { "field": "id", "title": "ID" },
        { "field": "name", "title": "Name" },
        { "field": "date", "title": "Date" }
      ]
    }
  ]
}
```

## Best Practices

- Use descriptive and unique `nick` names for components
- Keep page configurations organized by grouping related components
- Use appropriate component types for different use cases
- Include meaningful titles and descriptions
- Use `uuid_page` to uniquely identify pages

## Page Lifecycle

1. Client requests page configuration via `/anx/config?uuid_page={{uuid_page}}`
2. Server returns page configuration
3. Client processes configuration and loads dynamic data
4. Client renders page components
5. User interacts with components
6. Client handles events and updates data

## Data Flow

- Page configuration defines the structure
- Dynamic data is loaded based on `dataSource` properties
- Formulas are evaluated to calculate derived values
- User interactions trigger actions and data updates
