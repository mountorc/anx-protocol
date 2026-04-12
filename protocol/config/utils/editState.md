# Edit State Definition

## Edit State Values

| Value | Meaning | Description |
|-------|---------|-------------|
| 0 | 不可见 | The element is not visible |
| 1 | 不可编辑 | The element is visible but cannot be edited |
| 2 | 可编辑 | The element is visible and can be edited |

## Usage Scenarios

EditState is used in both card kinds (like page, form, json, list) and item kinds.

## Inheritance Rules

The editState of a parent kind affects the editState of child kinds:

1. **If parent has editState=1 and child has editState=2**: Child uses editState=1
2. **If parent has no editState defined**: Child uses its own editState
3. **If parent has editState=2 and child has editState=1**: Child uses editState=1
4. **General rule**: The child's editState is the minimum value between the parent's editState and the child's own editState

## Example

- Parent (form) editState=1, Child (input item) editState=2 → Child uses editState=1
- Parent (page) editState=2, Child (form) editState=1 → Child uses editState=1
- Parent (list) no editState, Child (item) editState=2 → Child uses editState=2
