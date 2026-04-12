# SOP (Standard Operating Procedure) Component Specification

## Overview

The SOP component in ANX protocol defines structured workflows with clear control flow mechanisms, including sources for dependencies and targets for dynamic routing. This allows for both deterministic execution and adaptive decision-making.

## Basic Structure

```json
{
  "protocol": "ANX",
  "version": "1.0.0",
  "kind": "sop",
  "title": "Workflow Title",
  "steps": [
    {
      "uuid": "step_id",
      "start": true,
      "nick": "stepNickname",
      "kind": "form",
      "items": [
        {"nick": "lastName", "kind": "input"},
        {
          "nick": "industry",
          "kind": "options",
          "optionsSet": {
            "dataset": {
              "url_dataset": "http://localhost:7887/dataset/industries"
            },
            "valueNick": "id",
            "titleNick": "name"
          }
        }
      ]
    },
    {
      "uuid": "step_id",
      "action": "stepAction",
      "sources": ["source_step_id"],
      "condition": [
        {
          "operator": "operator",
          "nick": "variableName",
          "value": "value",
          "targets": ["target_step_id"]
        }
      ]
    }
  ]
}
```

## ANX SOP Control Flow: Sources, Targets, and Execution Semantics

ANX SOP uses two complementary mechanisms to define control flow: sources and targets. The sources field lists predecessor steps that must be completed before the current step can be scheduled, establishing static structural dependencies to ensure determinism, verifiability, and support for synchronization and parallel patterns. The targets field provides a constrained set of candidate steps for dynamic routing, allowing the LLM to select appropriate branches based on runtime conditions. Together, they balance structural stability and adaptive decision-making.

For step synchronization with multiple sources, ANX SOP supports two joining strategies controlled by the sources_join field:

- **all** (default): The step executes only when all executed sources have completed. Unexecuted sources due to conditional routing are marked as skipped and do not block the workflow.

- **any**: The step executes as soon as any one of its sources has completed.

In case of overlapping declarations—when a step appears in the predecessor’s targets list and also lists the predecessor in its own sources—dynamic routing via targets takes precedence. The step is executed only if selected by the LLM, rather than being automatically triggered by the source dependency.

## Field Descriptions

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| protocol | string | Yes | Protocol name, fixed as "ANX" |
| version | string | Yes | Protocol version |
| kind | string | Yes | Component type, fixed as "sop" |
| title | string | Yes | Workflow title |
| steps | array | Yes | Array of workflow steps |

### Step Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| uuid | string | Yes | Unique identifier for the step |
| start | boolean | No | Indicates if this is the start step |
| nick | string | No | Step nickname |
| kind | string | No | Component type for the step |
| items | array | No | Items for form-based steps |
| action | string | No | Action to perform for the step |
| sources | array | No | List of predecessor step UUIDs |
| sources_join | string | No | Joining strategy: "all" or "any" |
| condition | array | No | Conditional routing rules |
| approvalRequired | boolean | No | Whether approval is required |

### Form Item Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| nick | string | Yes | Field nickname |
| kind | string | Yes | Field type (e.g., input, options, textarea, date) |
| optionsSet | object | No | Options configuration for dropdown/selection fields |
| required | boolean | No | Whether the field is required |

### OptionsSet Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| dataset | object | No | Dataset configuration |
| valueNick | string | No | Field name for option values |
| titleNick | string | No | Field name for option display text |

### Dataset Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| url_dataset | string | No | URL for dataset endpoint |

### Condition Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| operator | string | Yes | Comparison operator (e.g., "==", "<", ">", "≤", "≥") |
| nick | string | Yes | Variable name to compare |
| value | any | Yes | Value to compare against |
| targets | array | Yes | Target step UUIDs for this condition |

## Example

```json
{
  "protocol": "ANX",
  "version": "1.0.0",
  "kind": "sop",
  "title": "Employee Leave-Request Approval Workflow",
  "steps": [
    {
      "uuid": "step_123",
      "start": true,
      "nick": "fillLeaveForm",
      "kind": "form",
      "items": [
        {"nick": "leaveStartDate", "kind": "date", "required": true},
        {"nick": "leaveEndDate", "kind": "date", "required": true},
        {"nick": "leaveReason", "kind": "textarea", "required": true}
      ]
    },
    {
      "uuid": "step_234",
      "action": "calculateLeaveDuration",
      "sources": ["step_123"],
      "condition": [
        {"operator": "≤", "nick": "leaveDuration", "value": 3, "targets": ["step_345"]},
        {"operator": ">", "nick": "leaveDuration", "value": 3, "targets": ["step_456"]}
      ]
    },
    {
      "uuid": "step_345",
      "action": "submitToDirectSupervisor",
      "approvalRequired": true
    },
    {
      "uuid": "step_456",
      "action": "submitToDeptManager",
      "approvalRequired": true
    },
    {
      "uuid": "step_567",
      "sources": ["step_345", "step_456"],
      "action": "completeLeaveProcess",
      "condition": [
        {"operator": "==", "nick": "approvalStatus", "value": "approved", "targets": ["success"]},
        {"operator": "==", "nick": "approvalStatus", "value": "rejected", "targets": ["retry"]}
      ]
    }
  ]
}
```

## Usage Guidelines

1. **Step Identification**: Use unique UUIDs for each step to ensure proper referencing
2. **Dependency Management**: Use sources to define clear structural dependencies
3. **Conditional Routing**: Use condition blocks with operators to define dynamic routing paths
4. **Synchronization**: Choose appropriate sources_join strategy for multi-source steps
5. **Approval Workflows**: Mark steps requiring approval with approvalRequired: true
6. **Start Step**: Always include a start step with start: true to initiate the workflow
7. **Consistency**: Maintain consistent naming conventions for nicks and actions
8. **Validation**: Ensure all required fields are present for each step type

## Best Practices

- Keep workflows modular and focused on specific business processes
- Use descriptive nicknames and action names for better readability
- Define clear conditional logic with appropriate operators
- Test workflows with different input scenarios
- Document complex workflows with additional metadata
- Use sources_join: "any" for parallel processing scenarios
- Use sources_join: "all" for steps requiring complete input from multiple sources