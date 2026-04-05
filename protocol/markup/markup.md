# ANX Markup Format

## Overview

ANX markup format is a lightweight XML-like syntax used to define card nodes in ANX protocol. It provides a concise way to specify card components with their properties and actions.

## Syntax

ANX markup uses a compact syntax format:

```xml
<x cardKind cardKey tap="actionName">Content</x>
```

### Attributes

- **cardKind**: Directly specifies the card type as an attribute (e.g., "button", "input", "text", "form", etc.)
- **cardKey**: Directly specifies the unique identifier as an attribute value. This is typically a globally unique key generated during card node initialization.
- **tap**: Optional attribute that defines the action to be triggered when the card is tapped/clicked
- **Other attributes**: Additional attributes can be added as needed for specific card types

## Examples

### Basic Button

```xml
<x button submitBtn tap="submitForm">Submit</x>
```

### Input Field

```xml
<x input nameField placeholder="Enter your name"></x>
```

### Text Display

```xml
<x text welcomeText>Welcome to ANX Protocol!</x>
```

### Form Example

```xml
<x form card_123>Form content</x>
```

## Usage Guidelines

1. **Card Key**: Always use unique identifiers to ensure proper identification and state management. These keys are typically generated randomly during card node initialization and should be globally unique.
2. **Card Type**: Use valid card kinds as defined in the ANX protocol specification, directly as an attribute
3. **Tap Actions**: Define tap actions that correspond to existing trigger functions in your application
4. **Content**: For cards that support text content, place it between the opening and closing tags
5. **Syntax Consistency**: Use the compact syntax consistently throughout your codebase

## Integration

ANX markup can be used in various contexts:

- **Markdown Blocks**: Embed markup within ANX markdown blocks
- **Configuration Files**: Use markup syntax in ANX configuration files
- **API Responses**: Return markup-formatted content from ANX APIs

## Parsing

When parsing ANX markup, follow these steps:

1. Identify the opening `<x>` tag
2. Extract the attributes:
   - Look for the card type directly as an attribute, followed by the cardKey
3. Extract other attributes like `tap`, etc.
4. The second attribute is the cardKey
5. Parse the content between the tags (if any)
6. Create the corresponding card component with the extracted properties

## Best Practices

- Keep markup concise and focused
- Use consistent naming conventions for cardKey values (e.g., using camelCase or snake_case)
- Document complex markup structures
- Test markup parsing thoroughly to ensure compatibility
- Use the compact syntax consistently for all card nodes
- Keep attribute names and values concise and meaningful

## Related Documents

- [spec/kinds.md](spec/kinds.md) - Defines all supported card kinds
- [spec/utils/trigger-and-tap.md](spec/utils/trigger-and-tap.md) - Details on tap actions and triggers
