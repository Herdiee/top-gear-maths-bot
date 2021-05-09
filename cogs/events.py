# Dependencies
import discord
import json
from discord.ext import commands

import colored
from colored import stylize

# Load the config file
with open('./config.json', 'r') as configfile:
    config = json.load(configfile)

class Misc(commands.Cog):


    def __init__(self, client):
        self.client = client


    # Event triggered when the bot is online
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Old (better) Top Gear"))
        print('Bot is online.')


    # Event triggered when a member joins
    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed = discord.Embed(
            title="**Welcome Message",
            description="Welcome to Top Gear Maths Shed! We hope you enjoy your stay :D",
            color=0x2ecc71
            )
        embed.set_thumbnail(url = member.avatar_url)
        await member.send(embed=embed)

      
    # Ping Command
    @commands.command(name='ping',
                      brief='PONG',
                      description='Get the latency',
                      aliases=['pong']
                     )
    async def ping(self, ctx):
        await ctx.send('Pong!')

    
    # Suggest Command
    @commands.command(name='suggest',
                      brief='Make a suggestion',
                      description='Suggest things to improve the server',
                      aliases=['suggestion']
                      )
    async def suggest(self, context, *, message):
        imgembed= discord.Embed(
                  title="Suggestion",
                  description=f"{message}"
                  )
        imgembed.set_footer(text=f"From {context.author}", icon_url=context.author.avatar_url)
        try:
            image = context.message.attachments[0].url
            imgembed.set_image(url=image)
        except IndexError:
            image = None
        embmessage = await context.send(embed=imgembed)
        await embmessage.add_reaction("✅")
        await embmessage.add_reaction("❌")


    # Tutor Help
    @commands.command(name='tutor',
                      brief='Ping all tutors',
                      description='Ping all tutors',
                      aliases=['helpers']
                      )
    async def suggest(self, context, *, message):
        math_helper = discord.utils.get(context.guild.roles, id=config["tutor_role"])
        await context.send(f"{math_helper.mention} please help {context.author.mention} with ```{message}```")


def setup(client):
    client.add_cog(Misc(client))
    