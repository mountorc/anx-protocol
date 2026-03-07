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
  }

  // Read protocol files
  async readProtocolFile(filename) {
    const filePath = path.join(this.protocolPath, filename);
    try {
      const content = fs.readFileSync(filePath, 'utf8');
      return content;
    } catch (error) {
      return `Error reading file ${filename}: ${error.message}`;
    }
  }

  // Get all protocol files
  async getProtocolFiles() {
    try {
      const files = fs.readdirSync(this.protocolPath);
      return files.filter(file => file.endsWith('.md'));
    } catch (error) {
      return [];
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
        item: ['input', 'textarea', 'options', 'checkbox', 'button', 'text'],
        card: ['table', 'box', 'form', 'json', 'list']
      },
      formStructure: {
        kinds: 'Array of form items',
        itemFields: ['kind', 'type', 'nick', 'title', 'formula', 'defaultValue']
      },
      formulaSyntax: {
        variables: 'No special symbols needed',
        constants: 'Wrap in single quotes',
        operators: ['+', '-', '*', '/'],
        parentheses: 'Supported for grouping'
      }
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
}
