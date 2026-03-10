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
| `must` | Whether the field is required (true/false) |
| `placeholder` | Placeholder text for input fields |
| `minLength` | Minimum length for string fields |
| `maxLength` | Maximum length for string fields |
| `description` | Description of the field |
| `options` | Array of options for select fields |
| `optionsSet` | Configuration for loading options from a dataset |

## Example

```json
{
  "kinds": [
    {
      "kind": "input",
      "type": "string",
      "nick": "username",
      "title": "Username",
      "defaultValue": "",
      "must": true,
      "placeholder": "请输入用户名",
      "minLength": 3,
      "maxLength": 20,
      "description": "用户的登录名称"
    },
    {
      "kind": "input",
      "type": "number",
      "nick": "age",
      "title": "Age",
      "defaultValue": 18,
      "must": true,
      "minLength": 1,
      "maxLength": 3,
      "description": "用户的年龄"
    },
    {
      "kind": "options",
      "type": "string",
      "nick": "gender",
      "title": "Gender",
      "defaultValue": "male",
      "must": true,
      "description": "用户的性别"
    },
    {
      "kind": "options",
      "type": "string",
      "nick": "category",
      "title": "Category",
      "defaultValue": "",
      "must": true,
      "description": "产品分类",
      "optionsSet": {
        "dataset": {
          "uuid_dataset": "categories_dataset"
        },
        "labelNick": "categoryName",
        "valueNick": "categoryId"
      }
    }
  ]
}
```
