# Navigation Configuration Guide

## Overview

In ANX frontend interaction protocol, navigation configuration defines the menu structure for the application, including main menus and submenus.

## Navigation Structure

A typical navigation configuration includes the following structure:

```json
{
  "title": "菜单标题",
  "nick": "菜单nick",
  "uuid_page": "页面UUID",
  "items": [
    {
      "title": "菜单标题",
      "nick": "菜单nick",
      "uuid_page": "页面UUID"
    }
  ]
}
```

## Field Descriptions

| Field | Description | Required |
|-------|-------------|----------|
| `title` | Menu title displayed to users | Yes |
| `nick` | Unique identifier for the menu | Yes |
| `uuid_page` | UUID of the page associated with this menu | Yes |
| `url_page` | URL of the page associated with this menu | No |
| `items` | Array of submenu items | No |

## Submenu Structure

Each submenu item in the `items` array follows the same structure:

```json
{
  "title": "菜单标题",
  "nick": "菜单nick",
  "uuid_page": "页面UUID",
  "url_page": "页面URL"
}
```

## Example Navigation Configuration

```json
{
  "title": "Dashboard",
  "nick": "dashboard",
  "uuid_page": "dashboard_123",
  "url_page": "/dashboard",
  "items": [
    {
      "title": "Overview",
      "nick": "overview",
      "uuid_page": "overview_456",
      "url_page": "/dashboard/overview"
    },
    {
      "title": "Analytics",
      "nick": "analytics",
      "uuid_page": "analytics_789",
      "url_page": "/dashboard/analytics",
      "items": [
        {
          "title": "Sales",
          "nick": "sales",
          "uuid_page": "sales_101",
          "url_page": "/dashboard/analytics/sales"
        },
        {
          "title": "Users",
          "nick": "users",
          "uuid_page": "users_102",
          "url_page": "/dashboard/analytics/users"
        }
      ]
    }
  ]
}
```

## Complete Navigation Example

```json
[
  {
    "title": "Dashboard",
    "nick": "dashboard",
    "uuid_page": "dashboard_123",
    "url_page": "/dashboard"
  },
  {
    "title": "Products",
    "nick": "products",
    "uuid_page": "products_456",
    "url_page": "/products",
    "items": [
      {
        "title": "All Products",
        "nick": "all_products",
        "uuid_page": "all_products_789",
        "url_page": "/products/all"
      },
      {
        "title": "Add Product",
        "nick": "add_product",
        "uuid_page": "add_product_101",
        "url_page": "/products/add"
      }
    ]
  },
  {
    "title": "Settings",
    "nick": "settings",
    "uuid_page": "settings_102",
    "url_page": "/settings",
    "items": [
      {
        "title": "User Settings",
        "nick": "user_settings",
        "uuid_page": "user_settings_103",
        "url_page": "/settings/user"
      },
      {
        "title": "System Settings",
        "nick": "system_settings",
        "uuid_page": "system_settings_104",
        "url_page": "/settings/system"
      }
    ]
  }
]
```

## Best Practices

- Use descriptive and unique `nick` names for menus
- Keep menu structures organized and hierarchical
- Use meaningful `title` values that are clear to users
- Ensure each menu item has a valid `uuid_page`
- Limit the depth of nested submenus for better usability
- Consider using icons for menu items to enhance visual recognition

## Usage in Application

1. Navigation configuration is typically loaded once during application startup
2. The menu structure is rendered based on the configuration
3. Clicking on menu items navigates to the corresponding page using the `uuid_page`
4. Active menu items are highlighted based on the current page
