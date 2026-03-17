# Style Configuration Guide

## Overview

This guide describes how to configure styles in ANX frontend interaction protocol, supporting both JSON format and text format for CSS styles.

## Style Formats

ANX supports two formats for style configuration:

1. **JSON format**: Object-based style configuration
2. **Text format**: String-based CSS style configuration

## JSON Format

The JSON format uses a JavaScript object to define styles, similar to React's inline styles. This format is recommended for most use cases due to its structured nature and ease of manipulation.

### Basic Usage

```json
{
  "style": {
    "color": "#333",
    "fontSize": "14px",
    "lineHeight": "1.5",
    "padding": "10px",
    "backgroundColor": "#f5f5f5"
  }
}
```

### Common Style Properties

| Property | Description | Example Value |
|----------|-------------|---------------|
| `color` | Text color | "#333", "red" |
| `fontSize` | Font size | "14px", "1.2em" |
| `fontFamily` | Font family | "Arial, sans-serif" |
| `fontWeight` | Font weight | "normal", "bold", "600" |
| `lineHeight` | Line height | "1.5", "24px" |
| `textAlign` | Text alignment | "left", "center", "right" |
| `margin` | Margin | "10px", "10px 20px" |
| `padding` | Padding | "10px", "10px 20px" |
| `backgroundColor` | Background color | "#f5f5f5", "white" |
| `border` | Border | "1px solid #ddd" |
| `borderRadius` | Border radius | "4px", "50%" |
| `width` | Width | "100%", "300px" |
| `height` | Height | "200px", "auto" |
| `display` | Display type | "block", "inline", "flex" |
| `flexDirection` | Flex direction | "row", "column" |
| `justifyContent` | Justify content | "flex-start", "center", "space-between" |
| `alignItems` | Align items | "flex-start", "center", "stretch" |

## Text Format

The text format uses a CSS string to define styles, similar to traditional CSS. This format is useful for more complex styles or when you want to use CSS features not easily expressed in JSON format.

### Basic Usage

```json
{
  "style": "color: #333; font-size: 14px; line-height: 1.5; padding: 10px; background-color: #f5f5f5;"
}
```

### Example with Complex Styles

```json
{
  "style": "color: #333; font-size: 14px; line-height: 1.5; padding: 10px; background-color: #f5f5f5; border: 1px solid #ddd; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"
}
```

## Usage in Components

Styles can be applied to most components in ANX protocol. Here are examples of how to use styles in different components:

### Text Component

```json
{
  "kind": "text",
  "content": "Hello, world!",
  "style": {
    "color": "#333",
    "fontSize": "16px",
    "fontWeight": "bold"
  }
}
```

### HTML Component

```json
{
  "kind": "html",
  "content": "<div>HTML content</div>",
  "style": "color: #333; font-size: 14px; line-height: 1.5;"
}
```

### Markdown Component

```json
{
  "kind": "markdown",
  "value": "# Markdown content",
  "style": {
    "color": "#333",
    "fontSize": "14px",
    "lineHeight": "1.5"
  }
}
```

## Formula Support

Styles can also use formula substitution, similar to other properties in ANX protocol:

```json
{
  "style": {
    "color": "{{isError ? '#ff0000' : '#333'}}",
    "fontSize": "{{user.preferences.fontSize}}px"
  }
}
```

## Best Practices

- Use JSON format for most use cases, as it's more structured and easier to manipulate
- Use text format for complex styles or when you need to use CSS features not easily expressed in JSON
- Keep styles consistent across components
- Use descriptive variable names when using formulas in styles
- Test styles across different browsers to ensure compatibility

## Performance Considerations

- Avoid overly complex styles, as they may impact rendering performance
- Use CSS variables for repeated values
- Consider using a style preprocessor if you have many styles
- Test styles on different devices to ensure responsive design

## Error Handling

- If a style property is invalid, it will typically be ignored
- Test styles thoroughly to ensure they display as expected
- Use browser developer tools to debug style issues