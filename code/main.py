from flask import Flask, request
from flask_restful import Resource, Api
import re
import get_send_text
import private_script, group_script
import asyncio
import qqbotdata
from time import *
import os

app = Flask(__name__)

api = Api(app)


class AcceptMes(Resource):

    def post(self):
        # 这里对消息进行分发，暂时先设置一个简单的分发
        _ = request.json
        if _.get("message_type") == "private":  # 说明有好友发送信息过来
            uid = _["sender"]["user_id"]  # 获取发信息的好友qq号
            message = _["raw_message"]  # 获取发送过来的消息
            asyncio.run(private_script.handle_private(uid, message))

        elif _.get("message_type") == "group" and "@bot名称" in _["raw_message"]:
            gid = _["group_id"]  # 获取发送消息的群号
            uid = _["sender"]["user_id"]
            asyncio.run(group_script.send(gid, f"[CQ:at,qq={uid}]" + "你没@上哦~"))

        elif _.get("message_type") == "group" and "[CQ:at,qq=bot的qq号]" in _["raw_message"]:  # 制作群聊消息
            message = _["raw_message"].replace("[CQ:at,qq=bot的qq号]", "")  # 获取发送过来的消息
            gid = _["group_id"]  # 获取发送消息的群号
            uid = _["sender"]["user_id"]
            with open(r"D:\bot\blacklist.txt", mode="r", encoding="utf-8") as f:
                uids = f.read()
            if str(uid) in uids:
                asyncio.run(group_script.quit(gid, uid))
            else:
                asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
                asyncio.run(group_script.handle_group(gid, message, uid=uid))

        elif _.get("message_type") == "group":
            message_id = _["message_id"]
            gid = _["group_id"]
            group_id, message, msg_id, user_id, nickname, time = asyncio.run(group_script.get_message(message_id))
            qqbotdata.save_data(group_id, message, msg_id, user_id, nickname, time)
            if message.strip()[:5] == "网易云歌词":
                name = message[6:]
                music_content, music_main = get_send_text.get_music_lyrics_about_netease(name)
                try:
                    num = qqbotdata.get_data(time, user_id)
                    # group_script.Send(gid, music_main[int(num)][0])
                except IndexError as e:
                    asyncio.run(group_script.send(gid, music_content))
                    asyncio.run(group_script.send(gid, "请在15秒内选择喔~选完请耐心等待哈！，大概15秒"))
                    sleep(15)
                    num = qqbotdata.get_data(time, user_id)
                    # group_script.Send(gid, music_main[int(num)][0])
                    asyncio.run(group_script.send(gid, music_main[int(num)][0]))

        # 下面这部分有消息重复发的bug暂时还无法修复
        # elif _.get("message_type") == "group":
        #     message_id = _["message_id"]
        #     gid = _["group_id"]
        #     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        #     group_id, message, msg_id, user_id, nickname, time = asyncio.run(group_script.get_message(message_id))
        #     qqbotdata.save_data(group_id, message, msg_id, user_id, nickname, time)
        #     if message.strip()[:5] == "网易云歌词":
        #         name = message[6:]
        #         music_content, music_main = get_send_text.get_music_lyrics_about_netease(name)
        #         asyncio.run(group_script.send(gid, music_content))
        #         data = qqbotdata.get_data_test(time, user_id)
        #
        #         while str(data) == "()":
        #             # sleep(1)
        #             data = qqbotdata.get_data_test(time, user_id)
        #         asyncio.run(group_script.send(gid, music_main[int(data[0][1])][0]))
        #     else:
        #         pass

            elif message.strip()[:4] == "qq歌词":
                name = message[5:]
                music_content, music_main = get_send_text.get_music_lyrics_about_qq(name)
                try:
                    num = qqbotdata.get_data(time, user_id)
                    # group_script.Send(gid, music_main[int(num)][0])
                except IndexError as e:
                    asyncio.run(group_script.send(gid, music_content))
                    asyncio.run(group_script.send(gid, "请在15秒内选择喔~选完请耐心等待哈！，大概15秒"))
                    sleep(15)
                    num = qqbotdata.get_data(time, user_id)
                    # group_script.Send(gid, music_main[int(num)][0])
                    asyncio.run(group_script.send(gid, music_main[int(num)][0]))

            elif message.strip()[:5] == "网易云点歌":
                name = message[6:]
                music_content, music_main = get_send_text.get_music_lyrics_about_netease(name)
                try:
                    num = qqbotdata.get_data(time, user_id)
                    # group_script.Send(gid, music_main[int(num)][0])
                except IndexError as e:
                    asyncio.run(group_script.send(gid, music_content))
                    asyncio.run(group_script.send(gid, "请在15秒内选择喔~选完请耐心等待哈！，大概15秒"))
                    sleep(15)
                    num = qqbotdata.get_data(time, user_id)
                    # group_script.Send(gid, music_main[int(num)][0])
                    asyncio.run(group_script.send(gid, f"[CQ:music,type=163,id={music_main[int(num)][2]}]"))

            elif message.strip()[:4] == "qq点歌":
                name = message[5:]
                music_content, music_main = get_send_text.get_music_lyrics_about_qq(name)
                try:
                    num = qqbotdata.get_data(time, user_id)
                    # group_script.Send(gid, music_main[int(num)][0])
                except IndexError as e:
                    asyncio.run(group_script.send(gid, music_content))
                    asyncio.run(group_script.send(gid, "请在15秒内选择喔~选完请耐心等待哈！，大概15秒"))
                    sleep(15)
                    num = qqbotdata.get_data(time, user_id)
                    # group_script.Send(gid, music_main[int(num)][0])
                    asyncio.run(group_script.send(gid, f"{music_main[int(num)][3]}"))

        elif _.get("notice_type") == "group_increase":  # 有新成员加入
            uid = _["user_id"]  # 获取加入者的qq
            gid = _["group_id"]  # 获取群号
            asyncio.run(group_script.group_increase(uid, gid))  # 发送欢迎语

        elif _.get("sub_type") == "poke":  # 如果事件类型为戳一戳
            uid = _["user_id"]
            tid = _["target_id"]
            if str(tid) != "bot的qq号":
                return
            try:
                gid = _["group_id"]
            except KeyError as e:
                gid = None
            asyncio.run(group_script.click_event(uid, gid))  # 传入群号和qq号

        elif _.get("notice_type") == "group_recall":
            gid = _["group_id"]
            uid = _["user_id"]
            message_id = _["message_id"]
            if str(uid) != "bot的qq号":
                asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
                messge = f"[CQ:at,qq={uid}]" + "我看见辣！" + "你撤回的消息是：\n" + asyncio.run(group_script.get_recall_message(message_id))
                asyncio.run(group_script.send(gid, messge))
            else:
                pass

api.add_resource(AcceptMes, "/", endpoint="index")
if __name__ == '__main__':
    app.run("0.0.0.0", 5701, debug=True)  # 注意，这里的端口要和配置文件中的保持一致配置文件中的保持一致
