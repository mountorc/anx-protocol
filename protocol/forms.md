# ANX 协议 4 类标准形式

ANX 协议采用**一核多体、各司其职、相互配合**的设计思路，专为 AI Agent 理解与执行优化，并非只使用单一结构。

其中 **ANX Config 形式**为协议核心，承载最完整的结构定义与配置信息，是构建 ANX 应用、SOP、小程序等场景的基础与关键。

围绕这一核心，协议延伸出四类标准形式，分别面向不同环节协同工作：

| 形式 | 职责 | 适用场景 |
|------|------|----------|
| **CLI 形式** | 运行时指令执行 | 命令行交互、自动化脚本 |
| **Config 形式** | 应用与流程配置 | 应用定义、页面配置、SOP |
| **Markdown 块形式** | 人与 Agent 对话中的可视化交互 | 文档嵌入、对话渲染 |
| **Card 节点形式** | 向 AI 清晰呈现应用当前状态与页面结构 | AI 理解、状态展示 |

多形式设计的目的是让协议在**构建配置、运行执行、可视化对话、AI 理解**等全流程中都能自然适配、各司其职，既保证底层逻辑统一，又能在不同场景下高效可用。

---

## 1. ANX Config 形式

用于 AI 原生应用、SOP、小程序的配置描述。

### 关键特征

在 JSON 结构中，`kind`、`kinds` 或 `autoSet` 是 ANX 配置的关键字段，常见于 ANX APP、SOP 等场景。

### 使用格式

```json
{
  "kind": "form",
  "kinds": [],
  "autoSet": {}
}
```

### 相关文档

- [协议核心规范](./spec/main.md) - ANX 协议主文档
- [组件类型定义](./spec/kinds.md) - 所有 kind 类型的定义
- [页面配置](./spec/kinds/page.md) - 页面级别的配置
- [表单配置](./spec/kinds/form.md) - 表单组件配置
- [表格配置](./spec/kinds/table.md) - 表格组件配置

---

## 2. ANX Markdown 块形式

用于在 Markdown 中进行模块声明、渲染展示与可视化交互。

### 关键特征

在 Markdown 里，通过 `:::anx` 声明一个 ANX 可视化块，由 Marked-ANX 负责解析、渲染与交互。

### 使用格式

```markdown
:::anx
{
  "kind": "form"
}
:::
```

### 开源实现

开源项目 [marked-anx](https://github.com/mountorc/marked-anx) 插件已完整实现 `:::anx` 的解析与可视化渲染逻辑。

### 相关文档

- [Markdown 组件](./spec/kinds/markdown.md) - Markdown 内容显示
- [HTML 组件](./spec/kinds/html.md) - HTML 内容嵌入

---

## 3. ANX Card 节点形式

用于在任意文本中标记可交互节点，标识一个 ANX 执行单元。

### 关键特征

在 Markdown 或页面中，`<x>` 是 ANX 标签的标志性标记，出现 `<x>` 即代表使用 ANX 协议声明节点结构。

同时，`cardKey` 字段是 ANX 节点的重要标准，也是区分 ANX Config 与 ANX Card 的关键标识。

### 使用格式

**基础结构：**
```html
<x kind cardKey>
  内容区域
</x>
```

**示例：**
```html
<x form card_1234>
  表单区域
</x>
```

### 相关文档

- [Box 组件](./spec/kinds/box.md) - 容器组件，类似 Card 概念
- [Board 组件](./spec/kinds/board.md) - 面板组件，包含多个 kind

---

## 4. ANX CLI 形式

用于在 ANX 应用运行环境中执行命令、进行交互控制。

### 关键特征

在生产与执行环境中，以 `anx` 开头的命令即为 ANX CLI 命令，遵循 ANX 协议 CLI 命令集定义。

### 使用格式

**通用格式：**
```bash
anx <cardKey> <action> params
```

**示例：**
```bash
# 获取指定 card 的表单信息
anx card_1234 get_form

# 为指定 card 的表单写入数据
anx card_1234 set_form '{"username":"kevin"}'
```

### 相关文档

- [CLI 命令指南](./runtime/cli.md) - ANX CLI 命令详细说明

---

## 形式对比

| 特性 | Config | Markdown 块 | Card 节点 | CLI |
|------|--------|-------------|-----------|-----|
| **格式** | JSON | `:::anx` 代码块 | `<x>` 标签 | 命令行 |
| **用途** | 配置定义 | 可视化渲染 | 状态标记 | 执行控制 |
| **场景** | 应用/SOP 定义 | 文档/对话 | AI 理解 | 运行时 |
| **关键字段** | `kind`, `kinds` | `:::anx` | `cardKey` | `anx` 命令 |

---

## 快速导航

根据你的使用场景，选择合适的形式：

- **构建应用或 SOP** → 使用 [Config 形式](./spec/main.md)
- **在文档中嵌入交互模块** → 使用 [Markdown 块形式](#2-anx-markdown-块形式)
- **让 AI 理解页面结构** → 使用 [Card 节点形式](#3-anx-card-节点形式)
- **命令行控制 ANX 应用** → 使用 [CLI 形式](./runtime/cli.md)

---

## 官方资源

- **ANX 协议官方仓库**: https://github.com/mountorc/anx-protocol
- **marked-anx 插件**: https://github.com/mountorc/marked-anx
- **anx-core 核心库**: https://github.com/mountorc/anx-core

更多形式与场景化能力正在持续迭代中，欢迎关注与共建！
