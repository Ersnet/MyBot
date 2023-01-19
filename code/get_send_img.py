import random
import time
from lxml import etree
import requests
import re
import cv2
import numpy as np
import asyncio
import aiohttp
import os
import shutil
import json
from PIL import ImageDraw, ImageFont, Image

def get_qq_image(cq):
    text = re.finditer("url=.*", cq)
    str_t = text.__next__().group()
    url = str_t.replace("url=", "").replace("]", "")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56"
    }
    with requests.get(url, headers=headers) as resp:
        img = resp.content
    with open(r"D:\bot\temp_qq\img.jpg", mode="wb") as f:
        f.write(img)

def get_img2t(img):
    arr = ["#", "+", "-", "."]
    img = cv2.imread(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h = np.size(gray, 0)
    w = np.size(gray, 1)
    # 初始化与原图一样尺寸的黑色图片
    res = np.ndarray([h, w])
    font = cv2.FONT_HERSHEY_SIMPLEX
    for i in range(0, h, 5):
        for j in range(0, w, 5):
            # 获取灰度值对应字符
            t = arr[round(3 - gray[i, j] / 255 * 3)]
            # 绘制字符
            cv2.putText(res, t, (j, i), font, 0.1, color=(255, 255, 255))
    # 显示结果图
    # 保存结果图
    cv2.imwrite(r"D:\bot\data\images\img2t.jpg", res)

def get_setu(sort):
    url = "https://moe.jitsu.top/api"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46"
    }
    params = {
        "sort": sort
    }

    with requests.get(url, headers=headers, params=params) as resp:
        img = resp.content
    with open(r"D:\bot\data\images\setu.png", mode="wb") as f:
        f.write(img)

def save_qq_image(cq):
    text = re.finditer("url=.*", cq)
    name_re = re.finditer("保存.*?CQ:", cq)

    str_t = text.__next__().group()
    name = name_re.__next__().group().replace("保存 ", "").replace("[CQ:", "")

    url = str_t.replace("url=", "").replace("]", "")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56"
    }
    with requests.get(url, headers=headers) as resp:
        img = resp.content
    with open(f"D:\\bot\\data\\images\\{name}", mode="wb") as f:
        f.write(img)

def get_world_news():
    url = "https://api.vvhan.com/api/60s"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56"
    }
    with requests.get(url, headers=headers) as resp:
        img = resp.content
    with open("D:\\bot\\data\\images\\news.png", mode="wb") as f:
        f.write(img)

def get_moyu_date():
    url = "https://api.vvhan.com/api/moyu"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56"
    }
    with requests.get(url, headers=headers) as resp:
        img = resp.content
    with open("D:\\bot\\data\\images\\moyu.png", mode="wb") as f:
        f.write(img)

def get_latex(text):
    url = "https://latex.codecogs.com/png.image?\huge&space;\dpi{200}" + text
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56"
    }
    with requests.get(url, headers=headers) as tex:
        pic = tex.content
    with open(r"D:\bot\data\images\tex.png", mode="wb") as f:
        f.write(pic)

def get_exact_v_latex(text):
    url = "https://latex.codecogs.com/png.image?\huge&space;\dpi{200}" + text
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56"
    }
    with requests.get(url, headers=headers) as tex:
        pic = tex.content
    with open(r"D:\bot\data\images\exact.png", mode="wb") as f:
        f.write(pic)

async def get_emoji_mix(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46"
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as emoji_img:
            if emoji_img.status == 200:
                with open("D:\\bot\\data\\images\\emoji.png", mode="wb") as f:
                    f.write(await emoji_img.content.read())
            else:
                pass

def get_qq_avatar(qq):
    url = "http://q.qlogo.cn/headimg_dl"
    params = {
        "dst_uin": qq,
        "spec": 640,
        "img_type": "jpg"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56"
    }
    with requests.get(url, params=params, headers=headers) as resp:
        img = resp.content
    with open(r"D:\bot\data\images\qq.png", mode="wb") as f:
        f.write(img)

def get_dingzhen_face():
    url1 = "http://api.sevin.cn/api/dingzhen.php"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56"
    }
    with requests.get(url1, headers=headers) as resp:
        url2 = resp.text
    with requests.get(url2, headers=headers) as resp:
        img = resp.content
    with open(r"D:\bot\data\images\dingzhen.png", mode="wb") as f:
        f.write(img)

def get_wife():
    wives = os.listdir(r"D:\bot\wife")
    wife = random.choice(wives)
    shutil.copy(fr"D:\bot\wife\{wife}", fr"D:\bot\data\images\{wife}")
    return wife

def get_there_wives():
    wives = os.listdir(r"D:\bot\wife")
    wife1 = random.choice(wives)
    wife2 = random.choice(wives)
    wife3 = random.choice(wives)
    shutil.copy(fr"D:\bot\wife\{wife1}", fr"D:\bot\data\images\{wife1}")
    shutil.copy(fr"D:\bot\wife\{wife2}", fr"D:\bot\data\images\{wife2}")
    shutil.copy(fr"D:\bot\wife\{wife3}", fr"D:\bot\data\images\{wife3}")
    return wife1, wife2, wife3

async def get_many_setu(url, num):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56"
    }
    async with aiohttp.ClientSession() as client:
        async with client.get(url, headers=headers) as resp:
            with open(f"D:\\bot\\data\\images\\setu{num}.png", mode="wb") as f:
                f.write(await resp.content.read())

async def get_one_setu(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56"
    }
    async with aiohttp.ClientSession() as client:
        async with client.get(url, headers=headers) as resp:
            with open(f"D:\\bot\\data\\images\\setu1.png", mode="wb") as f:
                f.write(await resp.content.read())

def get_xibao(content):
    font = ImageFont.truetype("C:/Windows/Fonts/simhei.ttf", 48)
    img = Image.open("D:/bot/face/xi.png")
    width, height = img.size
    x = font.getlength(content)
    draw = ImageDraw.Draw(img)
    draw.text(((width - x)/2, height/2), content, (0, 0, 0), font)
    img.save("D:/bot/data/images/xibao.png")

