import requests
import jsonpath
import docx
import random
import asyncio
import aiohttp

def get_kfc_v50():
    url = "http://thursday.gouyin.net/api/kfc.php"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"
    }
    with requests.get(url, headers=headers) as resp:
        kfc = resp.json()
    v50 = jsonpath.jsonpath(kfc, "$..content")
    kfc_v50 = ""
    for i in v50:
        kfc_v50 += i
    if "STARS-607" in kfc_v50:
        new = kfc_v50.replace("STARS-607", "APTX4869")
        return new
    else:
        return kfc_v50

def get_meme(meme):
    url = "https://uapi.woobx.cn/app/jiki-pedia"
    data = {
        "page": 1,
        "phrase": meme
    }
    with requests.post(url, data=data) as text:
        json_t = text.json()
    lst = jsonpath.jsonpath(json_t, "$...texts")
    meme_text = lst[0][1]["content"].replace("\n", "")
    return meme_text

def get_city_weather(c):
    url = "https://tenapi.cn/wether/"
    params = {
        "city": c
    }
    with requests.get(url, params=params) as resp:
        json = resp.json()
    city = jsonpath.jsonpath(json, "$..city")
    date = jsonpath.jsonpath(json, "$..date")
    weather = jsonpath.jsonpath(json, "$..weather")
    wind = jsonpath.jsonpath(json, "$..wind")
    airQuality = jsonpath.jsonpath(json, "$..airQuality")
    temperature = jsonpath.jsonpath(json, "$..temp")
    airData = jsonpath.jsonpath(json, "$..airData")
    humidity = jsonpath.jsonpath(json, "$..humidity")
    pm10 = jsonpath.jsonpath(json, "$..pm10")
    pm25 = jsonpath.jsonpath(json, "$..pm25")
    data = list(zip(date, city, weather, temperature, wind, airData, airQuality, pm25, pm10, humidity))
    name = ["日期：", "城市：", "天气：", "温度：", "风向：", "污染指数：", "空气质量：", "pm2.5：", "pm10：", "湿度："]
    w = ""
    for n, d in zip(name, data[0]):
        w += n + str(d) + "\n"
    return w.strip()

def get_shit_text(title):
    url = "https://api.edwiv.com/bzsy/gen.php"
    params = {
        "event": title,
        "length": 800,
        "counterType": 0,
        "isWritten": 0
    }
    with requests.get(url, params=params) as resp:
        t = resp.text
    return t

def get_fuck_text():
    path = "fuck_text.docx"
    file = docx.Document(path)
    t_lst = [i for i in file.paragraphs]
    return random.choice(t_lst).text

def get_translate(text):
    url = "https://api.gmit.vip/Api/Translate"
    params = {
        "format": "json",
        "text": text,
        "from": "auto",
        "to": "auto"
    }
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46"
    }
    with requests.get(url, params=params, headers=headers) as translate:
        translate_text = translate.json()
    return translate_text["data"]["result"]

def get_music_lyrics_about_netease(name):
    url = "https://music.liuzhijin.cn/"
    data = {
        "input": name,
        "filter": "name",
        "type": "netease",
        "page": 1,
    }
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54",
        "x-requested-with": "XMLHttpRequest"
    }
    with requests.post(url, data=data, headers=headers) as resp:
        json_text = resp.json()

    title = jsonpath.jsonpath(json_text, '$..title')
    author = jsonpath.jsonpath(json_text, '$..author')
    url = jsonpath.jsonpath(json_text, '$..url')
    lrc = jsonpath.jsonpath(json_text, '$..lrc')
    song_id = jsonpath.jsonpath(json_text, '$..songid')

    music_t = list(zip(title, author))
    music_main = list(zip(lrc, url, song_id))

    music_content = ""
    for i, n in zip(music_t, range(len(music_t))):
        music_content += f"{n}." + "歌曲名称：" + i[0] + "  " + "创作者：" + i[1] + "\n"

    return music_content.strip(), music_main

def get_music_lyrics_about_qq(name):
    url = "https://music.liuzhijin.cn/"
    data = {
        "input": name,
        "filter": "name",
        "type": "qq",
        "page": 1,
    }
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54",
        "x-requested-with": "XMLHttpRequest"
    }
    with requests.post(url, data=data, headers=headers) as resp:
        json_text = resp.json()

    title = jsonpath.jsonpath(json_text, '$..title')
    author = jsonpath.jsonpath(json_text, '$..author')
    url = jsonpath.jsonpath(json_text, '$..url')
    lrc = jsonpath.jsonpath(json_text, '$..lrc')
    song_id = jsonpath.jsonpath(json_text, '$..songid')
    link = jsonpath.jsonpath(json_text, '$..link')

    music_t = list(zip(title, author))
    music_main = list(zip(lrc, url, song_id, link))

    music_content = ""
    for i, n in zip(music_t, range(len(music_t))):
        music_content += f"{n}." + "歌曲名称：" + i[0] + "  " + "创作者：" + i[1] + "\n"

    return music_content.strip(), music_main

