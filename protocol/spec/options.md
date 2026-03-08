# 选项配置

## 概述

ANX 系统中的选项配置用于定义组件的可配置属性，提供灵活的参数设置能力。

## 基本结构

选项配置的基本结构如下：

```json
{
  "name": "选项名称",
  "label": "选项标签",
  "type": "数据类型",
  "default": "默认值",
  "required": false,
  "description": "选项描述",
  "options": [
    {
      "label": "选项标签",
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
| name | string | 是 | 选项名称，用于标识选项 |
| label | string | 是 | 选项标签，用于显示在界面上 |
| type | string | 是 | 数据类型，如 string、number、boolean、array、object 等 |
| default | any | 否 | 默认值 |
| required | boolean | 否 | 是否必填，默认为 false |
| description | string | 否 | 选项描述，用于说明选项的用途 |
| options | array | 否 | 选项列表，用于下拉选择等场景 |
| validate | object | 否 | 验证规则配置 |

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
  "name": "title",
  "label": "标题",
  "type": "string",
  "default": "默认标题",
  "required": true,
  "description": "页面标题"
}
```

### 数字输入选项

```json
{
  "name": "count",
  "label": "数量",
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
  "name": "enabled",
  "label": "启用",
  "type": "boolean",
  "default": true
}
```

### 下拉选择选项

```json
{
  "name": "status",
  "label": "状态",
  "type": "enum",
  "default": "active",
  "options": [
    { "label": "激活", "value": "active" },
    { "label": "禁用", "value": "inactive" },
    { "label": "删除", "value": "deleted" }
  ]
}
```

### 数组选项

```json
{
  "name": "tags",
  "label": "标签",
  "type": "array",
  "default": [],
  "description": "页面标签列表"
}
```

### 对象选项

```json
{
  "name": "style",
  "label": "样式",
  "type": "object",
  "default": {
    "color": "#000",
    "fontSize": "14px"
  },
  "description": "组件样式配置"
}
```