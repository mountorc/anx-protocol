# 语音录制组件规范

## 概述

语音录制组件用于录制和播放语音，支持录音时长控制、格式选择等功能。

## 基本结构

```json
{
  "type": "voice",
  "maxDuration": 60,
  "format": "audio/mp3",
  "required": false,
  "value": "音频文件路径",
  "controls": true
}
```

## 字段说明

| 字段名 | 类型 | 必选 | 说明 |
|-------|------|------|------|
| type | string | 是 | 组件类型，固定为 "voice" |
| maxDuration | number | 否 | 最大录音时长（秒），默认为 60 秒 |
| format | string | 否 | 音频格式，如 "audio/mp3"、"audio/wav" 等 |
| required | boolean | 否 | 是否必填，默认为 false |
| value | string | 否 | 音频文件路径 |
| controls | boolean | 否 | 是否显示播放控制，默认为 true |

## 示例

### 基本语音录制

```json
{
  "type": "voice",
  "id": "voiceMessage",
  "name": "语音消息",
  "label": "请录制语音消息",
  "maxDuration": 60,
  "format": "audio/mp3",
  "required": true,
  "description": "最长录制 60 秒"
}
```

### 带播放控制的语音录制

```json
{
  "type": "voice",
  "id": "interviewRecording",
  "name": "面试录音",
  "label": "请录制面试回答",
  "maxDuration": 120,
  "format": "audio/wav",
  "controls": true,
  "description": "最长录制 2 分钟，支持播放和重录"
}
```

### 可选语音录制

```json
{
  "type": "voice",
  "id": "feedbackVoice",
  "name": "语音反馈",
  "label": "语音反馈（可选）",
  "maxDuration": 30,
  "format": "audio/mp3",
  "required": false,
  "description": "您可以录制语音反馈，最长 30 秒"
}
```