# ANX CLI Command Guide

## Overview

This guide describes the command-line interface (CLI) format and command set for ANX frontend interaction protocol.

## Command Format

The ANX CLI uses the following format:

```
anx <cardKey> <action> [parameters...]
```

Where:
- `<cardKey>`: The cardKey of the component built by anx-core, used to locate the execution position
- `<action>`: The action to execute
- `[parameters...]`: Optional parameters for the action

## Parameter Writing and Variable Placeholder Specification

### Literal Writing

- **Content without spaces or special symbols**: Write directly without quotes
- **Content containing spaces, Chinese characters, or special symbols**: Must be wrapped in double quotes `"`
- **Do not use single quotes**

### Variable Placeholder

- Support variable placeholder syntax: `${variableName}`
- Variables are replaced at runtime by the execution context or workflow engine
- Can be used alone or mixed with literals within double quotes
- **Does not support expressions, operations, or function calls**

### Examples

```plaintext
# Normal value
anx username input hello

# Content with spaces
anx title fill "欢迎使用 ANX"

# Variable
anx username input ${username}

# Mixed use
anx title input "用户：${username}"
```

## Available Actions

### 1. Query Commands

#### get_config

**Description**: Get component configuration; read structure only, not values

**Usage**:
```
anx <cardKey> get_config
```

**Example**:
```
anx user-profile get_config
```

**Output**:
Returns the ANX configuration object for the specified component.

#### get_form

**Description**: Get form overall data; only valid for form components

**Usage**:
```
anx <cardKey> get_form
```

**Example**:
```
anx login-form get_form
```

**Output**:
Returns the form data object for the specified form component.

#### get_node

**Description**: Get complete node information (structure + values + state)

**Usage**:
```
anx <cardKey> get_node
```

**Example**:
```
anx dashboard get_node
```

**Output**:
Returns the complete node object including structure, values, and state.

#### get_children

**Description**: Get list of child component cardKeys

**Usage**:
```
anx <cardKey> get_children
```

**Example**:
```
anx form-container get_children
```

**Output**:
Returns an array of cardKeys for child components.

#### get_options

**Description**: Get optional configuration items for dropdown/radio/checkbox

**Usage**:
```
anx <cardKey> get_options
```

**Example**:
```
anx country-select get_options
```

**Output**:
Returns an array of option objects for the specified component.

#### get_value

**Description**: Get current component value; universal

**Usage**:
```
anx <cardKey> get_value
```

**Example**:
```
anx username-input get_value
```

**Output**:
Returns the current value of the specified component.

#### get_state

**Description**: Get state: disabled/hidden/checked/expanded, etc.

**Usage**:
```
anx <cardKey> get_state
```

**Example**:
```
anx submit-button get_state
```

**Output**:
Returns the state object of the specified component.

#### get_validate

**Description**: Get validation result: success/failure/error message

**Usage**:
```
anx <cardKey> get_validate
```

**Example**:
```
anx email-input get_validate
```

**Output**:
Returns the validation result object for the specified component.

### 2. Input and Assignment Commands

#### input

**Description**: Append input character by character; keep focus, can be called continuously

**Usage**:
```
anx <cardKey> input <content>
```

**Parameters**:
- `<content>`: The content to append (string)

**Example**:
```
anx search-input input hello
```

#### fill

**Description**: Fill input box at once; overwrite existing content

**Usage**:
```
anx <cardKey> fill <content>
```

**Parameters**:
- `<content>`: The content to fill (string)

**Example**:
```
anx username-input fill john_doe
```

#### set

**Description**: Universal assignment; applicable to all component state settings

**Usage**:
```
anx <cardKey> set <value>
```

**Parameters**:
- `<value>`: The value to set (can be string, number, boolean, object, etc.)

**Example**:
```
anx age-input set 25
anx is-admin set true
```

#### set_form

**Description**: Form batch assignment; only valid for form components. By default, it performs incremental update, only modifying parameters defined in the JSON.

**Usage**:
```
anx <cardKey> set_form <JSON> [--replace]
```

**Parameters**:
- `<JSON>`: JSON string representing form data
- `--replace`: Optional flag to perform full replacement instead of incremental update

**Example**:
```
# Incremental update (default)
anx registration-form set_form '{"username": "john", "email": "john@example.com"}'

# Full replacement
anx registration-form set_form '{"username": "john"}' --replace
```

#### clear

**Description**: Clear content/value; do not reset to default value

**Usage**:
```
anx <cardKey> clear
```

**Example**:
```
anx search-input clear
```

#### reset

**Description**: Reset to initial default value; and clear validation status

**Usage**:
```
anx <cardKey> reset
```

**Example**:
```
anx form-container reset
```

### 3. Selection Commands

#### select

**Description**: Single selection/dropdown select an item; triggers option change

**Usage**:
```
anx <cardKey> select <value>
```

**Parameters**:
- `<value>`: The value to select

**Example**:
```
anx country-select select "United States"
anx gender-select select male
```

#### add_option

**Description**: Multi-select mode: add an item

**Usage**:
```
anx <cardKey> add_option <value>
```

**Parameters**:
- `<value>`: The value to add

**Example**:
```
anx interests-select add_option "Programming"
anx roles-select add_option admin
```

#### remove_option

**Description**: Multi-select mode: remove an item

**Usage**:
```
anx <cardKey> remove_option <value>
```

**Parameters**:
- `<value>`: The value to remove

