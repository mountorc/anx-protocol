# 过滤组件规范

## 概述

过滤组件用于对数据进行筛选和过滤，支持多种过滤条件和操作符。

## 基本结构

```json
{
  "type": "filter",
  "id": "唯一标识符",
  "name": "组件名称",
  "fields": [
    {
      "name": "字段名",
      "label": "字段标签",
      "type": "数据类型",
      "operator": "操作符",
      "value": "过滤值",
      "options": [
        {
          "label": "选项标签",
          "value": "选项值"
        }
      ]
    }
  ],
  "logic": "逻辑关系",
  "actions": "操作配置"
}
```

## 字段说明

| 字段名 | 类型 | 必选 | 说明 |
|-------|------|------|------|
| type | string | 是 | 组件类型，固定为 "filter" |
| id | string | 是 | 组件唯一标识符 |
| name | string | 否 | 组件名称 |
| fields | array | 是 | 过滤字段配置 |
| logic | string | 否 | 逻辑关系，如 "and" 或 "or"，默认为 "and" |
| actions | array | 否 | 操作按钮配置 |

## 过滤字段配置

| 字段名 | 类型 | 必选 | 说明 |
|-------|------|------|------|
| name | string | 是 | 字段名，对应数据中的字段 |
| label | string | 是 | 字段标签，用于显示在界面上 |
| type | string | 是 | 数据类型，如 "string"、"number"、"date"、"boolean" 等 |
| operator | string | 是 | 操作符，如 "eq"、"ne"、"gt"、"lt"、"contains" 等 |
| value | any | 否 | 过滤值 |
| options | array | 否 | 选项列表，用于下拉选择等场景 |

## 操作符说明

### 字符串操作符

| 操作符 | 描述 | 示例 |
|-------|------|------|
| eq | 等于 | { "operator": "eq", "value": "test" } |
| ne | 不等于 | { "operator": "ne", "value": "test" } |
| contains | 包含 | { "operator": "contains", "value": "test" } |
| startsWith | 以...开头 | { "operator": "startsWith", "value": "test" } |
| endsWith | 以...结尾 | { "operator": "endsWith", "value": "test" } |
| in | 包含在列表中 | { "operator": "in", "value": ["a", "b", "c"] } |
| notIn | 不包含在列表中 | { "operator": "notIn", "value": ["a", "b", "c"] } |

### 数字操作符

| 操作符 | 描述 | 示例 |
|-------|------|------|
| eq | 等于 | { "operator": "eq", "value": 10 } |
| ne | 不等于 | { "operator": "ne", "value": 10 } |
| gt | 大于 | { "operator": "gt", "value": 10 } |
| lt | 小于 | { "operator": "lt", "value": 10 } |
| gte | 大于等于 | { "operator": "gte", "value": 10 } |
| lte | 小于等于 | { "operator": "lte", "value": 10 } |
| between | 在范围内 | { "operator": "between", "value": [5, 15] } |

### 日期操作符

| 操作符 | 描述 | 示例 |
|-------|------|------|
| eq | 等于 | { "operator": "eq", "value": "2023-01-01" } |
| ne | 不等于 | { "operator": "ne", "value": "2023-01-01" } |
| gt | 大于 | { "operator": "gt", "value": "2023-01-01" } |
| lt | 小于 | { "operator": "lt", "value": "2023-01-01" } |
| gte | 大于等于 | { "operator": "gte", "value": "2023-01-01" } |
| lte | 小于等于 | { "operator": "lte", "value": "2023-01-01" } |
| between | 在范围内 | { "operator": "between", "value": ["2023-01-01", "2023-12-31"] } |

### 布尔操作符

| 操作符 | 描述 | 示例 |
|-------|------|------|
| eq | 等于 | { "operator": "eq", "value": true } |
| ne | 不等于 | { "operator": "ne", "value": true } |

## 操作配置

```json
[
  {
    "type": "button",
    "label": "查询",
    "action": "search",
    "style": {
      "color": "#fff",
      "backgroundColor": "#1890ff"
    }
  },
  {
    "type": "button",
    "label": "重置",
    "action": "reset",
    "style": {
      "color": "#333",
      "backgroundColor": "#fff",
      "border": "1px solid #d9d9d9"
    }
  }
]
```

## 示例

### 基本过滤

```json
{
  "type": "filter",
  "id": "userFilter",
  "name": "用户过滤",
  "fields": [
    {
      "name": "username",
      "label": "用户名",
      "type": "string",
      "operator": "contains",
      "value": ""
    },
    {
      "name": "age",
      "label": "年龄",
      "type": "number",
      "operator": "between",
      "value": [18, 60]
    }
  ],
  "actions": [
    {
      "type": "button",
      "label": "查询",
      "action": "search"
    },
    {
      "type": "button",
      "label": "重置",
      "action": "reset"
    }
  ]
}
```

### 高级过滤

```json
{
  "type": "filter",
  "id": "orderFilter",
  "name": "订单过滤",
  "fields": [
    {
      "name": "orderStatus",
      "label": "订单状态",
      "type": "string",
      "operator": "in",
      "options": [
        { "label": "待支付", "value": "pending" },
        { "label": "已支付", "value": "paid" },
        { "label": "已发货", "value": "shipped" },
        { "label": "已完成", "value": "completed" }
      ],
      "value": []
    },
    {
      "name": "orderDate",
      "label": "订单日期",
      "type": "date",
      "operator": "between",
      "value": []
    },
    {
      "name": "amount",
      "label": "订单金额",
      "type": "number",
      "operator": "gte",
      "value": 0
    }
  ],
  "logic": "and",
  "actions": [
    {
      "type": "button",
      "label": "查询",
      "action": "search"
    },
    {
      "type": "button",
      "label": "重置",
      "action": "reset"
    }
  ]
}
```

### 动态过滤

```json
{
  "type": "filter",
  "id": "productFilter",
  "name": "产品过滤",
  "fields": [
    {
      "name": "category",
      "label": "产品分类",
      "type": "string",
      "operator": "eq",
      "options": [],
      "value": "",
      "dataSource": "/api/categories"
    },
    {
      "name": "price",
      "label": "价格范围",
      "type": "number",
      "operator": "between",
      "value": [0, 1000]
    },
    {
      "name": "inStock",
      "label": "是否有库存",
      "type": "boolean",
      "operator": "eq",
      "value": true
    }
  ],
  "actions": [
    {
      "type": "button",
      "label": "查询",
      "action": "search"
    }
  ]
}
```