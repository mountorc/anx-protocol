# ANX: AI Native eX Protocol

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![arXiv](https://img.shields.io/badge/arXiv-2604.04820-orange)](https://arxiv.org/abs/2604.04820)

## What is ANX?

**ANX (AI Native eX)** is an open, extensible, and verifiable agent-native protocol and top-level framework for AI agent interaction. It integrates CLI, Skill, and MCP to resolve pain points in existing approaches through protocol innovation, architectural optimization, and tool supplementation.

For detailed technical specifications and implementation guidelines, please refer to the [ANX Protocol Documentation](./protocol/catalog.md).

## 📄 Read the Paper

The complete research paper is available on arXiv:

**Paper Title**: [ANX: Protocol-First Design for AI Agent Interaction with a Supporting 3EX Decoupled Architecture](https://arxiv.org/abs/2604.04820)

**Authors**: Xu Mingze (Hangzhou Ziyou Data Technology Co., Ltd.)

**Cite as**: `arXiv:2604.04820 [cs.AI]`

### Quick Links

- [View Full Paper (PDF)](https://arxiv.org/pdf/2604.04820)
- [View HTML Version](https://arxiv.org/html/2604.04820v1)
- [View TeX Source](https://arxiv.org/src/2604.04820)
- [GitHub Repository](https://github.com/mountorc/anx-protocol)

---

## 📖 How to Read This Paper

This paper introduces ANX, a novel agent-native interaction protocol. Here's a recommended reading path:

### 1. Start with Abstract and Introduction (Sections 1)

- **Abstract**: Understand the core problem ANX solves and its four key innovations
- **1.1 Background**: Learn why existing approaches (GUI automation, MCP, skills) are insufficient
- **1.2 Contributions**: Get a roadmap of the paper's main contributions

**Key Takeaway**: ANX addresses fragmentation in agent interaction protocols by providing a unified, efficient, and secure framework.

### 2. Review Related Work (Section 2)

Section 2 provides a comprehensive survey of existing approaches across four dimensions:

| Dimension | Description |
|-----------|-------------|
| **Protocol & Tooling** | Task representation, discovery, token efficiency |
| **Discovery & Retrieval** | Discovery mechanism, latency, dynamic updates |
| **Security** | Data isolation, human confirmation, authentication |
| **Collaboration** | SOP representation, multi-agent coordination |

**Key Takeaway**: Existing solutions each address partial problems but lack a holistic approach.

### 3. Core Protocol Design (Section 3.1)

The ANX Protocol has four core components:

1. **ANX Markup**: Structured, machine-executable encoding with high information density
2. **ANX Config**: Unified configuration format for components
3. **ANX CLI**: Command-line interface for agent interaction
4. **ANX SOP**: Machine-executable Standard Operating Procedures

### 4. Architecture: 3EX (Section 3.2)

The 3EX (Expression-Exchange-Execution) decoupled architecture:

```
┌─────────────────────────────────────────────────────────────┐
│                    Expression Layer                         │
│         (Task specification via ANX Markup)                │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Exchange Layer (ANXHub)                  │
│      (Dynamic discovery, negotiation, use-and-go apps)      │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Execution Layer                          │
│      (ANX Core, CLI, Nodes - secure execution)             │
└─────────────────────────────────────────────────────────────┘
```

### 5. Security Mechanisms (Section 3.3)

ANX provides native security features:

- **UI-to-Core Data Isolation**: Sensitive data bypasses LLM context
- **Human-Only Confirmation**: Confirmation cannot be delegated to agents
- **Threat Model**: Comprehensive security analysis

### 6. Experimental Results (Sections 4-5)

**Performance Improvements**:

| Metric | Qwen3.5-plus | GPT-4o |
|--------|--------------|--------|
| Token Reduction vs MCP | 47.3% | 55.6% |
| Token Reduction vs GUI | 57.1% | 66.3% |
| Execution Time Reduction vs MCP | 58.1% | 57.7% |

**Key Takeaway**: ANX significantly reduces token consumption and execution time while maintaining security.

---

## 🏗️ Core Innovations Summary

### Protocol Innovations

| Innovation | Description | Benefit |
|------------|-------------|---------|
| **Agent-Native Design** | ANX Config, Markup, CLI designed first for agents | High information density, reduced tokens |
| **Human-Agent Shared Interaction** | Same definition renders as agent instructions AND human UI | Develop once, use everywhere |
| **Create-on-Demand** | Agents generate apps dynamically, no pre-registration | Use-and-go capability |
| **Machine-Executable SOP** | Structured ANX Markup eliminates NL ambiguity | Reliable long-horizon tasks |

### Architecture Innovations

| Innovation | Description | Benefit |
|------------|-------------|---------|
| **3EX Layered Architecture** | Expression-Exchange-Execution decoupling | Lower cognitive load, higher efficiency |
| **ANXHub** | Massive application marketplace | Dynamic discovery, no installation |
| **Embedded Security** | Direct UI-to-Core communication | Sensitive data isolation |
| **Multi-Agent Collaboration** | Stable SOP execution with human gatekeepers | Scalable cooperation |

---

## 📚 Paper Structure Overview

```
1. Introduction
   ├── Background & Problem Statement
   ├── Contributions
   └── Paper Structure

2. Related Work
   ├── GUI-Based Approaches
   ├── Tool-Calling Protocols (MCP)
   ├── Emerging Agent-Native Protocols
   ├── Agent Architecture & Governance
   ├── Four-Dimensional Evaluation Framework
   └── Research Gaps

3. ANX Protocol & Architecture
   ├── ANX Protocol (Markup, Config, CLI, SOP)
   ├── 3EX Architecture
   ├── Security Mechanisms
   └── ANX SOP Runtime & Multi-Agent Collaboration

4. Experimental Methodology
   ├── Research Questions
   ├── Task Design
   └── Evaluation Metrics

5. Results & Discussion
   ├── RQ1: Efficiency
   └── Discussion

6. Conclusion & Future Work
```

---

## 🔑 Key Terms

| Term | Definition |
|------|------------|
| **ANX** | AI Native eX - Agent-native interaction protocol |
| **ANX Markup** | Structured encoding format for agent interaction |
| **3EX Architecture** | Expression-Exchange-Execution decoupled architecture |
| **ANXHub** | Dynamic application marketplace in Exchange layer |
| **SOP** | Standard Operating Procedure - machine-executable workflow |
| **Use-and-Go** | On-demand app creation without pre-registration |

---

## 📎 Citation

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

---

## 什么是 ANX？

**ANX (AI Native eX)** 是一个开放的、可扩展的、可验证的 Agent 原生交互协议和顶层框架。它通过协议创新、架构优化和工具补充，整合 CLI、Skill 和 MCP 来解决现有方法中的痛点。

详细技术规范请参阅 [ANX 协议文档](./protocol/catalog.md)。

## 协议文件

### protocol 文件夹

- **catalog.md**: 协议文档索引，您可以在此处找到每个文件包含的内容
- **forms.md**: ANX 协议 4 类标准形式 - 介绍协议的四种标准形式（CLI、Config、Markdown 块、Card 节点）及其使用场景

## 主要功能

ANX (AI Native Ex) 前端交互协议是一套专为 Agent 设计的统一前端编码标准，主要功能包括：

1. **统一的交互标准**：建立了 Agent 与前端应用交互的统一规范，打破了传统上 Agent 必须使用浏览器或应用程序的限制

2. **导航配置**：
   - 定义菜单结构和子菜单
   - 支持页面导航和参数传递
   - 提供完整的导航示例

3. **事件处理**：
   - 支持多种触发类型：input、focus、blur、submit、tap、longtap、doubletap、cancel、clear
   - 支持多种动作类型：navigateTo、navigateBack、updateData、setTimeout、requestSet

4. **数据操作**：
   - 基于唯一标识符的智能数据更新（存在则更新，不存在则插入）
   - 支持字段映射配置（paramMap）和唯一标识符映射（uniqueMap）

5. **表单和表格**：
   - 定义表单字段结构和验证规则
   - 定义表格结构、列和高级功能
   - 支持数据源配置

## 使用场景

ANX 协议可以用于多种场景：

1. **低代码引擎**：作为页面可视化展示格式和低代码引擎语言
2. **Agent Skill**：作为 AI 理解应用内容的技能
3. **Skill SOP 声明**：作为技能的标准操作流程（SOP）声明
4. **Markdown 嵌入**：作为嵌入到 markdown 中的交互模块