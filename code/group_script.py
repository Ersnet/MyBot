import asyncio
import aiohttp
import httpx
import json
import random
import requests
import get_send_img
import get_send_text
import private_script
import config
import re
from random import choice
from datetime import datetime
from sympy import *
from sympy.abc import x, y
from math import *
from get_send_img import *
from get_send_text import *
import os
import jsonpath

with open("words.json", mode="r", encoding="utf-8") as f:
    json_words = json.load(f)

words_lst = ['mua', '啾咪', '摸', '上你', '傻', '裸', '贴', '老婆', '抱', '亲', '一下', '咬', '操', '123', '进去', '调教', '搓', '让', '捏', '挤', '略', '呐', '原味', '胖次', '内裤', '内衣', '衣服', 'ghs', '批', '憨批', 'kkp', '咕', '骚', '喜欢', 'suki', '好き', '看', '不能', '砸了', '透', '口我', '草我', '自慰', 'onani', 'オナニー', '炸了', '色图', '涩图', '告白', '对不起', '吻', '软', '壁咚', '掰开', '女友', '是', '喵', '嗷呜', '叫', '拜', '佬', 'awsl', '臭', '香', '腿', '张开', '脚', '脸', '头发', '手', 'pr', '舔', '小穴', '腰', '诶嘿嘿', '可爱', '扭蛋', '鼻', '眼', '色气', '推', '床', '举', '手冲', '饿', '变', '敲', '爬', '怕', '冲', '射', '不穿', '迫害', '猫粮', '揪尾巴', '薄荷', '早', '晚安', '揉', '榨', '掐', '胸', '奶子', '欧派', '嫩', '蹭', '牵手', '握手', '拍照', 'w', '睡不着', '欧尼酱', '哥', '爱你', '过来', '自闭', '打不过', '么么哒', '很懂', '膝枕', '累了', '安慰', '洗澡', '一起睡觉', '一起', '多大', '姐姐', '糖', '嗦', '牛子', '🐂子', '🐮子', '嫌弃', '紧', 'baka', '笨蛋', '插', '插进来', '屁股', '翘', '翘起来', '抬', '抬起', '爸', '傲娇', 'rua', '咕噜咕噜', '咕噜', '上床', '做爱', '吃掉', '吃', '揪', '种草莓', '种草', '掀', '妹', '病娇', '嘻', '按摩', '按住', '按在', '按倒', '按', '炼铜', '白丝', '黑丝', '喷', '约会', '出门', '上学', '上班', '下课', '回来', '回家', '放学', '下班']

