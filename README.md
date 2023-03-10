# BotHelp

**介绍**

---

小小刚 bot 是基于 flask 模块与 go-cqhttp 框架用 python 编写的一个~~人工智障~~bot

源代码已在GitHub开源

**创作者**

---

Ersnet

QQ：3327569276

哔哩哔哩：439114514 [space.bilibili.com/43911...](https://space.bilibili.com/439114514)

GitHub：[github.com/Ersnet](https://github.com/Ersnet)

**环境配置**

---

需要搭建好go-cqhttp框架[github.com/Mrs4s/go-cqhttp](https://github.com/Mrs4s/go-cqhttp)

以及MySQL环境[download.mysql.com/archives/community/](https://download.mysql.com/archives/community/)

go-cqhttp的配置文件可以直接参考我的[github.com/Ersnet/MyBot/blob/main/config.yml](https://github.com/Ersnet/MyBot/blob/main/config.yml)

我使用的python版本为3.10.0

需要安装好python的第三方库[github.com/Ersnet/MyBot/edit/main/requirements.txt](https://github.com/Ersnet/MyBot/edit/main/requirements.txt)

直接在终端输入pip install -r requirements.txt

如果安装速度较慢，可以考虑换源，这里使用清华源

终端输入pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

**bot搭建**

---

这里我默认将go-cqhttp框架安装在了D盘，运行时请注意源码中的路径问题

bot启动时，请一直保持[github.com/Ersnet/MyBot/edit/main/code/main.py](https://github.com/Ersnet/MyBot/edit/main/code/main.py)的正常运行，切勿关闭窗口

由于篇幅原因[github.com/Ersnet/MyBot/edit/main/wife](https://github.com/Ersnet/MyBot/edit/main/wife)中的图片并没有上传完全

全部图片请见[www.aliyundrive.com/s/WnwutuV3j4J](https://www.aliyundrive.com/s/WnwutuV3j4J)

提取码：23ln

**功能**

---
|功能|调用|关键词参数|
| --------------------------------------------------------------------------------------| ----------------------------------------------------------------------------------------| ------------------------------------------------------------|
|获取帮助文档|@+bot 名称 + 帮助 + 关键词参数|无|
|发送二次元~~涩图~~|@+bot 名称 + 二次元 + 空格 + 关键词参数（可选择不填）|pc：横屏壁纸 mp：竖屏壁纸 silver：银发 furry：兽耳 starry：星空1080p：分辨率setu：涩图但不漏 r18：🚫|
|发送多份~~涩图~~|@+bot 名称 + 来{关键词参数}份~~涩图~~|~~涩图~~数量|
|答案之书|@+bot 名称 + 答案之书 + 空格 + 关键词参数|问题|
|英译中，中译英|@+bot 名称 + 翻译 + 空格 + 关键词参数|需要翻译的语句|
|数学计算|@+bot 名称 + 计算 + 空格 + 关键词参数|需要计算的表达式（包括基本运算，三角函数，对数指数运算等等）|
|求根计算|@+bot 名称 + 求根 + 空格 + 关键词参数|方程表达式（需将化为等号右边等于 0 的方程式，调用时无需输入等于 0）|
|因式分解|@+bot 名称 + 因式分解 + 空格 + 关键词参数|数学表达式|
|LaTeX 公式书写|@+bot 名称 +/latex+ 空格 + 关键词参数|LaTeX 表达式|
|天气查询|@+bot 名称 + 天气 + 空格 + 关键词参数|所需查找天气的中国城市|
|字符画生成|@+bot 名称 + 字符画 + 空格 + 关键词参数|所需生成字符画的图片|
|梗百科|@+bot 名称 + 梗百科 + 空格 + 关键词参数|所需查询的梗|
|KFC 文案生成|@+bot 名称 +kfc+ 空格 + 关键词参数|无|
|狗屁不通文章生成器|@+bot 名称 + 狗屁不通文章生成 + 空格 + 关键词参数|文章题目|
|撤回 bot 消息|在 bot 消息回复下发送撤回即可|无|
|保存图片|@+bot 名称 + 保存 + 空格 + 关键词参数|图片名称（需要带上文件后缀）和图片|
|删除图片|@+bot 名称 + 删除 + 空格 + 关键词参数|图片名称（需要带上后缀）|
|发送已保存图片|@+bot 名称 + 关键词参数|图片名称（需要带上后缀）|
|随机发送已保存图片|@+bot 名称 +随机图 + 空格 + 关键词参数（可选择不填）|图片名称中所含有的关键字|
|查看已保存图片|@+bot 名称 + 已存图 + 关键词参数|无|
|每日新闻|@+bot 名称 + 新闻 + 空格 + 关键词参数|无|
|摸鱼日历|@+bot 名称 + 摸鱼日历 + 空格 + 关键词参数|无|
|emoji 表情合成|@+bot 名称 + emoji + 空格 + 关键词参数|emoji1+emoji2|
|抽取二次元老婆|@+bot 名称 + 抽老婆 + 空格 + 关键词参数|可无也可是@别人|
|二次元老婆三连|@+bot 名称 + 老婆三连 + 空格 + 关键词参数|可无也可是@别人|
|文字转语音|@+bot 名称 + say + 空格 + 关键词参数|文本内容|
|获取丁真表情包|@+bot 名称 + 丁真 + 空格 + 关键词参数|无|
|喜报表情包制作|@+bot 名称 + 喜报 + 空格 + 关键词参数|文本内容|
|出警表情包制作|@+bot 名称 + 出警 + 空格 + 关键词参数|QQ号或是@别人|
|为什么@我表情包制作|@+bot 名称 + at我 + 空格 + 关键词参数|QQ号或是@别人|
|扔表情包制作|@+bot 名称 + 扔 + 空格 + 关键词参数|QQ号或是@别人|
|结婚表情包制作|@+bot 名称 + 结婚 + 空格 + 关键词参数|QQ号或是@别人|
|完美的表情包制作|@+bot 名称 + 完美的 + 空格 + 关键词参数|QQ号或是@别人|
|哭哭表情包制作|@+bot 名称 + 苦 + 空格 + 关键词参数|QQ号或是@别人|
|安全感表情包制作|@+bot 名称 + 安全感 + 空格 + 关键词参数|QQ号或是@别人|
|获取网易云音乐歌词|网易云歌词 + 关键词参数|歌名|
|网易云点歌|网易云点歌 + 关键词参数|歌名|
|获取QQ音乐歌词|qq歌词 + 关键词参数|歌名|
|QQ点歌|qq点歌 + 关键词参数|歌名|
|**将群友拉入bot黑名单**|**@+bot 名称 + 拉黑 + 关键词参数**|**群友QQ号**|
|AI~~智障~~聊天|@+bot 名称 + 关键词参数|聊天内容|

到目前，小小刚 bot 仅具有这些功能，后续功能等待 Ersnet 缓慢开发中~

黑色加粗字体表示只有bot管理员可用

**声明**

---

创作者（Ersnet）开发 bot 的目的是增加功能指令让群聊聊天更加有趣

因此，禁止有辱骂过度调戏 bot 的行为，一律发现，将拉入 bot 黑名单!

**最后的最后**

---

如有发现 bot 存在 bug 等问题，请及时联系创作者（Ersnet）进行修理，也十分欢迎前来debug ∠( ᐛ 」∠)_

最后，祝 bot 使用者们好运！（* ＾-＾ *）

‍

