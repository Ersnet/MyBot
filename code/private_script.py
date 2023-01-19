import httpx
from datetime import datetime

async def handle_private(uid, message):  # 处理私聊信息
    if message:  # 简单的判断，只是判断其是否为空
        _ = await get_resp(message)
        ret = _.get("content", "获取回复失败")
        await send(uid, f"{ret}\n当前时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

async def get_resp(message):  # 对接口发送请求，获取响应数据
    async with httpx.AsyncClient() as client:
        params = {
            "key": "free",
            "appid": 0,
            "msg": message,
        }
        resp = await client.get("http://api.qingyunke.com/api.php", params=params)
        return resp.json()

async def send(uid, message):
    """
    用于发送消息的函数
    :param uid: 用户id
    :param message: 发送的消息
    :return: None
    """
    async with httpx.AsyncClient(base_url="http://127.0.0.1:5700") as client:
        # 如果发送的为私聊消息
        params = {
            "user_id": uid,
            "message": message.replace("{br}", "\n").replace("菲菲", "小小刚")
        }
        await client.get("/send_private_msg", params=params)

