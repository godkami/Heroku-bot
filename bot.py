import discord
from discord.ext.commands import Bot
from discord import Game
import discord.ext.commands
import requests
from bs4 import BeautifulSoup

client=Bot(command_prefix='-')

u="https://myanimelist.cdn-dena.com/images/anime/3/24641.jpg"
p="https://myanimelist.net/anime.php?q="

@client.command()
async def emb():
	embed=discord.Embed(title="hh",description="hhh")
	embed.colour = 0xFFFFFF
	embed.set_image(url=u)
	await client.say(embed=embed)
	
	
@client.command()
async def anime(title:str):
	
	
	s=p+title
	page=requests.get(s)
	soup=BeautifulSoup(page.text,'html.parser')
	res=soup.find('td',attrs={'class':'borderClass bgColor0'})
	var_link=res.find('a')['href']
	
	page=requests.get(var_link)
	soup=BeautifulSoup(page.text,'html.parser')
	result=soup.find('span',attrs={'itemprop':'description'}).text
	res_2=soup.find('div',attrs={'style':'text-align: center;'})
	res_3=soup.find('span',attrs={'itemprop':'name'}).text
	imag=res_2.find('img')['src']
	embed=discord.Embed(title=res_3,description=result,colour=0xFFFFFF)
	embed.set_image(url=imag)
	
	await client.say(embed=embed)

	
@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Anime Party"))
    print("Logged in as " + client.user.name)
	
	
client.run('NDY4NDczNzQ0MTcyNjQ2NDIw.DjMTAA.dOcTSBhooqxxkiC2lwBbgMWGhE4')
