# HTML Component Guide

## Overview

This guide describes the `html` component in ANX frontend interaction protocol, which is used to display HTML content in the interface.

## Component Structure

The `html` component is defined with `kind: "html"` and supports the following properties:

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `kind`   | string | Yes | Must be "html" to indicate this is an HTML component |
| `title`  | string | No | Optional title for the HTML section |
| `content` | string | Yes | HTML content to display |
| `height` | string | No | Optional height for the HTML container (e.g., "300px") |
| `width`  | string | No | Optional width for the HTML container (e.g., "100%") |
| `styles` | object | No | Optional CSS styles for the HTML container |

## Basic Usage

```json
{
  "kind": "html",
  "content": "<div style='padding: 20px; background-color: #f0f0f0;'>\n  <h2>HTML Content</h2>\n  <p>This is a paragraph of HTML content.</p>\n  <ul>\n    <li>Item 1</li>\n    <li>Item 2</li>\n    <li>Item 3</li>\n  </ul>\n</div>"
}
```

## Example with Title and Dimensions

```json
{
  "kind": "html",
  "title": "Embedded HTML",
  "content": "<div class='custom-content'>\n  <h3>Welcome</h3>\n  <p>Hello, this is custom HTML content.</p>\n</div>",
  "height": "400px",
  "width": "100%"
}
```

## Formula Support

The `html` component supports formula substitution in the `content` property, using the same syntax as the `text` component:

```json
{
  "kind": "html",
  "content": "<div>\n  <h2>Welcome {{user.name}}</h2>\n  <p>Your balance is ${{account.balance}}</p>\n  <p>Today is ${formatDate(date)}</p>\n</div>"
}
```

## Security Considerations

When using the `html` component, consider the following security aspects:

1. **XSS Protection**: Ensure that any user-generated content included in the HTML is properly sanitized to prevent cross-site scripting attacks.

2. **Content Security Policy (CSP)**: If your application implements CSP, ensure that the HTML content complies with the policy.

3. **External Resources**: Be cautious when including external scripts or stylesheets, as they may introduce security risks.

## Best Practices

- Keep HTML content concise and focused
- Use inline styles sparingly; prefer external styles when possible
- Validate HTML content to ensure it's well-formed
- Test HTML content across different browsers to ensure compatibility
- Use formula substitution responsibly, especially with user input

## Performance Considerations

- Complex HTML content may impact rendering performance
- Avoid overly nested HTML structures
- Consider lazy-loading for large HTML content
- Use efficient CSS selectors

## Error Handling

- If the HTML content is invalid, it may not render correctly
- Test HTML content thoroughly to ensure it displays as expected
- Provide fallback content if the HTML fails to render