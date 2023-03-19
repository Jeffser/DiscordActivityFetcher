import discord, json
from discord.ext import tasks, commands
from os import system
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())
author = False

###################
serverID = 0
userID = 0
botToken = ''
fileDirectory = ''
###################

@tasks.loop(minutes=0.1)
async def record():
    global author
    if author == False: return
    currentActivities = []
    for cA in author.activities: currentActivities.append({'details': cA.details, 'large_image_url': cA.large_image_url, 'name': cA.name, 'state': cA.state})
    currentActivities = json.dumps(currentActivities).replace('"', '\\"')
    system(f'echo "{currentActivities}" > ' + fileDirectory)
    #with open("/srv/http/discord.json", "w") as outfile: outfile.write()

@bot.event
async def on_ready():
    global author
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='you 🐱'))
    author = bot.get_guild(serverID).get_member(userID)
    record.start()

if __name__ == "__main__":
    bot.run(botToken)
