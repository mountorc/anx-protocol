const fs = require('fs');
const path = require('path');

class ANXFrontendProtocolSkill {
  constructor() {
    // Try to find protocol folder in different locations
    this.protocolPath = path.join(__dirname, 'protocol');
    if (!fs.existsSync(this.protocolPath)) {
      // Fallback to parent directory
      this.protocolPath = path.join(__dirname, '../protocol');
    }
    this.catalogPath = path.join(this.protocolPath, 'catalog.md');
    this.catalogIndex = null;
  }

  // Parse catalog.md to create an index
  async parseCatalog() {
    try {
      const catalogContent = fs.readFileSync(this.catalogPath, 'utf8');
      const lines = catalogContent.split('\n');
      const index = {};

      lines.forEach(line => {
        // Match lines like "### 1. spec/main.md"
        const match = line.match(/### \d+\.\s+([^\n]+)/);
        if (match) {
          const filePath = match[1].trim();
          // Extract filename from path
          const filename = path.basename(filePath);
          index[filename] = filePath;
        }
      });

      this.catalogIndex = index;
      return index;
    } catch (error) {
      console.error('Error parsing catalog:', error);
      return {};
    }
  }

  // Get catalog index
  async getCatalogIndex() {
    if (!this.catalogIndex) {
      await this.parseCatalog();
    }
    return this.catalogIndex;
  }

  // Read protocol files using catalog index
  async readProtocolFile(filename) {
    try {
      // Get catalog index
      const index = await this.getCatalogIndex();
      
      // Find the file path in the catalog
      let filePath;
      if (index[filename]) {
        // Use the path from catalog
        filePath = path.join(this.protocolPath, path.basename(index[filename]));
      } else {
        // Fallback to direct path
        filePath = path.join(this.protocolPath, filename);
      }

      const content = fs.readFileSync(filePath, 'utf8');
      return content;
    } catch (error) {
      return `Error reading file ${filename}: ${error.message}`;
    }
  }

  // Get all protocol files from catalog
  async getProtocolFiles() {
    try {
      const index = await this.getCatalogIndex();
      return Object.keys(index);
    } catch (error) {
      // Fallback to directory listing
      try {
        const files = fs.readdirSync(this.protocolPath);
        return files.filter(file => file.endsWith('.md'));
      } catch (fallbackError) {
        return [];
      }
    }
  }

  // Get protocol documentation
  async getProtocolDocumentation() {
    const files = await this.getProtocolFiles();
    const documentation = {};

    for (const file of files) {
      documentation[file] = await this.readProtocolFile(file);
    }

    return documentation;
  }

  // Get frontend programming guidelines
  async getFrontendGuidelines() {
    const guidelines = {
      name: 'ANX Frontend Protocol Guidelines',
      version: '1.0.0',
      description: 'AI Native Ex frontend interaction protocol guidelines',
      components: {
        item: ['input', 'textarea', 'options', 'checkbox', 'button', 'text', 'image', 'images', 'file', 'video', 'voice', 'json', 'list', 'time', 'date', 'month', 'year', 'datetime', 'color', 'province', 'city', 'markdown', 'html'],
        card: ['table', 'box', 'form', 'chart']
      },
      formStructure: {
        kinds: 'Array of form items',
        itemFields: ['kind', 'type', 'nick', 'title', 'formula', 'defaultValue', 'must']
      },
      formulaSyntax: {
        variables: 'No special symbols needed',
        constants: 'Wrap in single quotes',
        operators: ['+', '-', '*', '/'],
        parentheses: 'Supported for grouping',
        conditional: 'case when then else end syntax (SQL-like)'
      },
      chartTypes: ['pie', 'line', 'bar', 'scatter', 'radar', 'doughnut', 'polarArea', 'bubble', 'area'],
      datasetTypes: ['direct', 'uuid_dataset', 'url_dataset']
    };

    return guidelines;
  }

  // Skill interface methods
  async execute(command, args) {
    switch (command) {
      case 'getProtocolFiles':
        return await this.getProtocolFiles();
      case 'readProtocolFile':
        return await this.readProtocolFile(args.filename);
      case 'getProtocolDocumentation':
        return await this.getProtocolDocumentation();
      case 'getFrontendGuidelines':
        return await this.getFrontendGuidelines();
      default:
        return 'Command not supported. Available commands: getProtocolFiles, readProtocolFile, getProtocolDocumentation, getFrontendGuidelines';
    }
  }

  // Health check
  async healthCheck() {
    return { status: 'ok', timestamp: new Date().toISOString() };
  }
}

// Export the skill
module.exports = ANXFrontendProtocolSkill;

// For direct execution
if (require.main === module) {
  const skill = new ANXFrontendProtocolSkill();
  skill.healthCheck().then(console.log);
  skill.getFrontendGuidelines().then(console.log);
  skill.getProtocolFiles().then(console.log);
}
