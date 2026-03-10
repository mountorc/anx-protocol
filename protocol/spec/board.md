# 面板组件规范

## 概述

面板组件（board）用于将多个组件组合在一起，形成一个整体的内容区域。

## 基本结构

```json
{
  "kind": "board",
  "kinds": [
    {
      "kind": "组件类型"
    }
  ]
}
```

## 字段说明

| 字段名 | 类型 | 必选 | 说明 |
|-------|------|------|------|
| kind | string | 是 | 组件类型，固定为 "board" |
| kinds | array | 是 | 子组件列表，包含多个组件配置 |

## 示例

### 基本面板

```json
{
  "kind": "board",
  "kinds": [
    {
      "kind": "text",
      "value": "欢迎使用 ANX 系统"
    },
    {
      "kind": "input",
      "placeholder": "请输入内容"
    }
  ]
}
```

### 包含多个组件的面板

```json
{
  "kind": "board",
  "kinds": [
    {
      "kind": "text",
      "value": "用户信息"
    },
    {
      "kind": "input",
      "placeholder": "请输入姓名"
    },
    {
      "kind": "input",
      "placeholder": "请输入邮箱"
    },
    {
      "kind": "button",
      "label": "提交"
    }
  ]
}
```

### 嵌套面板

```json
{
  "kind": "board",
  "kinds": [
    {
      "kind": "board",
      "kinds": [
        {
          "kind": "text",
          "value": "左侧面板"
        }
      ]
    },
    {
      "kind": "board",
      "kinds": [
        {
          "kind": "text",
          "value": "右侧面板"
        }
      ]
    }
  ]
}
```