async def handle_group(gid, message, uid=None):  # 处理群聊信息
    if str(gid) in config.allow_group_id:
        user = f"[CQ:at,qq={uid}]" + "\n"
        temp_word_lst = [i for i in words_lst if i in message.strip()]

        if message.strip() == "":      # 简单的判断，只是判断其是否为空
            await send(gid, f"喵喵喵~ 当前时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        elif message.strip() == "帮助" or message.strip() == "help":
            await send(gid, user + "[CQ:image,file=help.png]")

        elif message.strip()[0:2] == "翻译":
            text = get_translate(message.strip()[3:])
            await send(gid, user + text)

        elif message.strip()[:3] == "二次元":
            n1 = random.uniform(1, 100)
            n2 = random.uniform(1, 100)
            if n1 > n2:
                await send(gid, user + "涩图看多了可不好哦~")
            else:
                if "r18" in message.strip()[4:]:
                    await send(gid, user + "不可以涩涩哦~哒咩~")
                else:
                    get_setu(message.strip()[4:])
                    await send(gid, user + "[CQ:image,file=setu.png]")
                    os.remove("D:\\bot\\data\\images\\setu.png")

        elif message.strip()[0] == "来" and message.strip()[-3:] == "份涩图":
            n1 = random.uniform(1, 100)
            n2 = random.uniform(1, 100)
            if n1 > n2:
                await send(gid, user + "少看点涩图吧！")
            else:
                num = re.finditer("\d.*", message.strip())
                num_true = int(num.__next__().group().strip("份涩图"))

                if num_true == 1:
                    url = "https://moe.jitsu.top/api?num=1"
                    task = [asyncio.create_task(get_send_img.get_one_setu(url))]
                    await asyncio.wait(task)
                    await send(gid, user + "[CQ:image,file=setu1.png]")
                    os.remove("D:\\bot\\data\\images\\setu1.png")

                elif num_true <= 5:
                    task = []
                    urls = "https://moe.jitsu.top/api"
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56"
                    }
                    params = {
                        "num": num_true
                    }
                    async with aiohttp.ClientSession() as client:
                        async with client.get(urls, headers=headers, params=params) as resp:
                            imgs_str = await resp.text()
                            imgs_json = json.loads(imgs_str)
                            imgs = imgs_json["pics"]
                    for url, n in zip(imgs, range(1, num_true + 1)):
                        task.append(asyncio.create_task(get_send_img.get_many_setu(url, n)))
                    await asyncio.wait(task)

                    imgs_cq = ""
                    for i in range(1, num_true+1):
                        imgs_cq += f"[CQ:image,file=setu{i}.png]"

                    await send(gid, user + imgs_cq)
                    for i in range(1, num_true + 1):
                        os.remove(f"D:\\bot\\data\\images\\setu{i}.png")
                else:
                    await send(gid, user + "你要的太多了啦~")

        elif message.strip()[:4] == "答案之书":
            with open('answersbook.json', 'r', encoding='utf-8') as f:
                json_data = json.load(f)

            answer = []
            for key, val in json_data.items():
                for k, v in val.items():
                    answer.append(v)

            await send(gid, user + str(random.choice(answer)))

        elif message.strip()[:2] == "计算":
            tex1 = latex(sympify(message.strip()[3:]))
            tex2 = latex(sympify(message.strip()[3:]).evalf())
            get_latex(tex1)
            get_exact_v_latex(tex2)
            pic1 = "[CQ:image,file=tex.png]"
            pic2 = "[CQ:image,file=exact.png]"
            await send(gid, user + f"计算：{message.strip()[3:]}=?\n结果：{pic1}\n精确值：{pic2}")
            os.remove("D:\\bot\\data\\images\\tex.png")
            os.remove("D:\\bot\\data\\images\\exact.png")

        elif message.strip()[:2] == "求根":
            tex = latex(solve(sympify(message.strip()[3:])))
            get_latex(tex)
            pic = "[CQ:image,file=tex.png]"
            await send(gid, user + f"求根：{message.strip()[3:]}=0\n结果：根为{pic}")
            os.remove("D:\\bot\\data\\images\\tex.png")

        elif message.strip()[:4] == "因式分解":
            tex = latex(factor(sympify(message.strip()[5:])))
            get_latex(tex)
            pic = "[CQ:image,file=tex.png]"
            await send(gid, user + f"因式分解：{message.strip()[5:]}=?\n结果：{pic}")
            os.remove("D:\\bot\\data\\images\\tex.png")

        elif message.strip()[:6] == "/latex":
            tex = message.strip()[7:]
            get_latex(tex)
            await send(gid, user + "[CQ:image,file=tex.png]")
            os.remove("D:\\bot\\data\\images\\tex.png")

        elif message.strip()[:2] == "天气":
            text = get_city_weather(message.strip()[3:])
            await send(gid, user + f"{text}")

        elif message.strip()[:3] == "字符画":
            get_qq_image(message.strip()[4:])
            get_img2t(r"D:\bot\temp_qq\img.jpg")
            await send(gid, user + "[CQ:image,file=img2t.jpg]")
            os.remove("D:\\bot\\data\\images\\img2t.png")

        elif message.strip()[:3] == "梗百科":
            meme = get_meme(message.strip()[4:])
            await send(gid, user + meme)

        elif message.strip() == "kfc":
            kfc_v50 = get_kfc_v50()
            await send(gid, user + kfc_v50)

        elif message.strip()[:8] == "狗屁不通文章生成":
            text = get_shit_text(message.strip()[9:])
            await send(gid, user + text)

        elif message.strip()[-2:] == "撤回":
            id = re.finditer("id=.*?]", message.strip())
            nid = id.__next__().group().replace("id=", "").replace("]", "")
            message_id = int(nid)
            await recall(message_id)

        elif message.strip()[:2] == "保存":
            name_re = re.finditer("保存.*?CQ:", message.strip())
            name = name_re.__next__().group().replace("保存 ", "").replace("[CQ:", "")
            names = [name for name in os.listdir(r"D:\bot\data\images") if name[-4:] == ".gif" or name[-4:] == ".jpg" or name[-4:] == ".png"]
            if name in names:
                await send(gid, user + "图片名称不能重复哦~")
            else:
                save_qq_image(message.strip())
                await send(gid, user + f"已保存{name}")

        elif message.strip()[:2] == "删除":
            name = message.strip()[3:]
            os.remove(f"D:\\bot\\data\\images\\{name}")
            await send(gid, user + f"已删除{name}")

        elif message.strip()[:3] == "已存图":
            path = r"D:\bot\data\images"
            names = names = [name for name in os.listdir(r"D:\bot\data\images") if name[-4:] == ".gif" or name[-4:] == ".jpg" or name[-4:] == ".png"]
            name = "\n".join(names)
            len_names = len(names)
            await send(gid, user + f"现在已保存{len_names}张图：\n" + name)

        elif message.strip()[:3] == "随机图":
            if len(message.strip()) <= 4:
                names = [name for name in os.listdir(r"D:\bot\data\images") if name[-4:] == ".gif" or name[-4:] == ".jpg" or name[-4:] == ".png"]
                name = random.choice(names)
                await send(gid, user + name + f"[CQ:image,file={name}]")
            else:
                key = message.strip()[4:]
                names = [name for name in os.listdir(r"D:\bot\data\images") if name[-4:] == ".gif" or name[-4:] == ".jpg" or name[-4:] == ".png"]
                key_names = []
                for i in names:
                    if key in i:
                        key_names.append(i)
                key_name = random.choice(key_names)
                await send(gid, user + key_name + f"[CQ:image,file={key_name}]")


        elif message.strip()[-4:] == ".jpg":
            await send(gid, user + f"[CQ:image,file={message.strip()}]")

        elif message.strip()[-4:] == ".gif":
            await send(gid, user + f"[CQ:image,file={message.strip()}]")

        elif message.strip()[-4:] == ".png":
            await send(gid, user + f"[CQ:image,file={message.strip()}]")

        elif message.strip()[:2] == "新闻":
            get_world_news()
            await send(gid, user + "[CQ:image,file=news.png]")
            os.remove("D:\\bot\\data\\images\\news.png")

        elif message.strip()[:4] == "摸鱼日历":
            get_moyu_date()
            await send(gid, user + "[CQ:image,file=moyu.png]")
            os.remove("D:\\bot\\data\\images\\moyu.png")

        elif message.strip()[:5] == "emoji":
            emoji = message.strip()[6:]
            url = "https://www.gstatic.com/android/keyboard/emojikitchen/"
            dates = [
                "20201001/",
                "20210218/",
                "20210521/",
                "20210831/",
                "20211115/",
                "20220110/",
                "20220203/",
                "20220406/",
                "20220506/",
            ]

            emoji_str = str(emoji.encode("unicode-escape")).replace("b'", "").replace("'", "").replace("\\", "").replace("U000", "u").replace("+", "_")
            emoji_one_str = emoji_str.split("_")
            new_emoji_str_lst = emoji_str.split("_")
            new_emoji_str_lst[0], new_emoji_str_lst[1] = new_emoji_str_lst[1], new_emoji_str_lst[0]
            new_emoji_str = "_".join(new_emoji_str_lst)

            urls = []
            for emoji_one in emoji_one_str:
                for date in dates:
                    first_url = url + date + emoji_one + "/" + emoji_str + ".png"
                    second_url = url + date + emoji_one + "/" + new_emoji_str + ".png"
                    urls.append(first_url)
                    urls.append(second_url)
            tasks = []
            for u in urls:
                tasks.append(asyncio.create_task(get_emoji_mix(u)))

            await asyncio.wait(tasks)

            path = r"D:\bot\data\images"
            names = [name for name in os.listdir(path) if name != "guild-images"]

            if "emoji.png" in names:
                await send(gid, user + "[CQ:image,file=emoji.png]")
                os.remove("D:\\bot\\data\\images\\emoji.png")
            else:
                await send(gid, user + "暂不支持合成这两个emoji捏~")

        elif message.strip()[:3] == "say":
            word = message.strip()[4:]
            await send(gid, f"[CQ:tts,text={word}]")

        elif message.strip()[:3] == "抽老婆":
            n1 = random.uniform(1, 100)
            n2 = random.uniform(1, 100)
            if n1 > n2:
                await send(gid, user + "想桃子呢，你哪有老婆")
            else:
                if "[CQ:at,qq=" in message.strip()[3:]:
                    wife_img = get_send_img.get_wife()
                    wife_name = wife_img.strip(".png")
                    await send(gid, message.strip()[3:] + "你今天的群老婆是：" + f"[CQ:image,file={wife_img}]" + wife_name)
                    os.remove(f"D:\\bot\\data\\images\\{wife_img}")
                else:
                    wife_img = get_send_img.get_wife()
                    wife_name = wife_img.strip(".png")
                    await send(gid, user + "你今天的群老婆是：" + f"[CQ:image,file={wife_img}]" + wife_name)
                    os.remove(f"D:\\bot\\data\\images\\{wife_img}")

        elif message.strip()[:4] == "老婆三连":
            n1 = random.uniform(1, 100)
            n2 = random.uniform(1, 100)
            if n1 > n2:
                await send(gid, user + "想桃子呢，你哪有老婆")
            else:
                if "[CQ:at,qq=" in message.strip()[4:]:
                    wife_img1, wife_img2, wife_img3 = get_send_img.get_there_wives()
                    wife_name1, wife_name2, wife_name3 = wife_img1.strip(".png"), wife_img2.strip(".png"), wife_img3.strip(".png")
                    await send(gid, message.strip()[4:] + "你今天的群老婆是：" + f"[CQ:image,file={wife_img1}]" + wife_name1 + f"[CQ:image,file={wife_img2}]" + wife_name2 + f"[CQ:image,file={wife_img3}]" + wife_name3)
                    os.remove(f"D:\\bot\\data\\images\\{wife_img1}")
                    os.remove(f"D:\\bot\\data\\images\\{wife_img2}")
                    os.remove(f"D:\\bot\\data\\images\\{wife_img3}")
                else:
                    wife_img1, wife_img2, wife_img3 = get_send_img.get_there_wives()
                    wife_name1, wife_name2, wife_name3 = wife_img1.strip(".png"), wife_img2.strip(".png"), wife_img3.strip(".png")
                    await send(gid, user + "你今天的群老婆是：" + f"[CQ:image,file={wife_img1}]" + wife_name1 + f"[CQ:image,file={wife_img2}]" + wife_name2 + f"[CQ:image,file={wife_img3}]" + wife_name3)
                    os.remove(f"D:\\bot\\data\\images\\{wife_img1}")
                    os.remove(f"D:\\bot\\data\\images\\{wife_img2}")
                    os.remove(f"D:\\bot\\data\\images\\{wife_img3}")

        elif message.strip() == "丁真":
            get_send_img.get_dingzhen_face()
            await send(gid, user + "[CQ:image,file=dingzhen.png]")
            os.remove("D:\\bot\\data\\images\\dingzhen.png")

        elif message.strip()[:2] == "喜报":
            content = message.strip()[3:]
            get_send_img.get_xibao(content)
            await send(gid, user + "[CQ:image,file=xibao.png]")
            os.remove("D:\\bot\\data\\images\\xibao.png")

        elif message.strip()[:2] == "出警":
            if "[CQ:at" in message.strip()[2:]:
                qq = get_send_text.get_qq_number(message.strip()[2:])
                get_send_img.get_qq_avatar(qq)
                get_send_img.get_police()
                await send(gid, user + "[CQ:image,file=police.png]")
                os.remove("D:\\bot\\data\\images\\police.png")
            else:
                qq = message.strip()[3:]
                get_send_img.get_qq_avatar(qq)
                get_send_img.get_police()
                await send(gid, user + "[CQ:image,file=police.png]")
                os.remove("D:\\bot\\data\\images\\police.png")

        elif message.strip()[:3] == "at我":
            if "[CQ:at" in message.strip()[3:]:
                qq = get_send_text.get_qq_number(message.strip()[3:])
                get_send_img.get_qq_avatar(qq)
                get_send_img.get_at_me()
                await send(gid, user + "[CQ:image,file=atme.png]")
                os.remove("D:\\bot\\data\\images\\atme.png")
            else:
                qq = message.strip()[4:]
                get_send_img.get_qq_avatar(qq)
                get_send_img.get_at_me()
                await send(gid, user + "[CQ:image,file=atme.png]")
                os.remove("D:\\bot\\data\\images\\atme.png")

        elif message.strip()[:1] == "扔":
            if "[CQ:at" in message.strip()[1:]:
                qq = get_send_text.get_qq_number(message.strip()[1:])
                get_send_img.get_qq_avatar(qq)
                get_send_img.get_throw()
                await send(gid, user + "[CQ:image,file=throw.png]")
                os.remove("D:\\bot\\data\\images\\throw.png")
            else:
                qq = message.strip()[2:]
                get_send_img.get_qq_avatar(qq)
                get_send_img.get_throw()
                await send(gid, user + "[CQ:image,file=throw.png]")
                os.remove("D:\\bot\\data\\images\\throw.png")

        elif message.strip()[:2] == "结婚":
            if "[CQ:at" in message.strip()[2:]:
                qq = get_send_text.get_qq_number(message.strip()[2:])
                get_send_img.get_qq_avatar(qq)
                get_send_img.get_married()
                await send(gid, user + "[CQ:image,file=married.png]")
                os.remove("D:\\bot\\data\\images\\married.png")
            else:
                qq = message.strip()[3:]
                get_send_img.get_qq_avatar(qq)
                get_send_img.get_married()
                await send(gid, user + "[CQ:image,file=married.png]")
                os.remove("D:\\bot\\data\\images\\married.png")

        elif message.strip()[:3] == "完美的":
            if "[CQ:at" in message.strip()[3:]:
                qq = get_send_text.get_qq_number(message.strip()[3:])
                get_send_img.get_qq_avatar(qq)
                get_send_img.get_perfect()
                await send(gid, user + "[CQ:image,file=perfect.png]")
                os.remove("D:\\bot\\data\\images\\perfect.png")
            else:
                qq = message.strip()[4:]
                get_send_img.get_qq_avatar(qq)
                get_send_img.get_perfect()
                await send(gid, user + "[CQ:image,file=perfect.png]")
                os.remove("D:\\bot\\data\\images\\perfect.png")

        elif message.strip()[:1] == "哭":
            if "[CQ:at" in message.strip()[1:]:
                qq = get_send_text.get_qq_number(message.strip()[1:])
                get_send_img.get_qq_avatar(qq)
                get_send_img.get_cry()
                await send(gid, user + "[CQ:image,file=cry.png]")
                os.remove("D:\\bot\\data\\images\\cry.png")
            else:
                qq = message.strip()[2:]
                get_send_img.get_qq_avatar(qq)
                get_send_img.get_cry()
                await send(gid, user + "[CQ:image,file=cry.png]")
                os.remove("D:\\bot\\data\\images\\cry.png")

        elif message.strip()[:3] == "安全感":
            if "[CQ:at" in message.strip()[3:]:
                qq = get_send_text.get_qq_number(message.strip()[3:])
                get_send_img.get_qq_avatar(qq)
                get_send_img.get_safe()
                await send(gid, user + "[CQ:image,file=safe.png]")
                os.remove("D:\\bot\\data\\images\\safe.png")
            else:
                qq = message.strip()[4:]
                get_send_img.get_qq_avatar(qq)
                get_send_img.get_safe()
                await send(gid, user + "[CQ:image,file=safe.png]")
                os.remove("D:\\bot\\data\\images\\safe.png")

        elif message.strip()[:2] == "拉黑":
            if str(uid) == "3327569276":
                u = message.strip()[3:]
                with open(r"D:\bot\blacklist.txt", mode="a", encoding="utf-8") as f:
                    f.write(u)
                await send(gid, user + f"已将{u}拉入黑名单")
            else:
                await send(gid, user + "你没有权限哦~")

        elif len(temp_word_lst) >= 1:
            word_content = random.choice(json_words[temp_word_lst[0]])
            await send(gid, user + word_content)

        else:
            _ = await private_script.get_resp(message)
            ret = _.get("content", "获取回复失败")
            await send(gid, user + ret)

