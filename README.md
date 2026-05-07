# ANX: AI Native eX Protocol

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![arXiv](https://img.shields.io/badge/arXiv-2604.04820-orange)](https://arxiv.org/abs/2604.04820)

## What is ANX?

**ANX (AI Native eX)** 是一个对 Agent 友好的前端编码格式，旨在建立统一标准，打破传统上 Agent 必须使用浏览器或应用程序来浏览网页或使用应用的场景。

ANX 提供四种标准形式：
- **CLI**: 命令行接口形式
- **Config**: 配置文件形式
- **Markdown Block**: Markdown 嵌入形式
- **Card Node**: 卡片节点形式

详细技术规范请参阅 [ANX 协议文档](./protocol/catalog.md)。

---

## 📖 Research Foundation | 论文理论支撑

ANX 协议的设计基于学术研究，其核心理念和技术规范在以下论文中有详细阐述：

**Paper**: [ANX: Protocol-First Design for AI Agent Interaction with a Supporting 3EX Decoupled Architecture](https://arxiv.org/abs/2604.04820)

**Authors**: Xu Mingze (Hangzhou Ziyou Data Technology Co., Ltd.)

### Why Read the Paper?

ANX 协议的设计融入了以下论文中的核心理论：

1. **Agent-Native Design Philosophy | Agent 原生设计理念**
   - 传统 GUI 自动化存在高 token 消耗、DOM 脆弱性问题
   - ANX 采用结构化编码（ANX Markup），信息密度高，显著降低 token 消耗
   - 实验数据：相比 MCP 减少 47.3%-55.6% token，相比 GUI 自动化减少 57.1%-66.3% token

2. **Human-Agent Shared Interaction | 人机共享交互**
   - 同一 ANX 定义可同时渲染为 Agent 可执行指令和人类可读界面
   - 开发一次，处处使用，消除人机交互碎片化

3. **3EX Architecture | 三层架构**
   - **Expression Layer**: 任务规范层（ANX Markup）
   - **Exchange Layer**: 交换层（ANXHub 动态应用市场）
   - **Execution Layer**: 执行层（ANX Core、CLI、Nodes）
   - 三层解耦设计降低 Agent 认知负担，提高执行效率

4. **Security by Design | 原生安全**
   - **UI-to-Core 隔离**: 敏感数据绕过 LLM 上下文，确保数据隔离
   - **Human-Only 确认**: 确认操作无法被委托给 Agent，防止自动化滥用

5. **Machine-Executable SOP | 机器可执行 SOP**
   - 结构化 ANX Markup 消除自然语言歧义
   - 支持可靠的长时域任务执行和多 Agent 协作

### Quick Links

- [View Full Paper (PDF)](https://arxiv.org/pdf/2604.04820)
- [View HTML Version](https://arxiv.org/html/2604.04820v1)
- [Cite as]: `arXiv:2604.04820 [cs.AI]`

### How to Navigate This README

- **For Protocol Implementation**: Start with [Key Features](#key-features) below
- **For Design Philosophy**: Read the [Research Foundation](#-research-foundation--论文理论支撑) section above
- **For Technical Specs**: Refer to [/protocol](./protocol/catalog.md)

---

## Key Features

ANX Frontend Interaction Protocol is a unified frontend coding standard designed specifically for Agents, with the following key features:

### 1. Unified Interaction Standard

Establishes a unified standard for Agent-frontend application interaction, breaking the traditional limitation where Agents must use browsers or applications.

**Theoretical Foundation**: Paper Section 1.1 - Background discusses why existing GUI-centric approaches are insufficient for agents.

### 2. Navigation Configuration

- Defines menu structures and submenus
- Supports page navigation and parameter passing
- Provides complete navigation examples (such as shopping website menus)

### 3. Event Handling

- Supports multiple trigger types: input, focus, blur, submit, tap, longtap, doubletap, cancel, clear
- Supports multiple action types: navigateTo, navigateToBack, updateData, setTimeout, requestSet
- Provides simplified tap event configuration

**Theoretical Foundation**: These design patterns support the "Create-on-Demand, Use-and-Go" principle from Paper Section 3.1.3.

### 4. Data Operations

- Intelligent data update based on unique identifiers (update if exists, insert if not)
- Supports field mapping configuration (paramMap) and unique identifier mapping (uniqueMap)
- Provides complete data update examples

**Theoretical Foundation**: Supports the 3EX Architecture's Expression-Exchange-Execution flow in Paper Section 3.2.

### 5. Forms and Tables

- Defines form field structures and validation rules
- Defines table structures, columns, and advanced features
- Supports data source configuration

**Theoretical Foundation**: Form-filling experiments in Paper Section 4-5 demonstrate ANX's token efficiency advantages.

### 6. Unified Mapping Specification

- Clearly defines that map refers to field name to field name mapping
- Provides consistent parameter passing and data processing methods

### 7. Flexible Configuration Format

- Uses JSON format for configuration
- Supports modular configuration structure
- Provides detailed configuration examples

---

## Usage Scenarios

ANX protocol can be used in various scenarios:

### 1. Low-code Engine

As a page visualization display format and low-code engine language, enabling rapid development and deployment of frontend interfaces.

### 2. Agent Skill

As a skill for AI to understand application content, allowing Agents to interact with frontend elements intelligently.

**Theoretical Foundation**: Paper Section 3.1.2 - ANX CLI provides the command interface for Agent interaction.

### 3. Skill SOP Declaration

As a standard operating procedure (SOP) declaration for skills, providing a structured way to define skill behaviors.

**Theoretical Foundation**: Paper Section 3.1.4 - ANX SOP Specification defines machine-executable SOPs that eliminate natural language ambiguity.

### 4. Markdown Embedding

As interactive modules embedded in markdown files, using the following formats:

**Interactive Module**: Use :::anx for embedding and running ANX as an interactive module:

```anx
:::anx
{
  "kind":"input",
  "updateData":{
    "tableName":...
  }
}
:::
```

**Code Display**: Use \`\`\`anx for pure ANX code display:

```anx
```anx
{
  "kind":"input",
  "updateData":{
    "tableName":...
  }
}
\`\`\`
```

---

## 主要功能

ANX (AI Native Ex) 前端交互协议是一套专为 Agent 设计的统一前端编码标准，主要功能包括：

### 1. 统一的交互标准

建立了 Agent 与前端应用交互的统一规范，打破了传统上 Agent 必须使用浏览器或应用程序的限制。

**理论支撑**: 论文第 1.1 节讨论了为什么现有 GUI 中心的方法对 Agent 是不够的。

### 2. 导航配置

- 定义菜单结构和子菜单
- 支持页面导航和参数传递
- 提供完整的导航示例（如购物网站菜单）

### 3. 事件处理

- 支持多种触发类型：input、focus、blur、submit、tap、longtap、doubletap、cancel、clear
- 支持多种动作类型：navigateTo、navigateToBack、updateData、setTimeout、requestSet
- 提供简化版的 tap 事件配置

**理论支撑**: 这些设计模式支持论文第 3.1.3 节中的 "Create-on-Demand, Use-and-Go" 原则。

### 4. 数据操作

- 基于唯一标识符的智能数据更新（存在则更新，不存在则插入）
- 支持字段映射配置（paramMap）和唯一标识符映射（uniqueMap）
- 提供完整的数据更新示例

**理论支撑**: 支持论文第 3.2 节中 3EX 架构的 Expression-Exchange-Execution 流程。

### 5. 表单和表格

- 定义表单字段结构和验证规则
- 定义表格结构、列和高级功能
- 支持数据源配置

**理论支撑**: 论文第 4-5 节的表单填充实验展示了 ANX 的 token 效率优势。

### 6. 统一的映射规范

- 明确 map 是字段名与字段名之间的映射
- 提供一致的参数传递和数据处理方式

### 7. 灵活的配置格式

- 使用 JSON 格式进行配置
- 支持模块化的配置结构
- 提供详细的配置示例

## 使用场景

ANX 协议可以用于多种场景：

1. **低代码引擎**：作为页面可视化展示格式和低代码引擎语言，实现前端界面的快速开发和部署
2. **Agent Skill**：作为 AI 理解应用内容的技能，使 Agent 能够智能地与前端元素交互
3. **Skill SOP 声明**：作为技能的标准操作流程（SOP）声明，提供结构化的方式来定义技能行为
4. **Markdown 嵌入**：作为嵌入到 markdown 中的交互模块

---

## 🔑 Key Terms | 关键术语

| Term | Definition | 论文参考 |
|------|------------|----------|
| **ANX** | AI Native eX - Agent-native interaction protocol | Section 1 |
| **ANX Markup** | 结构化编码格式，高信息密度 | Section 3.1.1 |
| **3EX Architecture** | Expression-Exchange-Execution 分层架构 | Section 3.2 |
| **ANXHub** | Exchange 层的动态应用市场 | Section 3.2.2 |
| **SOP** | Standard Operating Procedure - 机器可执行的工作流程 | Section 3.1.4 |
| **Use-and-Go** | 按需创建应用，无需预注册 | Section 3.1.3 |

---

## 📎 Citation | 引用

If you use ANX in your research, please cite:

```bibtex
@article{anx2026,
  title={ANX: Protocol-First Design for AI Agent Interaction with a Supporting 3EX Decoupled Architecture},
  author={Xu, Mingze},
  journal={arXiv preprint arXiv:2604.04820},
  year={2026}
}
```

---

## 🌐 Resources

- **Paper**: https://arxiv.org/abs/2604.04820
- **GitHub**: https://github.com/mountorc/anx-protocol
- **Documentation**: [/protocol](./protocol/catalog.md)
- **License**: [Apache 2.0](./LICENSE)