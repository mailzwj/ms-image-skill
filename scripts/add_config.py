#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--token", type=str, help="令牌")

args = parser.parse_args()
token = args.token

if not token:
    print("请输入令牌")
    exit(1)

cur_dir = os.path.dirname(__file__)

cfg_file = os.path.join(cur_dir, "..", "config.json")

cfg_content = json.load(open(cfg_file, "r", encoding="utf-8"))

cfg_content["api_key"] = token

json.dump(cfg_content, open(cfg_file, "w", encoding="utf-8"), ensure_ascii=False, indent=4)