**Example**:
```
anx interests-select remove_option "Gaming"
anx roles-select remove_option guest
```

#### check

**Description**: Check; checkbox/switch universal

**Usage**:
```
anx <cardKey> check
```

**Example**:
```
anx terms-checkbox check
anx dark-mode-switch check
```

#### uncheck

**Description**: Uncheck

**Usage**:
```
anx <cardKey> uncheck
```

**Example**:
```
anx newsletter-checkbox uncheck
anx notifications-switch uncheck
```

### 4. Interaction Event Commands

#### tap

**Description**: Universal tap/click; cross-platform unified replacement for click

**Usage**:
```
anx <cardKey> tap
```

**Example**:
```
anx submit-button tap
anx menu-item tap
```

#### double_tap

**Description**: Double tap/double click

**Usage**:
```
anx <cardKey> double_tap
```

**Example**:
```
anx image-viewer double_tap
```

#### long_press

**Description**: Long press/long press trigger

**Usage**:
```
anx <cardKey> long_press
```

**Example**:
```
anx file-item long_press
```

#### submit

**Description**: Submit form; automatically triggers validation

**Usage**:
```
anx <cardKey> submit
```

**Example**:
```
anx login-form submit
```

#### cancel

**Description**: Cancel/close popup/drawer/step

**Usage**:
```
anx <cardKey> cancel
```

**Example**:
```
anx popup-dialog cancel
anx drawer-panel cancel
```

#### confirm

**Description**: Confirm operation; popup confirmation/step confirmation

**Usage**:
```
anx <cardKey> confirm
```

**Example**:
```
anx delete-confirm confirm
anx step-form confirm
```

### 5. Display Control Commands

#### expand

**Description**: Expand component (collapse panel/dropdown panel)

**Usage**:
```
anx <cardKey> expand
```

**Example**:
```
anx settings-panel expand
anx dropdown-menu expand
```

#### collapse

**Description**: Collapse component

**Usage**:
```
anx <cardKey> collapse
```

**Example**:
```
anx settings-panel collapse
anx dropdown-menu collapse
```

#### show

**Description**: Show component

**Usage**:
```
anx <cardKey> show
```

**Example**:
```
anx error-message show
```

#### hide

**Description**: Hide component

**Usage**:
```
anx <cardKey> hide
```

**Example**:
```
anx error-message hide
```

### 6. Page Navigation Commands

#### goto

**Description**: Navigate to the page/route

**Usage**:
```
anx <cardKey> goto
```

**Example**:
```
anx dashboard-link goto
```

#### back

**Description**: Return to previous page; usually used for page/nav components

**Usage**:
```
anx <cardKey> back
```

**Example**:
```
anx nav-bar back
```

#### reload

**Description**: Reload/refresh current content

**Usage**:
```
anx <cardKey> reload
```

**Example**:
```
anx data-grid reload
```

#### scroll_to

**Description**: Scroll to the component position; and center display

**Usage**:
```
anx <cardKey> scroll_to
```

**Example**:
```
anx footer scroll_to
```

### 7. State Control Commands

#### enable

**Description**: Enable component; remove disabled state

**Usage**:
```
anx <cardKey> enable
```

**Example**:
```
anx submit-button enable
```

#### disable

**Description**: Disable component; cannot interact

**Usage**:
```
anx <cardKey> disable
```

**Example**:
```
anx submit-button disable
```

#### validate

**Description**: Manually trigger validation; do not submit

**Usage**:
```
anx <cardKey> validate
```

**Example**:
```
anx email-input validate
anx form-container validate
```

## Command Execution

When executing ANX CLI commands:

1. The `cardKey` is used to locate the specific component in the ANX application
2. The specified `action` is performed on that component
3. The result is returned in JSON format

## Error Handling

If an error occurs during command execution:

- Invalid `cardKey`: Returns an error indicating the component was not found
- Invalid `action`: Returns an error indicating the action is not supported
- Execution error: Returns an error with details about the failure
- Parameter error: Returns an error indicating invalid parameters

## Example Usage

### Querying Component Information
```bash
# Get component configuration
anx user-profile get_config

# Get form data
anx login-form get_form

# Get component value
anx username-input get_value

# Get validation result
anx email-input get_validate
```

### Setting Values and Interacting
```bash
# Fill input field
anx username-input fill john_doe

# Set value
anx age-input set 25

# Submit form
anx login-form submit

# Tap button
anx submit-button tap
```

### Selection Operations
```bash
# Select dropdown option
anx country-select select "United States"

# Add multi-select option
anx interests-select add_option "Programming"

# Check checkbox
anx terms-checkbox check
```

### Display and Navigation
```bash
# Show component
anx error-message show

# Expand panel
anx settings-panel expand

# Navigate to page
anx dashboard-link goto

# Scroll to component
anx footer scroll_to
```

## Use Cases

- **Development**: Debug and inspect component configurations during development
- **Testing**: Verify component behavior and data
- **Automation**: Integrate with CI/CD pipelines for automated testing
- **Monitoring**: Check component status and configuration in production
- **Scripting**: Create automation scripts for repetitive tasks

## Implementation Notes

- The CLI commands are typically executed through the ANX development server
- Command execution requires access to the ANX application context
- Results are returned in structured JSON format for easy parsing
- Some commands may require additional permissions depending on the component
- For commands with parameters containing spaces, wrap the parameter in quotes
- JSON parameters should be properly escaped when used in shell commands
