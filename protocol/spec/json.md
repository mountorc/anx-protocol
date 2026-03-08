# JSON 格式规范

## 概述

ANX 系统中使用 JSON 格式来定义页面配置、组件属性、数据结构等。本规范定义了 ANX 系统中 JSON 格式的标准和最佳实践。

## 基本规则

1. **语法规范**：遵循标准 JSON 语法，使用双引号包围字符串，使用逗号分隔键值对
2. **缩进**：使用 2 个空格进行缩进，保持代码可读性
3. **命名规范**：使用小驼峰命名法（camelCase）命名键名
4. **数据类型**：支持 string、number、boolean、array、object、null 等 JSON 标准数据类型
5. **注释**：JSON 本身不支持注释，但可以在配置文件中使用特殊字段（如 "//" 或 "_comment"）添加注释

## 命名规范

| 类型 | 规范 | 示例 |
|------|------|------|
| 键名 | 小驼峰命名法 | `dataSource`、`pageSize` |
| 组件类型 | 小写字母，单词之间用连字符分隔 | `text-input`、`date-picker` |
| ID | 小写字母，单词之间用下划线分隔 | `user_list`、`product_form` |
| 常量 | 全大写，单词之间用下划线分隔 | `MAX_LENGTH`、`DEFAULT_VALUE` |

## 数据类型规范

### 字符串

- 使用双引号包围
- 避免使用多余的转义字符
- 对于包含特殊字符的字符串，使用适当的转义

```json
{
  "name": "示例字符串",
  "url": "https://example.com"
}
```

### 数字

- 整数和浮点数都可以使用
- 避免使用科学计数法（除非必要）
- 对于金额等精确数值，建议使用字符串类型

```json
{
  "count": 100,
  "price": 99.99,
  "amount": "1000.00"
}
```

### 布尔值

- 使用 `true` 或 `false`（小写）
- 避免使用 1/0 或 "true"/"false" 字符串

```json
{
  "enabled": true,
  "required": false
}
```

### 数组

- 数组元素类型应保持一致
- 对于空数组，使用 `[]`
- 数组元素之间用逗号分隔

```json
{
  "items": [1, 2, 3],
  "emptyArray": []
}
```

### 对象

- 对象键值对之间用逗号分隔
- 对于空对象，使用 `{}`
- 对象嵌套不宜过深（建议不超过 4 层）

```json
{
  "user": {
    "name": "张三",
    "age": 30
  },
  "emptyObject": {}
}
```

### Null

- 使用 `null`（小写）表示空值
- 避免使用 undefined 或其他表示空值的方式

```json
{
  "value": null
}
```

## 最佳实践

1. **可读性**：保持适当的缩进和换行，提高代码可读性
2. **一致性**：在整个项目中保持一致的 JSON 格式风格
3. **完整性**：确保 JSON 结构完整，避免缺少必要的字段
4. **验证**：在使用前验证 JSON 格式的正确性
5. **性能**：对于大型 JSON 数据，考虑使用压缩或分段加载

## 示例

### 页面配置示例

```json
{
  "page": {
    "id": "home_page",
    "name": "首页",
    "components": [
      {
        "type": "text-input",
        "id": "search_input",
        "name": "搜索框",
        "placeholder": "请输入搜索内容"
      },
      {
        "type": "list",
        "id": "product_list",
        "name": "产品列表",
        "dataSource": "/api/products",
        "pageSize": 20
      }
    ]
  }
}
```

### 组件配置示例

```json
{
  "type": "form",
  "id": "user_form",
  "name": "用户表单",
  "fields": [
    {
      "name": "username",
      "label": "用户名",
      "type": "string",
      "required": true,
      "placeholder": "请输入用户名",
      "minLength": 3,
      "maxLength": 16,
      "description": "用户的登录名称",
      "validate": {
        "rule": "pattern:^[a-zA-Z0-9_]{3,16}$",
        "message": "用户名长度为 3-16 位，只能包含字母、数字和下划线"
      }
    },
    {
      "name": "email",
      "label": "邮箱",
      "type": "string",
      "required": true,
      "placeholder": "请输入邮箱",
      "minLength": 5,
      "maxLength": 50,
      "description": "用户的电子邮箱",
      "validate": {
        "rule": "email",
        "message": "请输入正确的邮箱格式"
      }
    }
  ],
  "actions": [
    {
      "type": "button",
      "label": "提交",
      "action": "submit",
      "style": {
        "color": "#fff",
        "backgroundColor": "#1890ff"
      }
    }
  ]
}
```

## 工具推荐

1. **JSON 验证器**：使用在线工具如 JSONLint 验证 JSON 格式的正确性
2. **格式化工具**：使用 Prettier 等工具自动格式化 JSON 文件
3. **编辑器插件**：使用 VS Code、Sublime Text 等编辑器的 JSON 插件提高开发效率

## 常见问题

### 语法错误
- 缺少逗号：在键值对或数组元素之间缺少逗号
- 多余的逗号：在对象或数组的最后一个元素后添加了逗号
- 单引号：使用了单引号而不是双引号
- 未定义的变量：使用了 JSON 中不存在的数据类型

### 结构问题
- 嵌套过深：JSON 结构嵌套层次过多，影响可读性和性能
- 字段缺失：缺少必要的字段，导致配置不完整
- 类型错误：字段类型与预期不符

### 性能问题
- 数据过大：JSON 数据过大，影响加载和解析性能
- 重复数据：存在大量重复数据，增加了数据大小