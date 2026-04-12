# Template Processing Guide

## Overview

This guide describes how templates are processed in ANX frontend interaction protocol, focusing on variable and formula substitution in templates.

## Variable/Formula Substitution

ANX supports two syntaxes for variable and formula substitution in templates:

1. **Double curly braces syntax**: `{{formula}}`
2. **Dollar sign syntax**: `${formula}`

### Basic Usage

```json
{
  "content": "Hello, {{nick1}}! Welcome, ${nick2}!"
}
```

In the example above, `{{nick1}}` will be replaced with the value of the `nick1` variable, and `${nick2}` will be replaced with the value of the `nick2` variable.

## Formula Support

The content inside `{{}}` and `${}` is not just a simple variable name - it can be a full formula. This allows for complex calculations and expressions.

### Example Formulas

```json
{
  "content": "Total: {{price * quantity}}",
  "content": "Discount: ${price * 0.1}",
  "content": "Final price: {{price * (1 - discount)}}",
  "content": "Welcome {{user.name}}, your balance is ${account.balance}"
}
```

## Syntax Rules

### Variables

- **Simple variables**: `{{variable}}` or `${variable}`
- **Nested variables**: `{{object.property}}` or `${object.property}`
- **Array access**: `{{array[0]}}` or `${array[0]}`

### Formulas

- **Arithmetic operations**: `{{a + b}}`, `${a * b}`, `${a / b}`, `${a - b}`
- **Comparison operations**: `{{a > b}}`, `${a < b}`, `${a == b}`
- **Logical operations**: `{{a && b}}`, `${a || b}`, `${!a}`
- **Function calls**: `{{Math.max(a, b)}}`, `${formatDate(date)}`
- **Conditional statements**: `{{if (condition) then value1 else value2}}`, `${if (condition) then value1 else value2}`

## Example Usage

### Basic Variable Substitution

```json
{
  "content": "Hello, {{username}}!"
}
```

### Formula Substitution

```json
{
  "content": "Your order total is {{subtotal + tax - discount}}",
  "content": "You have ${items.length} items in your cart"
}
```

### Complex Expressions

```json
{
  "content": "{{if (user.isMember) then 'Welcome back, ' + user.name else 'Hello, guest'}}",
  "content": "${items.map(item => item.name).join(', ')}"
}
```

### Conditional Statements (if then)

```json
{
  "content": "{{if (age >= 18) then 'Adult' else 'Minor'}}",
  "content": "${if (score >= 90) then 'A' else if (score >= 80) then 'B' else 'C'}",
  "content": "Your discount: {{if (membershipLevel === 'gold') then price * 0.2 else if (membershipLevel === 'silver') then price * 0.1 else 0}}"
}
```

## Best Practices

- Use descriptive variable names
- Keep formulas simple and readable
- Test complex formulas to ensure they evaluate correctly
- Use consistent syntax (either `{{}}` or `${}`) throughout your application
- Avoid overly complex formulas in template content

## Performance Considerations

- Formulas are evaluated at runtime, so complex formulas may impact performance
- Consider pre-calculating complex values and storing them as simple variables
- Use caching for expensive calculations

## Error Handling

- If a formula contains an error, it will typically be replaced with an empty string or error message
- Always validate formulas during development to catch errors early
- Provide fallback values for optional variables