async def group_increase(uid, gid):  # 处理有新成员加入的情况
    if str(gid) in config.allow_group_id:
        msg = config.welcome_group.get(str(gid), config.welcome_group["default"]) % uid  # welcome_group的键是qq群号，值是欢迎语
        await send(gid, msg)  # 发送信息

async def quit(gid, uid=None):
    user = f"[CQ:at,qq={uid}]" + "\n"
    await send(gid, user + "抱歉，您无权使用该bot")

async def fuck(gid, uid=None):
    user = f"[CQ:at,qq={uid}]" + "\n"
    text = get_fuck_text()
    await send(gid, user + f"{text}")

async def click_event(uid, gid):
    info = choice(config.click_info)  # 获取戳一戳的信息
    try:
        info = info % uid
    except TypeError:
        if gid:  # 说明其为群戳戳
            info = f"[CQ:at,qq={uid}]" + info
    if gid:
        await send(gid, info)
    else:
        await private_script.send(uid, info)

async def send(gid, message):
    """
    用于发送消息的函数
    :param gid: 群号
    :param message: 发送的消息
    :return: None
    """
    async with httpx.AsyncClient(base_url="http://127.0.0.1:5700") as client:
        # 如果发送的为私聊消息
        params = {
            "group_id": gid,
            "message": message.replace("{br}", "\n").replace("菲菲", "小小刚").replace("<br/>", ""),
        }
        await client.get("/send_group_msg", params=params)

