# ANX: AI Native eX Protocol

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![arXiv](https://img.shields.io/badge/arXiv-2604.04820-orange)](https://arxiv.org/abs/2604.04820)

## What is ANX?

**ANX (AI Native eX)** is an Agent-friendly frontend coding format designed to establish a unified standard that breaks the traditional scenario where Agents must use browsers or apps to browse web pages or use applications.

ANX provides four standard forms:
- **CLI**: Command-line interface form
- **Config**: Configuration file form
- **Markdown Block**: Markdown embedding form
- **Card Node**: Card node form

For detailed technical specifications, please refer to the [ANX Protocol Documentation](./protocol/catalog.md).

---

## 📖 Research Foundation

ANX protocol is grounded in academic research. Its core design principles and technical specifications are detailed in the following paper:

**Paper**: [ANX: Protocol-First Design for AI Agent Interaction with a Supporting 3EX Decoupled Architecture](https://arxiv.org/abs/2604.04820)

**Authors**: Xu Mingze (Hangzhou Ziyou Data Technology Co., Ltd.)

### Why Read the Paper?

The ANX protocol design incorporates the following core theories from the paper:

1. **Agent-Native Design Philosophy**
   - Traditional GUI automation suffers from high token consumption and DOM fragility
   - ANX uses structured encoding (ANX Markup) with high information density, significantly reducing token consumption
   - Experimental data: 47.3%-55.6% token reduction vs MCP, 57.1%-66.3% token reduction vs GUI automation

2. **Human-Agent Shared Interaction**
   - The same ANX definition can render as both Agent-executable instructions and human-readable UI
   - Develop once, use everywhere - eliminating human-agent interaction fragmentation

3. **3EX Architecture**
   - **Expression Layer**: Task specification layer (ANX Markup)
   - **Exchange Layer**: Exchange layer (ANXHub dynamic application marketplace)
   - **Execution Layer**: Execution layer (ANX Core, CLI, Nodes)
   - Three-layer decoupled design reduces Agent cognitive load and improves execution efficiency

4. **Security by Design**
   - **UI-to-Core Isolation**: Sensitive data bypasses LLM context, ensuring data isolation
   - **Human-Only Confirmation**: Confirmation operations cannot be delegated to Agents, preventing automated misuse

5. **Machine-Executable SOP**
   - Structured ANX Markup eliminates natural language ambiguity
   - Supports reliable long-horizon task execution and multi-Agent collaboration

### Quick Links

- [View Full Paper (PDF)](https://arxiv.org/pdf/2604.04820)
- [View HTML Version](https://arxiv.org/html/2604.04820v1)
- [Cite as]: `arXiv:2604.04820 [cs.AI]`

### How to Navigate This README

- **For Protocol Implementation**: Start with [Key Features](#key-features) below
- **For Design Philosophy**: Read the [Research Foundation](#-research-foundation) section above
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

\`\`\`anx
{
  "kind":"input",
  "updateData":{
    "tableName":...
  }
}
\`\`\`

---

## 🔑 Key Terms

| Term | Definition | Paper Reference |
|------|------------|-----------------|
| **ANX** | AI Native eX - Agent-native interaction protocol | Section 1 |
| **ANX Markup** | Structured encoding format with high information density | Section 3.1.1 |
| **3EX Architecture** | Expression-Exchange-Execution layered architecture | Section 3.2 |
| **ANXHub** | Dynamic application marketplace in Exchange layer | Section 3.2.2 |
| **SOP** | Standard Operating Procedure - machine-executable workflow | Section 3.1.4 |
| **Use-and-Go** | On-demand app creation without pre-registration | Section 3.1.3 |

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