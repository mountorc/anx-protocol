# 选项配置

## 概述

ANX 系统中的选项配置用于定义组件的可配置属性，提供灵活的参数设置能力。

## 基本结构

选项配置的基本结构如下：

```json
{
  "type": "数据类型",
  "default": "默认值",
  "must": false,
  "options": [
    {
      "title": "选项标签",
      "value": "选项值"
    }
  ],
  "validate": {
    "rule": "验证规则",
    "message": "验证失败提示"
  }
}
```

## 字段说明

### 基本字段

| 字段名 | 类型 | 必选 | 描述 |
|-------|------|------|------|
| type | string | 是 | 数据类型，如 string、number、boolean、array、object 等 |
| default | any | 否 | 默认值 |
| must | boolean | 否 | 是否必填，默认为 false |
| options | array | 否 | 选项列表，用于下拉选择等场景，每个选项包含 title（显示值）和 value（真实值）字段 |
| optionsSet | object | 否 | 从数据集加载选项的配置 |
| validate | object | 否 | 验证规则配置 |

## options 字段详细说明

### 基本概念

`options` 字段用于定义下拉选择、单选按钮等组件的可选项列表。它是一个数组，每个元素是一个包含 `title` 和 `value` 字段的对象：

- **title**: 显示值，用户在界面上看到的文本
- **value**: 真实值，系统内部使用的值

### 使用场景

`options` 字段主要用于以下场景：

1. **下拉选择框**: 提供多个选项供用户选择
2. **单选按钮组**: 显示一组互斥的选项
3. **枚举类型输入**: 限制用户输入为预定义的值

### 与 type 字段的配合

`options` 字段通常与 `type: "enum"` 配合使用，以明确表示这是一个枚举类型的输入：

```json
{
  "type": "enum",
  "default": "option1",
  "options": [
    { "title": "选项一", "value": "option1" },
    { "title": "选项二", "value": "option2" },
    { "title": "选项三", "value": "option3" }
  ]
}
```

### 高级用法

#### 1. 不同类型的 value

`value` 字段可以是任何类型，不仅限于字符串：

```json
{
  "type": "enum",
  "default": 1,
  "options": [
    { "title": "选项一", "value": 1 },
    { "title": "选项二", "value": 2 },
    { "title": "选项三", "value": 3 }
  ]
}
```

#### 2. 空值选项

可以添加一个空值选项，允许用户选择"无"或"请选择"：

```json
{
  "type": "enum",
  "default": "",
  "options": [
    { "title": "请选择", "value": "" },
    { "title": "选项一", "value": "option1" },
    { "title": "选项二", "value": "option2" }
  ]
}
```

#### 3. 分组选项

对于大量选项，可以使用分组结构：

```json
{
  "type": "enum",
  "default": "option1",
  "options": [
    {
      "group": "第一组",
      "items": [
        { "title": "选项一", "value": "option1" },
        { "title": "选项二", "value": "option2" }
      ]
    },
    {
      "group": "第二组",
      "items": [
        { "title": "选项三", "value": "option3" },
        { "title": "选项四", "value": "option4" }
      ]
    }
  ]
}
```

### 最佳实践

1. **保持简洁**: 选项数量不宜过多，一般不超过10个
2. **明确命名**: title 应该清晰易懂，value 应该简洁明确
3. **默认值**: 为枚举类型设置合理的默认值
4. **一致性**: 在整个系统中保持选项的命名和值的一致性
5. **国际化**: 如果支持多语言，title 应该支持国际化

### 与 optionsSet 的区别

- **options**: 静态定义的选项列表，直接在配置中指定
- **optionsSet**: 从数据集动态加载的选项列表，通过 uuid_dataset 引用外部数据

根据具体需求选择合适的方式：
- 如果选项固定不变，使用 `options`
- 如果选项需要从外部数据源获取，使用 `optionsSet`

### optionsSet 字段说明

| 字段名 | 类型 | 必选 | 描述 |
|-------|------|------|------|
| dataset | object | 是 | 数据集配置，包含 uuid_dataset 字段 |
| titleNick | string | 是 | 数据集中作为选项显示名的字段 |
| valueNick | string | 是 | 数据集中作为选项值的字段 |

### 数据类型

| 类型 | 描述 | 示例 |
|------|------|------|
| string | 字符串类型 | "text" |
| number | 数字类型 | 123 |
| boolean | 布尔类型 | true |
| array | 数组类型 | [1, 2, 3] |
| object | 对象类型 | { "key": "value" } |
| enum | 枚举类型 | 需要配合 options 字段使用 |

### 验证规则

| 规则 | 描述 | 示例 |
|------|------|------|
| required | 必填验证 | { "rule": "required", "message": "此项为必填项" } |
| min | 最小值验证 | { "rule": "min:10", "message": "最小值为 10" } |
| max | 最大值验证 | { "rule": "max:100", "message": "最大值为 100" } |
| pattern | 正则表达式验证 | { "rule": "pattern:^\\d+$", "message": "请输入数字" } |
| email | 邮箱格式验证 | { "rule": "email", "message": "请输入正确的邮箱格式" } |

## 示例

### 文本输入选项

```json
{
  "type": "string",
  "default": "默认标题",
  "must": true
}
```

### 数字输入选项

```json
{
  "type": "number",
  "default": 10,
  "validate": {
    "rule": "min:1",
    "message": "数量至少为 1"
  }
}
```

### 布尔选项

```json
{
  "type": "boolean",
  "default": true
}
```

### 下拉选择选项

```json
{
  "type": "enum",
  "default": "active",
  "options": [
    { "title": "激活", "value": "active" }, // title: 显示值，value: 真实值
    { "title": "禁用", "value": "inactive" }, // title: 显示值，value: 真实值
    { "title": "删除", "value": "deleted" } // title: 显示值，value: 真实值
  ]
}
```

### 从数据集加载选项

```json
{
  "type": "enum",
  "default": "",
  "optionsSet": {
    "dataset": {
      "uuid_dataset": "categories_dataset"
    },
    "titleNick": "categoryName",
    "valueNick": "categoryId"
  }
}
```

### 数组选项

```json
{
  "type": "array",
  "default": []
}
```

### 对象选项

```json
{
  "type": "object",
  "default": {
    "color": "#000",
    "fontSize": "14px"
  }
}
```