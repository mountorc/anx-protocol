# Trigger and Tap Configuration Guide

## Overview

In ANX frontend interaction protocol, trigger and tap configurations define event-driven actions for UI elements, such as input changes, long taps, and regular taps.

## TriggerSet Configuration

`triggerSet` defines configurations for various event triggers:

```json
{
  "triggerSet": {
    "input": {
      "updateData": {
        "tableName": "table1",
        "paramMap": {
          "table_field1": "source_field1",
          "table_field2": "source_field2"
        },
        "uniqueMap": {
          "table_unique_field": "source_unique_field"
        }
      }
    },
    "longtap": {
      "navigateTo": {
        "path": "/page",
        "paramMap": {
          "target_param1": "source_field1",
          "target_param2": "source_field2"
        }
      }
    }
  }
}
```

### Trigger Types

| Trigger Type | Description |
|-------------|-------------|
| `input` | Triggered when input value changes |
| `focus` | Triggered when element gains focus |
| `blur` | Triggered when element loses focus |
| `submit` | Triggered when form is submitted |
| `tap` | Triggered when element is tapped |
| `longtap` | Triggered when element is long-pressed |
| `doubletap` | Triggered when element is double-tapped |
| `cancel` | Triggered when action is cancelled |
| `clear` | Triggered when input is cleared |

### Action Types

| Action Type | Description |
|-------------|-------------|
| `navigateTo` | Navigate to a specific page |
| `navigateBack` | Navigate back to previous page |
| `updateData` | Update data in a dataset |
| `setTimeout` | Set a timeout for delayed action |
| `requestSet` | Send a request to server |



## TapSet Configuration

`tapSet` is a simplified version for regular tap events:

```json
{
  "tapSet": {
    "navigateTo": {
      "path": "/page",
      "paramMap": {
        "target_param1": "source_field1",
        "target_param2": "source_field2"
      }
    },
    "requestSet": {
      "method": "POST",
      "url": "/api/submit",
      "paramMap": {
        "param1": "source_field1",
        "param2": "source_field2"
      }
    }
  }
}
```

### TapSet Field Descriptions

| Field | Description |
|-------|-------------|
| `navigateTo` | Target page to navigate to when tapped |
| `navigateBack` | Flag to navigate back when tapped |
| `updateData` | Data update configuration when tapped |
| `setTimeout` | Timeout configuration when tapped |
| `requestSet` | Request configuration when tapped |

### requestSet Configuration

The `requestSet` configuration for tapSet supports the following fields:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `method` | string | Yes | HTTP request method (e.g., "GET", "POST", "PUT", "DELETE") |
| `url` | string | Yes | Request URL |
| `paramMap` | object | No | Parameter mapping from source fields to request parameters |

### Request Execution Function

When a tap event triggers a `requestSet` action, the following process is executed:

1. **Parameter Collection**: The `paramMap` is used to collect parameters from the source fields
2. **Request Preparation**: The collected parameters are prepared as request data
3. **Request Execution**: The HTTP request is sent to the specified URL with the collected parameters
4. **Response Handling**: The response from the server is processed

#### Example Request Execution Function

```javascript
function executeRequest(requestConfig, sourceData) {
  // Step 1: Collect parameters using paramMap
  const params = {};
  if (requestConfig.paramMap) {
    Object.keys(requestConfig.paramMap).forEach(targetParam => {
      const sourceField = requestConfig.paramMap[targetParam];
      params[targetParam] = sourceData[sourceField];
    });
  }
  
  // Step 2 & 3: Execute the request
  return fetch(requestConfig.url, {
    method: requestConfig.method,
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(params)
  })
  .then(response => response.json())
  .then(data => {
    // Step 4: Handle response
    console.log('Request successful:', data);
    return data;
  })
  .catch(error => {
    console.error('Request failed:', error);
    throw error;
  });
}
```

## Usage Examples

### Example 1: Input Trigger with Data Update

```json
{
  "triggerSet": {
    "input": {
      "updateData": {
        "tableName": "users",
        "paramMap": {
          "name": "userName",
          "email": "userEmail"
        },
        "uniqueMap": {
          "id": "userId"
        }
      }
    }
  }
}
```

### Example 2: Long Tap with Navigation

```json
{
  "triggerSet": {
    "longtap": {
      "navigateTo": {
        "path": "/edit-user",
        "paramMap": {
          "userId": "id"
        }
      }
    }
  }
}
```

### Example 3: Simple Tap Navigation

```json
{
  "tapSet": {
    "navigateTo": {
      "path": "/product-details",
      "paramMap": {
        "productId": "id"
      }
    }
  }
}
```

### Example 4: Tap with Request

```json
{
  "tapSet": {
    "requestSet": {
      "method": "POST",
      "url": "/api/submit-form",
      "paramMap": {
        "name": "userName",
        "email": "userEmail",
        "phone": "userPhone"
      }
    }
  }
}
```

### Example 5: Focus Trigger with Request

```json
{
  "triggerSet": {
    "focus": {
      "requestSet": {
        "url": "/api/get-data",
        "paramMap": {
          "userId": "id"
        }
      }
    }
  }
}
```

### Example 6: Submit Trigger with Data Update

```json
{
  "triggerSet": {
    "submit": {
      "updateData": {
        "tableName": "orders",
        "paramMap": {
          "order_id": "orderId",
          "status": "orderStatus"
        },
        "uniqueMap": {
          "order_id": "orderId"
        }
      }
    }
  }
}
```

## Best Practices

- Use `triggerSet` for complex event handling with multiple event types
- Use `tapSet` for simple tap navigation actions
- Ensure `paramMap` keys match the expected parameter names in the target page
- Use `uniqueMap` for data updates to ensure correct record identification
- Keep configurations concise and focused on the specific event actions
- Use appropriate trigger types for different user interactions
- Choose the right action type based on the desired outcome