# ANX Card Node Usage Guide

## Overview

This guide explains how to use ANX Card Node format (`<x kind cardKey>`) and the ANX CLI commands to interact with ANX components.

## Card Node Format

### Basic Structure

The ANX Card Node format uses the `<x>` tag with two required attributes:

```html
<x kind cardKey>
  Content area
</x>
```

- **kind**: Specifies the component type (e.g., form, input, button, etc.)
- **cardKey**: Unique identifier for the component, used for CLI commands

### Example

```html
<x form card_1774672305364_5722>
  ## User Registration Form
  
  <x input card_1774672305364_7557>
  **username:** Please enter username
  </x>
  
  <!-- Other components -->
  
</x>
```

## CLI Commands

### Basic Format

```bash
anx <cardKey> <action> <params>
```

- **cardKey**: The unique identifier of the component
- **action**: The action to perform (e.g., get_form, set_form, get_value, set_value)
- **params**: Parameters for the action (usually JSON format)

### Common Commands

#### 1. Get Form Data

```bash
anx card_1774672305364_5722 get_form
```

#### 2. Set Form Data

```bash
anx card_1774672305364_5722 set_form '{"username": "John", "email": "john@example.com"}'
```

#### 3. Get Field Value

```bash
anx card_1774672305364_7557 get_value
```

#### 4. Set Field Value

```bash
anx card_1774672305364_7557 set_value '{"value": "John"}'
```

## Example Form Analysis

Let's analyze the provided user registration form:

### Form Structure

```html
<x form card_1774672305364_5722>
  ## 用户注册表单
  
  <x input card_1774672305364_7557>
  **username:** 请输入用户名
  </x>
  
  <x input card_1774672305364_2819>
  **email:** 请输入邮箱
  </x>
  
  <x date card_1774672305364_5872>
  **birthday:** 请选择出生日期
  </x>
  
  <x input card_1774672305364_4370>
  **age:** 请输入年龄
  </x>
  
  <x text card_1774672305364_4433>
  **成年年数:**
  </x>
  
  <x options card_1774672305364_5510>
  **gender:**
  
  - 男
  - 女
  - 其他
  
  </x>
  
  <x checkbox card_1774672305364_7560>
  **hobbies:**
  
  - 阅读
  - 运动
  - 音乐
  - 旅行
  
  </x>
  
  <x textarea card_1774672305364_5254>
  **description:**
  
  ```
  请输入个人简介
  ```
  </x>
  
  <x list card_1774672305364_1056>
  ## 技能列表
  
  | 技能名称 | 熟练度 | 使用年限 |
  | --- | --- | --- |
  | JavaScript | advanced | 5 |
  | Vue.js | intermediate | 3 |
  
  </x>
  
  <x button card_1774672305364_4211>
  [提交](/submit)
  </x>
</x>
```

### Component Types

| Component Type | cardKey | Description |
|----------------|---------|-------------|
| form | card_1774672305364_5722 | Main form container |
| input | card_1774672305364_7557 | Username input field |
| input | card_1774672305364_2819 | Email input field |
| date | card_1774672305364_5872 | Birthday date picker |
| input | card_1774672305364_4370 | Age input field |
| text | card_1774672305364_4433 | Adult years display |
| options | card_1774672305364_5510 | Gender selection |
| checkbox | card_1774672305364_7560 | Hobbies selection |
| textarea | card_1774672305364_5254 | Personal description |
| list | card_1774672305364_1056 | Skills list |
| button | card_1774672305364_4211 | Submit button |

## Usage Examples

### 1. Fill and Submit the Form

```bash
# Set form data
anx card_1774672305364_5722 set_form '{
  "username": "张三",
  "email": "zhangsan@example.com",
  "birthday": "1990-01-01",
  "age": 36,
  "gender": "男",
  "hobbies": ["阅读", "运动"],
  "description": "喜欢编程和旅行",
  "技能列表": [
    {"技能名称": "JavaScript", "熟练度": "advanced", "使用年限": 5},
    {"技能名称": "Vue.js", "熟练度": "intermediate", "使用年限": 3},
    {"技能名称": "Python", "熟练度": "beginner", "使用年限": 1}
  ]
}'

# Submit the form
anx card_1774672305364_4211 tap
```

### 2. Update Specific Fields

```bash
# Update username
anx card_1774672305364_7557 set_value '{"value": "李四"}'

# Update age
anx card_1774672305364_4370 set_value '{"value": 28}'

# Update gender
anx card_1774672305364_5510 set_value '{"value": "女"}'

# Update hobbies
anx card_1774672305364_7560 set_value '{"value": ["阅读", "音乐", "旅行"]}'
```

### 3. Get Form Data

```bash
# Get entire form data
anx card_1774672305364_5722 get_form

# Get specific field value
anx card_1774672305364_7557 get_value
```

### 4. Update Skills List

```bash
# Update skills list
anx card_1774672305364_1056 set_value '{"value": [
  {"技能名称": "JavaScript", "熟练度": "advanced", "使用年限": 6},
  {"技能名称": "Vue.js", "熟练度": "advanced", "使用年限": 4},
  {"技能名称": "React", "熟练度": "intermediate", "使用年限": 2}
]}'
```

## Field Value Formats

### Input Fields

```json
{"value": "text value"}
```

### Date Fields

```json
{"value": "2023-12-31"}
```

### Number Fields

```json
{"value": 25}
```

### Options Fields (Single Selection)

```json
{"value": "男"}
```

### Checkbox Fields (Multiple Selection)

```json
{"value": ["阅读", "运动"]}
```

### Textarea Fields

```json
{"value": "This is a multi-line\ndescription"}
```

### List Fields

```json
{"value": [
  {"技能名称": "JavaScript", "熟练度": "advanced", "使用年限": 5},
  {"技能名称": "Vue.js", "熟练度": "intermediate", "使用年限": 3}
]}
```

## Best Practices

1. **CardKey Naming**: Use descriptive and unique cardKeys for easier identification
2. **Data Validation**: Validate data before setting it to ensure it matches expected formats
3. **Error Handling**: Handle errors gracefully when using CLI commands
4. **Form Structure**: Keep form structure consistent for easier maintenance
5. **Documentation**: Document cardKeys and their purposes for team collaboration

## Troubleshooting

### Common Issues

1. **Invalid cardKey**: Make sure you're using the correct cardKey for the component
2. **Incorrect data format**: Ensure data matches the expected format for the field type
3. **Permission issues**: Check if you have the necessary permissions to modify the component
4. **Component not found**: Verify the component exists and is properly registered

### Debugging Tips

- Use `get_form` to see the current state of the form
- Test with simple values first before complex data structures
- Check console logs for error messages
- Verify component types and cardKeys are correct

## Conclusion

The ANX Card Node format provides a powerful way to define interactive components, while the CLI commands offer a flexible method to interact with and modify these components. By following this guide, you can effectively work with ANX components in your applications.
