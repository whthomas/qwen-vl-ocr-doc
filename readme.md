# ocr_image.py

## 项目简介

`ocr_image.py` 是一个用于识别图片中的文本，并进行相关处理的 Python 脚本。它包含以下功能：

*   从图片中提取文字内容。
*   识别图片中文本的坐标。
*   识别图片并将图片还原成HTML。

## 使用方法

### API 配置

本项目使用了阿里云的百炼平台的 API，需要配置 `API_KEY` 环境变量。

1.  **获取 API Key:** 前往 [百炼官网](https://bailian.console.aliyun.com/?apiKey=1#/api-key) 获取 API Key。
2.  **配置环境变量:**
    *   在 `.env.local` 文件中添加 `BAILIAN_API_KEY` 变量，并将你的 API Key 填入。
        ```
        BAILIAN_API_KEY=你的API密钥
        ```
    *   或者，你也可以直接在系统环境变量中配置 `BAILIAN_API_KEY`。

配置完成后，请确保重新启动你的 Python 环境，以使环境变量生效。


### 1. 识别图片文本

使用 `extract_text_from_document` 函数可以从图片中提取文字内容。

```python
from ocr_image import extract_text_from_document

image_path = './static/images/scan_copy_contract.png'
model_id = 'qwen2.5-vl-3b-instruct'

extract_text_from_document(image_path, model_id)
```

### 2. 识别图片文本位置

使用 `recognize_image_text_and_position` 函数可以识别图片中文本的坐标，并将结果保存到指定的图片文件中。

```python
from ocr_image import recognize_image_text_and_position

image_path = './static/images/scan_copy_contract.png'
model_id = 'qwen2.5-vl-72b-instruct'
save_output_image_path = './output/output.jpg'

recognize_image_text_and_position(image_path, model_id, save_output_image_path)
```

### 3. 识别图片并还原成HTML

使用 `recognize_image_text_and_parse_html` 函数可以识别图片并将图片还原成HTML，并将HTML内容保存到指定目录下的 `index.html` 文件中。

```python
from ocr_image import recognize_image_text_and_parse_html

image_path = './static/images/scan_copy_contract.png'
output_path = './output'
model_id = 'qwen2.5-vl-72b-instruct'

recognize_image_text_and_parse_html(image_path, output_path, model_id)
```

## 示例

以下是一个完整的示例，演示如何使用 `ocr_image.py` 脚本：

```python
#!/usr/bin/env python3
# coding=utf-8

from ocr_image import recognize_image_text_and_position
from ocr_image import recognize_image_text_and_parse_html

image_path = './static/images/scan_copy_contract.png'
model_id = 'qwen2.5-vl-72b-instruct'

# 识别图片文本位置
recognize_image_text_and_position(image_path, model_id, "./output/output.jpg")

# 识别图片并还原成HTML
output_path = "./output"
recognize_image_text_and_parse_html(image_path, output_path, model_id)
```
