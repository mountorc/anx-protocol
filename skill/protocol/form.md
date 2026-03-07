# Form Configuration Guide

## Form Structure

In ANX frontend interaction protocol, a form configuration typically includes the following structure:

```json
{
  "kinds": [
    {
      "kind": "组件类型",
      "type": "数据格式",
      "nick": "字段名",
      "title": "显示名",
      "formula": "计算公式",
      "defaultValue": "默认值"
    }
  ]
}
```

## Field Descriptions

| Field | Description |
|-------|-------------|
| `kinds` | Array of form items/components |
| `kind` | Component type (e.g., input, textarea, options, checkbox, button, text, table, box, form, json, list) |
| `type` | Data format (e.g., string, number, boolean, date, array, object) |
| `nick` | Field name (used for data binding and submission) |
| `title` | Display name (shown to users) |
| `formula` | Calculation formula (if the field value is derived from other fields) |
| `defaultValue` | Default value for the field |

## Example

```json
{
  "kinds": [
    {
      "kind": "input",
      "type": "string",
      "nick": "username",
      "title": "Username",
      "defaultValue": ""
    },
    {
      "kind": "input",
      "type": "number",
      "nick": "age",
      "title": "Age",
      "defaultValue": 18
    },
    {
      "kind": "options",
      "type": "string",
      "nick": "gender",
      "title": "Gender",
      "defaultValue": "male"
    }
  ]
}
```