async def recall(message_id):
    """
    用于撤回消息的函数
    :param message_id: 发送的消息的id
    :return: None
    """
    async with httpx.AsyncClient(base_url="http://127.0.0.1:5700") as client:
        params = {
            "message_id": message_id,
        }
        await client.get("/delete_msg", params=params)

async def get_recall_message(message_id):
    """
    用于得到撤回消息的函数
    :param message_id: 发送的消息的id
    :return: None
    """
    async with aiohttp.ClientSession() as client:
        params = {
            "message_id": message_id,
        }
        async with client.get("http://127.0.0.1:5700/get_msg", params=params) as resp:
            data = await resp.json()
            message = data["data"]["message"]
    return message

async def get_message(message_id):
    """
    用于得到消息的函数
    :param message_id: 发送的消息的id
    :return: None
    """
    async with aiohttp.ClientSession() as client:
        params = {
            "message_id": message_id,
        }
        async with client.get("http://127.0.0.1:5700/get_msg", params=params) as resp:
            data = await resp.json()
            group_id = data["data"]["group_id"]
            message = data["data"]["message"]
            msg_id = data["data"]["message_id"]
            time = data["data"]["time"]
            nickname = data["data"]["sender"]["nickname"]
            user_id = data["data"]["sender"]["user_id"]
    return group_id, message, msg_id, user_id, nickname, time


