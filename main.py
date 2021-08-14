import discord
from discord.errors import Forbidden
from discord.ext import commands
import json
import os
import keep_alive


with open('setting.json', mode='r', encoding='utf8') as setting:
    DataA = json.load(setting)

with open('TOKEN.json', mode='r', encoding='utf8') as token:
    TOKEN = json.load(token)


#命令前綴，如不填寫則認為所有命令是前綴。
bot = commands.Bot(command_prefix='>')

#啟動訊息
@bot.event
async def on_ready():
    print("伺服器小助理已啟動\n靈異現象都會顯示在下方")
    #channel = bot.get_channel(int(DataA['channelA']))
    #await channel.send(f'')

#載入指令檔
@bot.command()
async def load(ctx, extension):
    if str(ctx.author.id) == ('340763969801289729'):
        bot.load_extension(f'cmds.{extension}')
        await ctx.send(f"載入 {extension} 完成")

#移除指令檔
@bot.command()
async def unload(ctx, extension):
    if str(ctx.author.id) == ('340763969801289729'):
        bot.unload_extension(f'cmds.{extension}')
        await ctx.send(f"暫時移除 {extension} 完成")

#重新載入指令檔
@bot.command()
async def reload(ctx, extension):
    if str(ctx.author.id) == ('340763969801289729'):
        bot.reload_extension(f'cmds.{extension}')
        await ctx.send(f"重新載入 {extension} 完成")

#識別只要是.py檔案才載入
for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        #檔案名稱最尾端刪除3個字元
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    keep_alive.keep_alive()
    #TOKEN
    bot.run(TOKEN['TOKEN'])