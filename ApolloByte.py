import discord, json, os, datetime
from colorama import Fore, init
from discord.ext import commands, tasks

with open('./config.json') as f:
    config = json.load(f)

os.system("title ApolloByte SelfBot")
os.system("color 3")

prefix = config.get('prefix')

bot = commands.Bot(description="ApolloByte Bot", command_prefix=f"{prefix}", self_bot=True)
bot.remove_command("help")

print('''                      ______                       __  __           
                     /      \                     /  |/  |          
                    /$$$$$$  |  ______    ______  $$ |$$ |  ______  
                    $$ |__$$ | /      \  /      \ $$ |$$ | /      \ 
                    $$    $$ |/$$$$$$  |/$$$$$$  |$$ |$$ |/$$$$$$  | Buy Apollo SelfBot today!
                    $$$$$$$$ |$$ |  $$ |$$ |  $$ |$$ |$$ |$$ |  $$ |
                    $$ |  $$ |$$ |__$$ |$$ \__$$ |$$ |$$ |$$ \__$$ | Join our discord!
                    $$ |  $$ |$$    $$/ $$    $$/ $$ |$$ |$$    $$/ 
                    $$/   $$/ $$$$$$$/   $$$$$$/  $$/ $$/  $$$$$$/   Or get our lifetime freeplan!
                              $$ |                                  
                              $$ |  discord.gg/invitehere -- For support, you should join this!                    
                              $$/   \n\n                            -- -- -- -- -- -- -- -- -- -- \n\n                                  github.com/PythonJoshua
                              
                            -- -- -- -- -- -- -- -- -- --\n      To get a list of commands, run the command: a.help on the support server in #cmd!
                            
                                    Activity Log:''')

@bot.event
async def on_ready():
    print('Thanks for choosing ApolloByte!')
    print(f'Currently logged in as: {bot.user.name}')
    print('Command logs loading.')
    print('Loading..')
    print('Loading...')
    print('Loading....')
    print('Successfully loaded! Please join the server by running the command: a.apollo')

input("""
Please verify that you with to continue:
Press Any 'Enter' To Verify: """)

print ("Thank you! Please remember it is not our fault if you get banned using this tool, it is your choice!\n")

@bot.command()
async def apollo(ctx):
    embed = discord.Embed(
        title="ApolloByte | BETA Release",
        description=
        "You most likely got told to run this command from our loader, it is highly advised that you join! [Join](https://discord.gg/invitehere)",
        colour=ctx.author.colour)
    embed.set_footer(text="MIT License | Copyright ©️ 2021, PythonJoshua | All rights reserved.")
    await ctx.message.delete()
    await ctx.send(embed=embed)

token = config.get('token')

bot.run(token, bot=False)

