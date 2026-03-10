# ANX Frontend Interaction Protocol

## Overview

ANX (AI Native Ex) is an Agent-friendly frontend coding format designed to establish a unified standard for frontend interactions. This protocol defines how Agents can interact with frontend applications without relying on traditional browsers or apps.

## Core Concepts

### Map Usage in ANX Protocol

In ANX protocol, `map` refers to a mapping between field names, not between field names and values. This is a fundamental concept that ensures consistent data handling across the protocol.

#### paramMap

`paramMap` is used to map table field names to source field names. It follows the structure:

```json
{
  "paramMap": {
    "table_field_name": "source_field_name"
  }
}
```

#### uniqueMap

`uniqueMap` is used to map table unique identifier field names to source field names. It follows the structure:

```json
{
  "uniqueMap": {
    "table_unique_field_name": "source_unique_field_name"
  }
}
```

### Key Principles

1. **Consistency**: All map structures in the protocol follow the same pattern of field name to field name mapping
2. **Clarity**: Map keys always represent table field names, while values represent source field names
3. **Flexibility**: Maps can contain multiple field mappings as needed

### Common Field Definitions

#### must

`must` is a boolean field that indicates whether a field is required. When set to `true`, the field must be provided and cannot be empty.

```json
{
  "must": true
}
```

#### title

`title` is a string field that represents the display name of a field, shown to users in the interface.

```json
{
  "title": "User Name"
}
```

#### nick

`nick` is a string field that represents the field name used for data binding and submission. It should be unique within the context of the component.

```json
{
  "nick": "userName"
}
```

## Protocol Components

The ANX protocol consists of several key components:

- **Navigation**: Defines menu structures and navigation flows
- **Forms**: Defines form fields, validation rules, and submission behavior
- **Tables**: Defines table structures, columns, and data sources
- **Triggers and Taps**: Defines event-driven actions and interactions
- **UpdateData**: Defines how to update or insert data based on unique identifiers

## Best Practices

- Follow the field name to field name mapping convention for all map structures
- Use descriptive and consistent naming for both table fields and source fields
- Ensure all required fields are properly mapped in paramMap and uniqueMap
- Validate data before using it in updateData operations
- Handle errors gracefully when performing data operations

## Usage Guidelines

1. **Configuration Files**: Use JSON format for all protocol configurations
2. **Field Naming**: Use snake_case or camelCase consistently throughout the application
3. **Documentation**: Maintain clear and up-to-date documentation for all protocol components
4. **Validation**: Implement client-side validation where appropriate
5. **Error Handling**: Implement proper error handling for all operations

## Implementation Notes

- The ANX protocol is designed to be flexible and adaptable to different frontend frameworks
- Implementations should follow the protocol specifications to ensure compatibility
- Extensions to the protocol should be documented and follow the same design principles
- Version control should be used to track changes to the protocol specifications