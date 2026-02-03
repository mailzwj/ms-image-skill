#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import os
import time
import json
import argparse
from PIL import Image
from io import BytesIO

parser = argparse.ArgumentParser()
# parser.add_argument("--token", help="令牌")
parser.add_argument("--prompt", help="提示词")
parser.add_argument("--size", help="图像尺寸", default='1280x720')
parser.add_argument("--output_dir", help="保存路径", default='ms_img_outputs')

args = parser.parse_args()

# print("arguments:", parser.parse_args().prompt)

base_url = 'https://api-inference.modelscope.cn/'

cur_dir = os.path.dirname(os.path.abspath(__file__))
cfg_file = os.path.join(cur_dir, "..", "config.json")
cfg_json = json.load(open(cfg_file, "r", encoding="utf-8"))

api_key = cfg_json.get("api_key")

# if api_key is None:
#     api_key = cfg_json.get("api_key")

if not api_key:
    print("未识别到令牌配置，你可以这样添加令牌：\n> 指挥skill“增加配置”，添加本地配置，永久生效")
    exit(1)

common_headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

# print("token:", api_key)
# print("size:", args.size)
# print("prompt:", args.prompt)

response = requests.post(
    f"{base_url}v1/images/generations",
    headers={**common_headers, "X-ModelScope-Async-Mode": "true"},
    data=json.dumps({
        "model": "Qwen/Qwen-Image-2512",
        "loras": "Wuli-Art/Qwen-Image-2512-Turbo-LoRA-2-Steps",
        "prompt": args.prompt,
        "size": args.size,
        "steps": 2,
        "guidance": 1.5
    }, ensure_ascii=False).encode('utf-8')
)

print("response:", response.json())

response.raise_for_status()
task_id = response.json()["task_id"]

print(f"Task ID: {task_id}")

while True:
    result = requests.get(
        f"{base_url}v1/tasks/{task_id}",
        headers={**common_headers, "X-ModelScope-Task-Type": "image_generation"},
    )
    result.raise_for_status()
    data = result.json()

    if data["task_status"] == "SUCCEED":
        image = Image.open(BytesIO(requests.get(data["output_images"][0]).content))
        output_dir = args.output_dir
        if os.path.exists(output_dir) == False:
            os.makedirs(output_dir)
        image.save(f"{output_dir}/result_{time.strftime('%Y%m%d%H%M%S')}.png")
        break
    elif data["task_status"] == "FAILED":
        print("Image Generation Failed.")
        break

    time.sleep(3)
