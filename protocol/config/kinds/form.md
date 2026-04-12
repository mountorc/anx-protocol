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

## Formula Calculation and Linkage

### Formula Linkage Mechanism

When an item defines a `formula` field, the following mechanism applies:

1. **Automatic Triggering**: Whenever any field in the form is updated, the system automatically re-evaluates all formulas that depend on the updated field.

2. **Value Assignment**: The calculated result of the formula is automatically assigned to the `value` property of the item.

3. **Dependency Tracking**: The system tracks dependencies between fields to ensure formulas are only re-evaluated when necessary.

### Example

```json
{
  "kinds": [
    {
      "kind": "input",
      "type": "number",
      "nick": "price",
      "title": "Price",
      "defaultValue": 100
    },
    {
      "kind": "input",
      "type": "number",
      "nick": "quantity",
      "title": "Quantity",
      "defaultValue": 2
    },
    {
      "kind": "text",
      "type": "number",
      "nick": "total",
      "title": "Total",
      "formula": "price * quantity"
    }
  ]
}
```

In this example:
- When the `price` or `quantity` field is updated, the `total` field's formula is automatically recalculated
- The result of `price * quantity` is assigned to `total.value`
- The user sees the updated total value immediately

### Formula Syntax

For detailed information about formula syntax and usage, please refer to the [Formula Guide](formula.md).

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
