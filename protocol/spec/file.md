# 文件上传组件规范

## 概述

文件上传组件用于上传和管理各种类型的文件，支持单文件和多文件上传。

## 基本结构

```json
{
  "kind": "file",
  "multiple": false,
  "accept": "文件类型",
  "maxSize": 10485760,
  "required": false,
  "value": "文件路径",
  "preview": true
}
```

## 字段说明

| 字段名 | 类型 | 必选 | 说明 |
|-------|------|------|------|
| kind | string | 是 | 组件类型，固定为 "file" |
| multiple | boolean | 否 | 是否支持多文件上传，默认为 false |
| accept | string | 否 | 可接受的文件类型，如 ".jpg,.png" 或 "image/*" |
| maxSize | number | 否 | 文件最大大小（字节），默认为 10MB |
| required | boolean | 否 | 是否必填，默认为 false |
| value | string/array | 否 | 文件路径或文件路径数组 |
| preview | boolean | 否 | 是否支持文件预览，默认为 true |

## 示例

### 单文件上传

```json
{
  "kind": "file",
  "id": "avatar",
  "name": "头像",
  "label": "请上传头像",
  "accept": "image/*",
  "maxSize": 5242880,
  "required": true,
  "description": "支持 JPG、PNG 格式，大小不超过 5MB"
}
```

### 多文件上传

```json
{
  "kind": "file",
  "id": "attachments",
  "name": "附件",
  "label": "请上传附件",
  "multiple": true,
  "accept": ".doc,.docx,.pdf,.txt",
  "maxSize": 20971520,
  "description": "支持 Word、PDF、文本文件，单个文件大小不超过 20MB"
}
```

### 带预览的文件上传

```json
{
  "kind": "file",
  "id": "productImages",
  "name": "产品图片",
  "label": "请上传产品图片",
  "multiple": true,
  "accept": "image/*",
  "maxSize": 10485760,
  "preview": true,
  "description": "支持 JPG、PNG 格式，大小不超过 10MB"
}
```