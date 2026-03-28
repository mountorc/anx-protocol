# How to Operate ANX Card Nodes

## Overview

This guide provides detailed instructions on how to operate ANX Card Nodes using the ANX Card Node format (`<x kind cardKey>`) and ANX CLI commands.

## Card Node Format

### Basic Structure

The ANX Card Node format uses the `<x>` tag with two required attributes:

```html
<x kind cardKey>
  Content area
</x>
```

- **kind**: Specifies the component type (e.g., form, input, button, options, checkbox, etc.)
- **cardKey**: Unique identifier for the component, used for CLI commands

### Component Types

Common component types include:

| Component Type | Description |
|----------------|-------------|
| form | Form container |
| input | Text input field |
| date | Date picker |
| options | Dropdown/radio selection |
| checkbox | Multiple selection |
| textarea | Multi-line text input |
| button | Action button |
| text | Non-editable text label (no set/input operations needed) |
| list | Table/list display |

## CLI Commands

### Basic Format

```bash
anx <cardKey> <action> <params>
```

- **cardKey**: The unique identifier of the component
- **action**: The action to perform
- **params**: Parameters for the action (usually JSON format)

### Common Actions

| Action | Description | Parameters |
|--------|-------------|------------|
| get_form | Get entire form data | N/A |
| set_form | Set form data | `{"field1": "value1", "field2": "value2"}` |
| get_value | Get field value | N/A |
| set_value | Set field value | `{"value": "new value"}` |
| tap | Trigger button click | N/A |

## Field Value Formats

### Text Fields

```json
{"value": "text value"}
```

### Number Fields

```json
{"value": 123}
```

### Date Fields

```json
{"value": "2023-12-31"}
```

### Options (Single Selection)

```json
{"value": "option_value"}
```

### Checkbox (Multiple Selection)

```json
{"value": ["option1", "option2"]}
```

### List Fields

```json
{"value": [{"field1": "value1", "field2": "value2"}]}
```

## Usage Examples

### Get Form Data

```bash
anx form_card_key get_form
```

### Set Form Data

```bash
anx form_card_key set_form '{"username": "user1", "email": "user1@example.com"}'
```

### Update Field Value

```bash
anx input_card_key set_value '{"value": "new value"}'
```

### Trigger Button

```bash
anx button_card_key tap
```

## Best Practices

1. **CardKey Naming**: Use descriptive and unique cardKeys
2. **Data Validation**: Validate data before setting
3. **Error Handling**: Handle errors gracefully
4. **Consistency**: Maintain consistent form structure
5. **Documentation**: Document cardKeys for team collaboration

## Troubleshooting

### Common Issues

- **Invalid cardKey**: Verify the cardKey is correct
- **Incorrect format**: Ensure data matches expected format
- **Component not found**: Check component registration

### Debugging Tips

- Use `get_form` to check current form state
- Test with simple values first
- Check console logs for errors
- Verify component types and cardKeys
