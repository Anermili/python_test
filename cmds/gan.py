import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
from PIL import Image, ImageDraw, ImageFont
import requests
import os

with open('setting.json', mode='r', encoding='utf8') as setting:
    DataA = json.load(setting)

class gan(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
      if msg.content.endswith('ttsave'):
        #創建目錄
          os.makedirs('./img/',exist_ok=True)
          url = str(msg.content)[:-6]
          r = requests.get(url)
          with open((f'./img/{(msg.author)}test_.png') ,'wb') as f:
        #將圖片下載下來
            f.write(r.content)
            await msg.channel.send('圖片已暫存')
      if msg.content.endswith('tt'):
        content = str(msg.content)[:-2]
      #開啟一張圖片
        image = Image.open(f'./img/{(msg.author)}test_.png')
        draw = ImageDraw.Draw(image)
      #定義文字字型及字號
        imageFont = ImageFont.truetype("./Fonts/MYuppy-dospy.ttf", 55) 
      #獲取圖片大小
        width,height = image.size 
      #下面三行是用來計算文字的位置，用來居中文字內容
        txtSize = draw.textsize(content, imageFont)
        pos_x = (width - txtSize[0]) / 2 if width > txtSize[0] else 0
        pos = (pos_x, 10)
      #文字寫入圖片
        draw.text(pos, content, font=imageFont, fill='#78fffa') 
      #儲存圖片
        image.save('./outputpic/test.png') 

        pic = discord.File(DataA['pic'])
        await msg.channel.send(file= pic)


        

        






def setup(bot):
    bot.add_cog(gan(bot))