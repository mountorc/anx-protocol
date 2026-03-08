# 列表组件规范

## 概述

列表组件用于展示一系列相关数据项，支持多种布局和交互方式。

## 基本结构

```json
{
  "type": "list",
  "id": "唯一标识符",
  "name": "组件名称",
  "dataSource": "数据来源",
  "template": "列表项模板",
  "layout": "布局方式",
  "pagination": "分页配置",
  "sort": "排序配置",
  "filter": "过滤配置",
  "actions": "操作配置",
  "options": [
    {
      "value": "选项值",
      "label": "选项标签"
    }
  ],
  "style": "样式配置"
}
```

## 字段说明

| 字段名 | 类型 | 必选 | 说明 |
|-------|------|------|------|
| type | string | 是 | 组件类型，固定为 "list" |
| id | string | 是 | 组件唯一标识符 |
| name | string | 否 | 组件名称 |
| dataSource | string/object | 是 | 数据来源，可以是 API 地址或本地数据对象 |
| template | string | 是 | 列表项模板名称 |
| layout | string | 否 | 布局方式，如 "vertical"、"horizontal"、"grid" 等 |
| pagination | object | 否 | 分页配置 |
| sort | object | 否 | 排序配置 |
| filter | object | 否 | 过滤配置 |
| actions | array | 否 | 操作按钮配置 |
| options | array | 否 | 选项配置 |
| style | object | 否 | 样式配置 |

## 分页配置

```json
{
  "enable": true,
  "pageSize": 10,
  "pageIndex": 1,
  "total": 100
}
```

## 排序配置

```json
{
  "field": "sortField",
  "order": "asc"
}
```

## 过滤配置

```json
{
  "conditions": [
    {
      "field": "fieldName",
      "operator": "eq",
      "value": "filterValue"
    }
  ]
}
```

## 操作配置

```json
[
  {
    "type": "button",
    "label": "操作按钮",
    "action": "actionName",
    "params": {
      "key": "value"
    }
  }
]
```

## 示例

### 基本列表

```json
{
  "type": "list",
  "id": "userList",
  "name": "用户列表",
  "dataSource": "/api/users",
  "template": "user-item",
  "layout": "vertical",
  "pagination": {
    "enable": true,
    "pageSize": 20
  }
}
```

### 网格布局列表

```json
{
  "type": "list",
  "id": "productList",
  "name": "产品列表",
  "dataSource": "/api/products",
  "template": "product-card",
  "layout": "grid",
  "style": {
    "gridColumns": "3"
  }
}
```

### 带操作按钮的列表

```json
{
  "type": "list",
  "id": "orderList",
  "name": "订单列表",
  "dataSource": "/api/orders",
  "template": "order-item",
  "actions": [
    {
      "type": "button",
      "label": "查看",
      "action": "viewOrder",
      "params": {
        "orderId": "{{id}}"
      }
    },
    {
      "type": "button",
      "label": "编辑",
      "action": "editOrder",
      "params": {
        "orderId": "{{id}}"
      }
    }
  ]
}
```