# async def send_group_forward_msg(group_id, messages):
#     """
#         用于发送合并转发的函数
#         :param group_id: 群号
#         :param message: 消息
#         :return: None
#         """
#     async with httpx.AsyncClient(base_url="http://127.0.0.1:5700") as client:
#         params = {
#             "group_id": group_id,
#             "messages": messages
#         }
#         await client.get("/send_group_forward_msg", params=params)
#
#

def Send(gid, message):
    url = "http://127.0.0.1:5700/send_msg"
    params = {
        "group_id": gid,
        "message": message
    }
    with requests.get(url, params=params) as resp:
        resp.close()

async def get_group_member_list(group_id):
    async with aiohttp.ClientSession() as client:
        params = {
            "group_id": group_id,
        }
        async with client.get("http://127.0.0.1:5700/get_group_member_list", params=params) as resp:
            json_text = await resp.json()
            nikcname = jsonpath.jsonpath(json_text, '$..nickname')
            user_id = jsonpath.jsonpath(json_text, '$..user_id')
            group_member_list = list(zip(nikcname, user_id))

    return group_member_list


# def send_group_forward_msg(group_id, messages):
#     url = "http://127.0.0.1:5700/send_group_forward_msg"
#     params = {
#         "group_id": group_id,
#         "messages": messages
#     }
#     with requests.get(url, params=params) as resp:
#         print(resp)
#
# a = [
#   {
#     "type": "node",
#     "data": {
#       "id": "372191328"
#     }
#   },
#   {
#     "type": "node",
#     "data": {
#       "id": "1630011638"
#     }
#   }
# ]
# send_group_forward_msg(720299678, f"[{a}]")
