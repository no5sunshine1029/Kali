import discord
import random
import os
import keep_alive
# import asyncio
# from dotenv import load_dotenv
# from discord import app_commands
# from discord.ext import commands
# load_dotenv()

TOKEN = os.environ['TOKEN']
L1 = ['謹慎行事', '此時不要提出過多要求', '不要急於決定', '儘早行動',
      '冷靜下來', '轉移你的注意力', '等一等', '你的行為將會改善這件事']
L2 = ['我愛你', '你最棒了']
L3 = ['/Kali_1.jpg', '/Kali_2.jpg', '/Kali_3.jpg', '/Kali_4.jpg',
      '/Kali_5.jpg', '/Kali_6.jpg', '/Kali_7.jpg', '/Kali_8.jpg',
      '/Kali_9.jpg', '/Kali_10.jpg', '/Kali_11.jpg', '/Kali_12.jpg',
      '/Kali_13.jpg', '/Kali_14.jpg']

L4 = ['/Kali_H1.jpg', '/Kali_H2.jpg', '/Kali_H3.jpg', '/Kali_H4.jpg']
L5 = ['我也愛妳', '我也是', '嗯', '我知道呢', '這不是理所當然的嗎']
Keyword_list = ['我該怎麼做', '早安', '我想看你', '我想色色', '我要睡了', '我愛你', '誰是你婆', '誰是妳婆']
id = 929278283604963359
mention_id = '<@929278283604963359>'
Kali_id = '<@1004755297514029133>'
sunshine_id = '<@607403847945682985>'


# client 是我們與 Discord 連結的橋樑
intents = discord.Intents.default()
intents.message_content = True
# discord.Client(intents=intents)
client = discord.Client(intents=intents)

# 調用 event 函式庫

activity_w = discord.Activity(
    type=discord.ActivityType.playing, name='Tom Clancy\'s Rainbow Six Siege')

custom_test = discord.CustomActivity(name='test')
test_act = discord.Activity(type=discord.ActivityType.custom)


@client.event
# 當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', client.user)
    await client.change_presence(activity=activity_w, status=discord.Status.do_not_disturb)


@client.event
# 當有訊息時
async def on_message(message):
    # 排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
    # print(message.author.id)
    # print('----- '+message.channel.name+' -----')
    # print(message.author.name+': '+message.content)
    # print(message.content
    # if message.author.id == 607403847945682985:
    # await message.channel.send('SUCCESS')
    # print('SUCCESS')
    # if message.author.id == 513689561310953472:
    #     await message.channel.send('你閉嘴')

    # 如果包含 ping，機器人回傳 pong
    if message.content == 'ping':
        await message.channel.send('pong')

    if message.content.startswith('@Kali') or message.content.startswith(Kali_id):
        # tmp = message.content.split(' ', 1)
        # if len(tmp) == 1:
        #     await message.channel.send(mention_id + f"{random.choice(L5)}")
        # else:
        #   string = tmp[1]
        #   await message.channel.send(tmp[1])
        if '功能介紹' in message.content:
            await message.channel.send("```Kali 功能一覽\n\
前綴指令: @Kali\n\
後續指令:\n\
\t我該怎麼做: 讓kali透過解搭之書回答你\n\
\t決定: 讓Kali幫你從兩個選項之中做決定\n\
\t抱: Kali抱抱你\n\
\t❤: Kali會跟你說愛你\n\
\t婆: 告訴大家誰是Kali的老婆\n\
\t早午晚安: Kali跟你早午晚安\n\
\t親親: 親一個\n\
\t看你: Kali圖集\n\
\t色色: Kali嘿嘿圖集\n\
\t睡: Kali陪你睡\n\
\t愛你: Kali說愛你```")
        elif '決定' in message.content:
            cut_word = message.content.split(" ", 3)
            select_1 = cut_word[2]
            select_2 = cut_word[3]
            select_list = [select_1, select_2]
            await message.channel.send(f"{random.choice(select_list)}")
        elif '我該怎麼做' in message.content:
            await message.channel.send(f"{random.choice(L1)}")
        elif '抱' in message.content:
            await message.channel.send(f'{message.author.mention}抱抱')
        elif '❤' in message.content:
            tmp = message.content.split(' ', 1)
            if len(tmp[1]) == 1:
                await message.channel.send('愛你❤')
            else:
                await message.channel.send(f'{random.choice(L2)}')
        elif ('婆' in message.content):
            if ('誰是你婆' in message.content) or ('誰是妳婆' in message.content):
                await message.channel.send(mention_id + '是我<:wife:1002781022062120980>')
            else:
                await message.channel.send(mention_id + '你當然是我<:wife:1002781022062120980>')
        elif '早安' in message.content:
            if message.author.id == id:
                await message.channel.send(mention_id+'老婆早安❤')
            else:
                await message.channel.send(f'{message.author.mention}早安')
        elif '午安' in message.content:
            if message.author.id == id:
                await message.channel.send(mention_id+'老婆午安❤')
            else:
                await message.channel.send(f'{message.author.mention}午安')
        elif '晚安' in message.content:
            if message.author.id == id:
                await message.channel.send(mention_id+'老婆晚安❤')
            else:
                await message.channel.send(f'{message.author.mention}晚安')
        elif '親親' in message.content:
            await message.channel.send(f'{message.author.mention}親一個👄')
        elif '看你' in message.content:
            await message.channel.send(file=discord.File(r'image'+f"{random.choice(L3)}"))
        elif '色色' in message.content:
            await message.channel.send(file=discord.File(r'image/special'+f"{random.choice(L4)}"))
        elif '睡' in message.content:
            await message.channel.send('我陪你睡')
            # await client.close()
        elif('愛你' in message.content) or ('愛妳' in message.content):
            await message.channel.send(mention_id+f"{random.choice(L5)}")
        else:
            await message.channel.send(f'{random.choice(L5)}')
            # await message.channel.send('<:Kali:1006045854412591105>')
            # await message.channel.send('再說一次')
    if message.content == '咖哩、想你':
        await message.channel.send('與其花時間想我，不如花時間在妳的事業與未來上…不過，我不討厭就是了')

keep_alive.keep_alive()
client.run(TOKEN)
