# 视频上传组件规范

## 概述

视频上传组件用于上传和播放视频，支持视频时长控制、格式选择等功能。

## 基本结构

```json
{
  "type": "video",
  "id": "唯一标识符",
  "name": "组件名称",
  "label": "标签",
  "multiple": false,
  "accept": "video/*",
  "maxSize": 104857600,
  "maxDuration": 600,
  "required": false,
  "description": "描述",
  "value": "视频文件路径",
  "controls": true,
  "preview": true
}
```

## 字段说明

| 字段名 | 类型 | 必选 | 说明 |
|-------|------|------|------|
| type | string | 是 | 组件类型，固定为 "video" |
| id | string | 是 | 组件唯一标识符 |
| name | string | 否 | 组件名称 |
| label | string | 否 | 组件标签 |
| multiple | boolean | 否 | 是否支持多视频上传，默认为 false |
| accept | string | 否 | 可接受的视频类型，如 "video/*" 或 ".mp4,.avi" |
| maxSize | number | 否 | 文件最大大小（字节），默认为 100MB |
| maxDuration | number | 否 | 最大视频时长（秒），默认为 600 秒（10 分钟） |
| required | boolean | 否 | 是否必填，默认为 false |
| description | string | 否 | 组件描述 |
| value | string/array | 否 | 视频文件路径或视频文件路径数组 |
| controls | boolean | 否 | 是否显示播放控制，默认为 true |
| preview | boolean | 否 | 是否支持视频预览，默认为 true |

## 示例

### 单个视频上传

```json
{
  "type": "video",
  "id": "introductionVideo",
  "name": "介绍视频",
  "label": "请上传介绍视频",
  "accept": "video/mp4",
  "maxSize": 52428800,
  "maxDuration": 300,
  "required": true,
  "description": "支持 MP4 格式，大小不超过 50MB，时长不超过 5 分钟"
}
```

### 多个视频上传

```json
{
  "type": "video",
  "id": "trainingVideos",
  "name": "培训视频",
  "label": "请上传培训视频",
  "multiple": true,
  "accept": "video/*",
  "maxSize": 104857600,
  "maxDuration": 600,
  "description": "支持多种视频格式，单个文件大小不超过 100MB，时长不超过 10 分钟"
}
```

### 带预览的视频上传

```json
{
  "type": "video",
  "id": "productDemo",
  "name": "产品演示",
  "label": "请上传产品演示视频",
  "accept": "video/mp4",
  "maxSize": 104857600,
  "maxDuration": 600,
  "controls": true,
  "preview": true,
  "description": "支持 MP4 格式，大小不超过 100MB，时长不超过 10 分钟"
}
```