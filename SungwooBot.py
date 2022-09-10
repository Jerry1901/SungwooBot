import discord
from discord.ext.commands import Bot

TOKEN = 'MTAxODE4ODYxODA2MzQyNTU4Nw.Giv0Ui.PHqXm4QWWeMaIzEniqgiQIy-AyfmfBoH_UYiOs'

intents = discord.Intents.all()

bot = Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
  print(f'logged in as {bot.user}')
  
@bot.event
async def on_message(message):
    if message.content == "준서": #입력할 메시지
        await message.delete()
        embed = discord.Embed(title="준서", description="준서가 감지되었어요!", color=0xff2707)
        embed.add_field(name="어허!! ||준서||라뇨!!", value="준서는 나빠요..", inline=False)
        await message.channel.send(embed=embed)
    if message.content == "🖕": #입력할 메시지
        await message.delete()
        embed = discord.Embed(title="(이모지)욕설 감지!", description="이모지로 욕하면 안걸릴줄 알았죠?", color=0xff2707)
        embed.add_field(name="어허!! ||🖕||이라뇨!!", value="이모지로 욕한것도 욕", inline=False)
        await message.channel.send(embed=embed)

bot.run(TOKEN)
