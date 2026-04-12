# Markdown 组件规范

## 概述

Markdown 组件用于显示和编辑 Markdown 格式的内容，支持 Markdown 语法解析和渲染。

## 基本结构

```json
{
  "kind": "markdown",
  "content": "Markdown 内容",
  "editable": false,
  "style": "样式配置"
}
```

## 字段说明

| 字段名 | 类型 | 必选 | 说明 |
|-------|------|------|------|
| kind | string | 是 | 组件类型，固定为 "markdown" |
| content | string | 否 | Markdown 内容 |
| editable | boolean | 否 | 是否可编辑，默认为 false |
| style | object | 否 | 样式配置 |

## 示例

### 静态 Markdown 显示

```json
{
  "kind": "markdown",
  "content": "# 标题\n\n这是一段 **粗体** 文本，*斜体* 文本，以及 [链接](https://example.com)。\n\n- 列表项 1\n- 列表项 2\n- 列表项 3"
}
```

### 可编辑的 Markdown

```json
{
  "kind": "markdown",
  "content": "# 编辑 Markdown\n\n在此输入 Markdown 内容...",
  "editable": true
}
```

### 带样式的 Markdown

```json
{
  "kind": "markdown",
  "content": "# 带样式的 Markdown\n\n这是一段带样式的 Markdown 内容。",
  "style": {
    "color": "#333",
    "fontSize": "14px",
    "lineHeight": "1.5"
  }
}
```