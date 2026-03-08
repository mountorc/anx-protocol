# Building ANX Configuration API

## Overview

This document describes how to build a configuration-based API for ANX frontend interaction protocol.

## Prerequisites

- Basic understanding of ANX protocol
- Backend development environment
- API routing setup

## Implementation Steps

### 1. Define API Endpoint

Create an API endpoint that returns ANX configuration using the default path:

```javascript
// Example in Node.js/Express
// Using query parameter: /anx/config?uuid_kind={{uuid_kind}}
app.get('/anx/config', (req, res) => {
  const uuidKind = req.query.uuid_kind;
  const config = getAnxConfig(uuidKind);
  res.json({ config });
});

// Using path parameter: /anx/config/{{uuid_kind}}
app.get('/anx/config/:uuid_kind', (req, res) => {
  const uuidKind = req.params.uuid_kind;
  const config = getAnxConfig(uuidKind);
  res.json({ config });
});
```

### 2. Create Configuration Structure

Define the ANX configuration structure with `kinds` array:

```javascript
function getAnxConfig(uuidKind) {
  switch (uuidKind) {
    case 'home':
      return {
        page: 'home',
        uuid_kind: uuidKind,
        kinds: [
          {
            kind: 'list',
            nick: 'items',
            title: 'Items',
            dataSource: '/api/data/items',
            template: 'list-item'
          },
          {
            kind: 'form',
            nick: 'search',
            title: 'Search',
            kinds: [
              {
                kind: 'input',
                type: 'string',
                nick: 'query',
                title: 'Search Query',
                defaultValue: ''
              },
              {
                kind: 'button',
                type: 'string',
                nick: 'submit',
                title: 'Search',
                action: 'search'
              }
            ]
          }
        ]
      };
    // Other pages...
    default:
      return { page: 'not-found', kinds: [] };
  }
}
```

### 3. Data Source APIs

Create separate APIs for data sources referenced in the configuration:

```javascript
app.get('/api/data/items', (req, res) => {
  // Fetch items from database or other source
  const items = [
    { id: 1, title: 'Item 1', description: 'Description 1' },
    { id: 2, title: 'Item 2', description: 'Description 2' }
  ];
  res.json(items);
});
```

### 4. Error Handling

Implement error handling for configuration retrieval:

```javascript
// For query parameter version
app.get('/anx/config', (req, res) => {
  try {
    const uuidKind = req.query.uuid_kind;
    const config = getAnxConfig(uuidKind);
    res.json({ config });
  } catch (error) {
    res.status(500).json({ error: 'Failed to load configuration' });
  }
});

// For path parameter version
app.get('/anx/config/:uuid_kind', (req, res) => {
  try {
    const uuidKind = req.params.uuid_kind;
    const config = getAnxConfig(uuidKind);
    res.json({ config });
  } catch (error) {
    res.status(500).json({ error: 'Failed to load configuration' });
  }
});
```

### 5. Caching (Optional)

Add caching to improve performance:

```javascript
const cache = new Map();

// For query parameter version
app.get('/anx/config', (req, res) => {
  const uuidKind = req.query.uuid_kind;
  
  // Check cache first
  if (cache.has(uuidKind)) {
    return res.json({ config: cache.get(uuidKind) });
  }
  
  try {
    const config = getAnxConfig(uuidKind);
    cache.set(uuidKind, config);
    res.json({ config });
  } catch (error) {
    res.status(500).json({ error: 'Failed to load configuration' });
  }
});

// For path parameter version
app.get('/anx/config/:uuid_kind', (req, res) => {
  const uuidKind = req.params.uuid_kind;
  
  // Check cache first
  if (cache.has(uuidKind)) {
    return res.json({ config: cache.get(uuidKind) });
  }
  
  try {
    const config = getAnxConfig(uuidKind);
    cache.set(uuidKind, config);
    res.json({ config });
  } catch (error) {
    res.status(500).json({ error: 'Failed to load configuration' });
  }
});
```

## Best Practices

- Keep configurations lightweight
- Use descriptive `nick` names for components
- Validate input parameters
- Implement proper error handling
- Consider caching for frequently accessed configurations

## Example Response

```json
{
  "config": {
    "page": "home",
    "kinds": [
      {
        "kind": "list",
        "nick": "items",
        "title": "Items",
        "dataSource": "/api/data/items",
        "template": "list-item"
      },
      {
        "kind": "form",
        "nick": "search",
        "title": "Search",
        "kinds": [
          {
            "kind": "input",
            "type": "string",
            "nick": "query",
            "title": "Search Query",
            "defaultValue": ""
          },
          {
            "kind": "button",
            "type": "string",
            "nick": "submit",
            "title": "Search",
            "action": "search"
          }
        ]
      }
    ]
  }
}
```
