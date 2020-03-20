import discord
import requests
import json
#import datetime

with open('config.json') as f:
  data = json.load(f)

TOKEN = str(data['token'])

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$cupdate'):
        usData = get_data("USA")
        allData = get_data("ALL")
        #lastUpdate = datetime.datetime.fromtimestamp(fromtimestamp(long(allData['updated'])))

        embed = discord.Embed(title="COVID-19 Stats", colour=discord.Colour(0xd0021b), url="https://www.worldometers.info/coronavirus/", description="this is the most up to date data relating to COVID-19\n\n")

        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/8/82/SARS-CoV-2_without_background.png")
        embed.set_footer(text="we're fucked lol (not really but that's what the media says)")

        embed.add_field(name="**__Worldwide__**", value="Cases: " + str(allData['cases']) + "\n\nDeaths: " + str(allData['deaths']) + "\n\nRecovered: "  + str(allData['recovered']), inline=True)
        embed.add_field(name="**__USA__**", value="Cases: " + str(usData['cases']) + " (**Today: " + str(usData['todayCases']) + "**)\n\nDeaths: " + str(usData['deaths']) + " (**Today: " + str(usData['todayDeaths']) + "**)\n\nRecovered: " + str(usData['recovered']), inline=True)

        await message.channel.send(embed=embed)

def get_data(type):
    covidApi = ""
    if type == "USA":
        covidApi = "https://corona.lmao.ninja/countries/usa" 
    if type == "ALL":
        covidApi = "https://corona.lmao.ninja/all" 

    
    data = requests.get(covidApi)

    return data.json()

client.run(TOKEN)

#Free apis?? idk and idc it better be or else wtf
#https://corona.lmao.ninja/countries/usa <-- Give usa data
#https://corona.lmao.ninja/all <--Gives all data

#{"cases":219265,"deaths":8968,"recovered":85745,"updated":1584592035456}
#{"country":"USA","cases":9458,"todayCases":199,"deaths":155,"todayDeaths":5,"recovered":108,"active":9195,"critical":64,"casesPerOneMillion":29}

