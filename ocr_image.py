#!/usr/bin/env python3
# coding=utf-8

from PIL import Image
from qwenvl import qwenvl_with_api
from qwenvl import encode_image
from format_tool import draw_bbox
from format_tool import clean_and_format_html
from format_tool import smart_resize


def recognize_image_text_and_parse_html(image_path, model_id='qwen2.5-vl-72b-instruct'):
    '''
    识别图片并将图片还原成HTML
    '''

    full_predict = format_image_to_html(image_path, model_id)

    return clean_and_format_html(full_predict)


def recognize_image_text_and_position(image_path, model_id='qwen2.5-vl-72b-instruct'):
    '''
    识别图片中文本的坐标
    '''

    full_predict = format_image_to_html(image_path, model_id)

    original_width, original_height = acquire_image_width_and_height(
        image_path)

    resized_height, resized_width = smart_resize(
        original_height, original_width
    )

    draw_bbox(image_path, resized_width, resized_height, full_predict)


def acquire_image_width_and_height(image_path):
    '''
    获取图片的宽度和高度
    '''
    with open(image_path, "rb") as image_file:
        image = Image.open(image_file)
        return image.width, image.height


def format_image_to_html(image_path, model_id='qwen2.5-vl-72b-instruct'):
    '''
    将图片格式化成HTML
    '''
    system_prompt = 'You are an AI specialized in recognizing and extracting text from images. Your mission is to analyze the image document and generate the result in QwenVL Document Parser HTML format using specified tags while maintaining user privacy and data integrity.'
    prompt = 'QwenVL HTML'

    base64_image = encode_image(image_path)

    return qwenvl_with_api(base64_image, prompt, system_prompt, model_id)


def extract_text_from_document(image_path, model_id='qwen2.5-vl-3b-instruct'):
    '''
    从图片中提取文字内容
    '''
    system_prompt = 'You are a helpful assistant.'
    prompt = 'Read all the text in the image.'

    base64_image = encode_image(image_path)

    qwenvl_with_api(base64_image, prompt, system_prompt, model_id)


if __name__ == "__main__":

    image_path = './static/images/scan_copy_contract.png'
    model_id = 'qwen2.5-vl-72b-instruct'

    recognize_image_text_and_position(image_path, model_id)
    # full_html = recognize_image_text_and_parse_html(image_path)
    # print(full_html)
