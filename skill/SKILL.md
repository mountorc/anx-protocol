---
name: ANX Frontend Protocol
description: Provides frontend programming guidelines based on ANX protocol, including catalog-based index lookup
version: 1.0.0
author: mountorc
category: frontend
---

# ANX Frontend Protocol Skill

## 核心能力
- **Catalog-based Index Lookup**: Uses `protocol/catalog.md` as the central index to locate and retrieve protocol files
- **Protocol File Management**: Provides structured access to all ANX protocol documentation files
- **Frontend Guidelines**: Delivers comprehensive frontend programming guidelines based on ANX protocol standards

## 命令
- **getProtocolFiles**: Get complete list of protocol files from catalog
- **readProtocolFile**: Read specific protocol file content by filename
- **getProtocolDocumentation**: Get all protocol documentation in structured format
- **getFrontendGuidelines**: Get frontend programming guidelines

## 使用场景
- When you need to follow ANX frontend interaction protocol
- When you need to understand component types and form structures
- When you need to generate frontend code following ANX standards
- When you need to quickly locate specific protocol documentation

## 工作原理
1. **Index Lookup**: Reads the catalog.md file to establish an index of all protocol documents
2. **Path Resolution**: Maps requested document names to their actual file paths
3. **Content Retrieval**: Fetches and returns the content of requested protocol files

## 输出解释
- Returns protocol documentation and guidelines in structured format
- Provides clear examples of ANX protocol usage
- Includes file path information for cross-referencing

## 示例
- "Get me the ANX frontend guidelines"
- "Show me the form configuration structure"
- "What component types are available in ANX?"
- "List all protocol files in the catalog"
- "Read the table configuration guidelines"
