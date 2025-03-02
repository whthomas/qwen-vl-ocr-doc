#!/usr/bin/env python3
# coding=utf-8

from openai import OpenAI
import os
import base64
from dotenv import load_dotenv

# Load API keys from .env.example
load_dotenv(dotenv_path=".env.local")

client = OpenAI(
    # If the environment variable is not configured, please replace the following line with the Dashscope API Key: api_key="sk-xxx".
    api_key=os.getenv('BAILIAN_API_KEY'),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)


def qwenvl_with_api(base64_image, prompt, system_prompt="You are a helpful assistant.", model_id="qwen2.5-vl-72b-instruct"):

    messages = [
        {
            "role": "system",
            "content": [{"type": "text", "text": system_prompt}]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    # 传入特定格式的图片信息加上图片对应的Base64编码值
                    # PNG image:  f"data:image/png;base64,{base64_image}"
                    # JPEG image: f"data:image/jpeg;base64,{base64_image}"
                    # WEBP image: f"data:image/webp;base64,{base64_image}"
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                },
                {"type": "text", "text": prompt},
            ],
        }
    ]

    completion = client.chat.completions.create(
        model=model_id,
        messages=messages,
        stream=True,
    )

    full_text = ""
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            full_text += chunk.choices[0].delta.content
            print(chunk.choices[0].delta.content, end="")

    return full_text


def encode_image(image_path):
    '''
    对文件进行编码
    '''
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
