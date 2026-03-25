# Building ANX Full-Information API

## Overview

This document describes how to build a full-information API for ANX frontend interaction protocol, which returns complete page content including dynamic data.

## Prerequisites

- Basic understanding of ANX protocol
- Backend development environment
- API routing setup
- anxcore-sdk installed

## Installation

First, install the anxcore-sdk:

```bash
npm install anxcore-sdk
```

## Implementation Steps

### 1. Define API Endpoint

Create an API endpoint that returns complete page information using the default path:

```javascript
// Example in Node.js/Express
const { AnxCore } = require('anxcore-sdk');

// Using query parameter: /anx/page?uuid_page={{uuid_page}}
app.get('/anx/page', async (req, res) => {
  const uuidPage = req.query.uuid_page;
  try {
    const content = await getAnxPage(uuidPage);
    res.json({ page: uuidPage, content });
  } catch (error) {
    res.status(500).json({ error: 'Failed to load page' });
  }
});

// Using path parameter: /anx/page/{{uuid_page}}
app.get('/anx/page/:uuid_page', async (req, res) => {
  const uuidPage = req.params.uuid_page;
  try {
    const content = await getAnxPage(uuidPage);
    res.json({ page: uuidPage, content });
  } catch (error) {
    res.status(500).json({ error: 'Failed to load page' });
  }
});
```

### 2. Implement Page Generation

Use anxcore-sdk to generate complete page content:

```javascript
async function getAnxPage(uuidPage) {
  // Initialize AnxCore
  const anxcore = new AnxCore();
  
  // Load configuration
  const config = getAnxConfig(uuidPage);
  
  // Process configuration and load dynamic data
  const processedContent = await anxcore.process(config);
  
  return processedContent;
}

function getAnxConfig(uuidPage) {
  switch (uuidPage) {
    case 'home':
      return {
        page: 'home',
        uuid_page: uuidPage,
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

### 3. Implement Data Fetching

Create functions to fetch dynamic data:

```javascript
// Example data fetching function
async function fetchItems() {
  // Fetch items from database or other source
  return [
    { id: 1, title: 'Item 1', description: 'Description 1' },
    { id: 2, title: 'Item 2', description: 'Description 2' }
  ];
}

// Register data fetchers with anxcore-sdk
anxcore.registerDataFetcher('/api/data/items', fetchItems);
```

### 4. Error Handling

Implement comprehensive error handling:

```javascript
app.get('/api/anx/page/:page', async (req, res) => {
  const page = req.params.page;
  try {
    const content = await getAnxPage(page);
    res.json({ page, content });
  } catch (error) {
    console.error('Error generating page:', error);
    res.status(500).json({ 
      error: 'Failed to load page',
      details: process.env.NODE_ENV === 'production' ? 'Internal server error' : error.message
    });
  }
});
```

### 5. Caching (Optional)

Add caching to improve performance:

```javascript
const cache = new Map();
const CACHE_DURATION = 5 * 60 * 1000; // 5 minutes

// For query parameter version
app.get('/anx/page', async (req, res) => {
  const uuidPage = req.query.uuid_page;
  const cacheKey = `page_${uuidPage}_${JSON.stringify(req.query)}`;
  
  // Check cache first
  const cached = cache.get(cacheKey);
  if (cached && Date.now() - cached.timestamp < CACHE_DURATION) {
    return res.json(cached.data);
  }
  
  try {
    const content = await getAnxPage(uuidPage);
    const response = { page: uuidPage, content };
    
    // Update cache
    cache.set(cacheKey, {
      data: response,
      timestamp: Date.now()
    });
    
    res.json(response);
  } catch (error) {
    res.status(500).json({ error: 'Failed to load page' });
  }
});

// For path parameter version
app.get('/anx/page/:uuid_page', async (req, res) => {
  const uuidPage = req.params.uuid_page;
  const cacheKey = `page_${uuidPage}_${JSON.stringify(req.query)}`;
  
  // Check cache first
  const cached = cache.get(cacheKey);
  if (cached && Date.now() - cached.timestamp < CACHE_DURATION) {
    return res.json(cached.data);
  }
  
  try {
    const content = await getAnxPage(uuidPage);
    const response = { page: uuidPage, content };
    
    // Update cache
    cache.set(cacheKey, {
      data: response,
      timestamp: Date.now()
    });
    
    res.json(response);
  } catch (error) {
    res.status(500).json({ error: 'Failed to load page' });
  }
});
```

## Best Practices

- Use proper error handling and logging
- Implement caching for frequently accessed pages
- Optimize data fetching to minimize latency
- Validate input parameters
- Consider using a CDN for static content

## Example Response

```json
{
  "page": "home",
  "content": {
    "kinds": [
      {
        "kind": "list",
        "nick": "items",
        "title": "Items",
        "data": [
          { "id": 1, "title": "Item 1", "description": "Description 1" },
          { "id": 2, "title": "Item 2", "description": "Description 2" }
        ],
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
