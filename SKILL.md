---
name: |
  ms-image-skill
description: |
  基于魔搭生图API的图像生成技能，当用户需要生成图像时调用
---

# 技能简介

* 基于魔搭生图API的图像生成技能，当用户需要生成图像时调用

# 指令

## 图像生成

* 第1步：选择图像尺寸
  - 1280x720
  - 720x1280
  - 1024x1024
  - 1024x768
  - 768x1024
  - 640x960
  - 854x1536
  - 1536x854

* 第2步：输入提示词。
* 第3步: 调用`python3 scripts/img_gen.py --prompt "提示词" --size "图像尺寸" --output_dir ms_img_outputs`生成图像。

# 新增配置

* 调用`python3 scripts/add_config.py --token "用户TOKEN"`新增本地配置。
