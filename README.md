# ANX Frontend Interaction Protocol

## What is ANX?

ANX stands for **AI Native Ex** (AI Native Interaction Protocol). It is an Agent-friendly frontend coding format designed to establish a unified standard that breaks the traditional scenario where Agents must use browsers or apps to browse web pages or use applications.

## 什么是 ANX？

ANX 代表 **AI Native Ex**（AI 原生交互协议）。它是一种对 Agent 友好的前端编码格式，旨在建立统一标准，打破传统上 Agent 必须使用浏览器或应用程序来浏览网页或使用应用的场景。

## Protocol Files

### protocol folder
- **catalog.md**: Protocol document index. You can find what each file contains here.

## Key Features

ANX (AI Native Ex) Frontend Interaction Protocol is a unified frontend coding standard designed specifically for Agents, with the following key features:

1. **Unified Interaction Standard**: Establishes a unified standard for Agent-frontend application interaction, breaking the traditional limitation where Agents must use browsers or applications

2. **Navigation Configuration**:
   - Defines menu structures and submenus
   - Supports page navigation and parameter passing
   - Provides complete navigation examples (such as shopping website menus)

3. **Event Handling**:
   - Supports multiple trigger types: input, focus, blur, submit, tap, longtap, doubletap, cancel, clear
   - Supports multiple action types: navigateTo, navigateBack, updateData, setTimeout, requestSet
   - Provides simplified tap event configuration

4. **Data Operations**:
   - Intelligent data update based on unique identifiers (update if exists, insert if not)
   - Supports field mapping configuration (paramMap) and unique identifier mapping (uniqueMap)
   - Provides complete data update examples

5. **Forms and Tables**:
   - Defines form field structures and validation rules
   - Defines table structures, columns, and advanced features
   - Supports data source configuration

6. **Unified Mapping Specification**:
   - Clearly defines that map refers to field name to field name mapping
   - Provides consistent parameter passing and data processing methods

7. **Flexible Configuration Format**:
   - Uses JSON format for configuration
   - Supports modular configuration structure
   - Provides detailed configuration examples

## Usage Scenarios

ANX protocol can be used in various scenarios:

1. **Low-code Engine**: As a page visualization display format and low-code engine language, enabling rapid development and deployment of frontend interfaces
2. **Agent Skill**: As a skill for AI to understand application content, allowing Agents to interact with frontend elements intelligently
3. **Skill SOP Declaration**: As a standard operating procedure (SOP) declaration for skills, providing a structured way to define skill behaviors
4. **Markdown Embedding**: As interactive modules embedded in markdown files, using the following formats:

   - **Interactive Module**: Use :::anx for embedding and running ANX as an interactive module:

     :::anx
     {
       "kind":"input",
       "updateData":{
         "tableName":...
       }
     }
     :::

   - **Code Display**: Use ```anx for pure ANX code display:

     ```anx
     {
       "kind":"input",
       "updateData":{
         "tableName":...
       }
     }
     ```

## 协议文件

### protocol 文件夹
- **catalog.md**：协议文档索引。您可以在这里找到每个文件包含的内容。

## 主要功能

ANX (AI Native Ex) 前端交互协议是一套专为 Agent 设计的统一前端编码标准，主要功能包括：

1. **统一的交互标准**：建立了Agent与前端应用交互的统一规范，打破了传统上Agent必须使用浏览器或应用程序的限制

2. **导航配置**：
   - 定义菜单结构和子菜单
   - 支持页面导航和参数传递
   - 提供完整的导航示例（如购物网站菜单）

3. **事件处理**：
   - 支持多种触发类型：input、focus、blur、submit、tap、longtap、doubletap、cancel、clear
   - 支持多种动作类型：navigateTo、navigateBack、updateData、setTimeout、requestSet
   - 提供简化版的tap事件配置

4. **数据操作**：
   - 基于唯一标识符的智能数据更新（存在则更新，不存在则插入）
   - 支持字段映射配置（paramMap）和唯一标识符映射（uniqueMap）
   - 提供完整的数据更新示例

5. **表单和表格**：
   - 定义表单字段结构和验证规则
   - 定义表格结构、列和高级功能
   - 支持数据源配置

6. **统一的映射规范**：
   - 明确map是字段名与字段名之间的映射
   - 提供一致的参数传递和数据处理方式

7. **灵活的配置格式**：
   - 使用JSON格式进行配置
   - 支持模块化的配置结构
   - 提供详细的配置示例

## 使用场景

ANX 协议可以用于多种场景：

1. **低代码引擎**：作为页面可视化展示格式和低代码引擎语言，实现前端界面的快速开发和部署
2. **Agent Skill**：作为AI理解应用内容的技能，使Agent能够智能地与前端元素交互
3. **Skill SOP 声明**：作为技能的标准操作流程（SOP）声明，提供结构化的方式来定义技能行为
4. **Markdown 嵌入**：作为嵌入到markdown中的交互模块，使用如下格式：

   - **交互模块**：使用 :::anx 格式嵌入并运行 ANX 作为交互模块：

     :::anx
     {
       "kind":"input",
       "updateData":{
         "tableName":...
       }
     }
     :::

   - **代码展示**：使用 ```anx 格式用于纯 ANX 代码展示：

     ```anx
     {
       "kind":"input",
       "updateData":{
         "tableName":...
       }
     }
     ```
