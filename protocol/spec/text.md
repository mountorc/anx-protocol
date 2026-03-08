# 文本组件规范

## 概述

文本组件用于显示静态或动态文本内容，支持变量替换和格式化。

## 基本结构

```json
{
  "type": "text",
  "id": "唯一标识符",
  "name": "组件名称",
  "content": "文本内容",
  "format": "格式化方式",
  "style": "样式配置"
}
```

## 字段说明

| 字段名 | 类型 | 必选 | 说明 |
|-------|------|------|------|
| type | string | 是 | 组件类型，固定为 "text" |
| id | string | 是 | 组件唯一标识符 |
| name | string | 否 | 组件名称 |
| content | string | 是 | 文本内容，支持变量替换 |
| format | string | 否 | 格式化方式，如 "plain"、"html"、"markdown" 等 |
| style | object | 否 | 样式配置 |

## 变量替换

文本组件支持两种变量替换方式：

1. **双大括号语法**：`{{变量名}}`
2. **美元符号语法**：`${变量名}`

### 示例

```json
{
  "type": "text",
  "id": "greeting",
  "name": "问候语",
  "content": "Hello, {{nick1}}! Welcome, ${nick2}!"
}
```

在上面的示例中，`{{nick1}}` 会被替换为变量 `nick1` 的值，`${nick2}` 会被替换为变量 `nick2` 的值。

## 格式化方式

| 格式化方式 | 描述 | 示例 |
|-----------|------|------|
| plain | 纯文本，不进行任何格式化 | "Hello, world!" |
| html | HTML 格式，支持 HTML 标签 | "<b>Hello</b>, world!" |
| markdown | Markdown 格式，支持 Markdown 语法 | "**Hello**, world!" |

## 样式配置

```json
{
  "style": {
    "color": "#333",
    "fontSize": "14px",
    "fontWeight": "normal",
    "textAlign": "left",
    "margin": "10px 0"
  }
}
```

## 示例

### 基本文本

```json
{
  "type": "text",
  "id": "welcomeText",
  "name": "欢迎文本",
  "content": "欢迎来到 ANX 系统！"
}
```

### 带变量的文本

```json
{
  "type": "text",
  "id": "userGreeting",
  "name": "用户问候",
  "content": "你好，{{username}}！今天是 ${date}，祝你有愉快的一天！"
}
```

### HTML 格式文本

```json
{
  "type": "text",
  "id": "formattedText",
  "name": "格式化文本",
  "content": "<h1>标题</h1><p>这是一段 <b>粗体</b> 文本，<i>斜体</i> 文本，以及 <a href='https://example.com'>链接</a>。</p>",
  "format": "html"
}
```

### Markdown 格式文本

```json
{
  "type": "text",
  "id": "markdownText",
  "name": "Markdown 文本",
  "content": "# 标题\n\n这是一段 **粗体** 文本，*斜体* 文本，以及 [链接](https://example.com)。",
  "format": "markdown"
}
```

### 带样式的文本

```json
{
  "type": "text",
  "id": "styledText",
  "name": "带样式的文本",
  "content": "这是一段带样式的文本",
  "style": {
    "color": "#1890ff",
    "fontSize": "16px",
    "fontWeight": "bold",
    "textAlign": "center",
    "margin": "20px 0"
  }
}
```