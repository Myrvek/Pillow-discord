import discord
from discord.ext.commands import Bot
from discord.ext import commands
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


Bot = commands.Bot(command_prefix='.')



@Bot.command() #декортаор
async def info(ctx, user: discord.Member): #Функция
    img = Image.open("infoimgimg.png") #Это пикча которую открываем
    draw = ImageDraw.Draw(img) #Рисуем пикчу штоле
    font = ImageFont.truetype("Modern_Sans_Light.otf", 100) #Это шрифт
    fontbig = ImageFont.truetype("Fitamint Script.ttf", 400) #Это большой шрифт
    draw.text((200, 0), "Инфо о вас", (255, 255, 255), font=fontbig) #Делает инфо
    draw.text((50, 500), "Его имя в дискорде {}".format(user.name), (255, 255, 255), font=font) #Делает ник
    draw.text((50, 700), "Его айди  {}".format(user.id), (255, 255, 255), font=font) #Делает id
    draw.text((50, 900), "Его статус{}".format(user.status), (255, 255, 255), font=font) #Делает статус
    draw.text((50, 1100), "Он создал аккаунт {}".format(user.created_at), (255, 255, 255), font=font) #Когда создал акк
    draw.text((50, 1300), "Имя на сервере {}".format(user.display_name), (255, 255, 255), font=font) # Ник юзера
    draw.text((50, 1700), "Он зашел{}".format(user.joined_at), (255, 255, 255), font=font) #Делаем когда зашел
    img.save('infoimg2.png') #Сохроняем
    await ctx.send("Вот твоя инфа в пикчи" , file  = discord.File("infoimg2.png"))
    
    
Bot.run('TOKEN HERE')
    
 
