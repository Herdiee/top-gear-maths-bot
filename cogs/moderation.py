# Dependencies
import discord
from discord.ext import commands


import colored
from colored import stylize


class Moderation(commands.Cog):


    def __init__(self, client):
        self.client = client


    # Purge command
    @commands.command(name="purge",
                      brief='Purge messages',
                      description='This command purges messages',
                      aliases=['clean','clear'],
                      )
    # Check that the user has manage messages permission
    @commands.has_permissions(manage_messages=True)
    # If no amount is specified, purge 5 messages
    async def purge(self, context, amount=5):
        try:
            # Purge the messages
            cleared_messages = await context.message.channel.purge(limit=amount)
            # Embed Creation
            embed = discord.Embed(
                title="Purged Messages!",
                description=f"**{len(cleared_messages)}** messages have been purged by **{context.message.author}**!",
                color=0xe67e22
            )
            # Send the embed
            await context.send(embed=embed)
            # Log to console
            print(stylize(f"Successfully cleared {len(cleared_messages)}", colored.fg("green")))
        except:
                # Log to console
                print(stylize(f"Error when {context.message.author} attempted to purge mesasges!", colored.fg("red")))
                # Reply with error message
                await context.send("Something went wrong!")


    # Ban command
    @commands.command(name="ban",
                      aliases=['bann'],
                      brief='Ban a member',
                      description='This command can be used to ban members'
                     )
    # Check that the user has the permissions to ban a member
    @commands.has_permissions(ban_members=True)
    async def ban(self, context, member: discord.Member, *args):
        try:
            # If the arguments contain a member that has administrator priviledges, send an erorr embed.
            if member.guild_permissions.administrator:
                # Embed Creation
                embed = discord.Embed(
                        title="Unable to ban user!",
                        description=f"There was an issue when trying to ban {member}, Perhaps they have permissions higher than the bot?",
                        color=0xe67e22
                        )
                # Send the embed
                await context.send(embed=embed)
                print(stylize(f"Error when banning {member}", colored.fg("red")))
            # If the member does not have admin permissions, ban them and send an embed.
            else:
                # Get the ban reason from the arguments provided by the administrator
                reason = " ".join(args)
                # Ban the user
                await member.ban(reason=reason)
                # Embed Creation
                embed = discord.Embed(
                    title="Banned a user!",
                        description=f"**{member}** has been banned by **{context.message.author}**!",
                        color=0xe67e22
                    )
                # Add the reason field 
                embed.add_field(
                        name="Reason:",
                        value=reason
                    )
                # Send the embed
                await context.send(embed=embed)
                # Log to console
                print(stylize(f"Successfully banned {member}", colored.fg("green")))
        except:
                # Log to console
                print(stylize(f"Error when banning {member}", colored.fg("red")))
                # Reply with error message
                await context.send("Something went wrong!")


    # Kick command
    @commands.command(name='kick',
                      pass_context=True,
                      brief='Kick a member',
                      description='This command can be used to kick a member'
                     )
    # Check that the user has the permission to kick a member
    @commands.has_permissions(kick_members=True)
    async def kick(self, context, member: discord.Member, *args):
        try:
            # If the arguments contain a member that has administrator priviledges, send an erorr embed.
            if member.guild_permissions.administrator:

                # Embed Creation
                embed = discord.Embed(
                        title="Unable to ban user!",
                        description=f"There was an issue when trying to ban {member}, Perhaps they have permissions higher than the bot?",
                        color=0xe67e22
                        )
                # Send the embed
                await context.send(embed=embed)
                print(stylize(f"Error when kicking {member}", colored.fg("red")))
            # If the member does not have admin permissions, ban them and send an embed.
            else:
                # Get the kick reason from the arguments provided by the administrator
                reason = " ".join(args)
                # Kick the user
                await member.kick(reason=reason)
                # Embed Creation
                embed = discord.Embed(
                    title="Kicked a user!",
                        description=f"**{member}** has been kicked by **{context.message.author}**!",
                        color=0xe67e22
                    )
                # Add the reason field 
                embed.add_field(
                        name="Reason:",
                        value=reason
                    )
                # Send the embed
                await context.send(embed=embed)
                # Log to console
                print(stylize(f"Successfully Kicked {member}", colored.fg("green")))
        except:
                # Log to console
                print(stylize(f"Error when kicking {member}", colored.fg("red")))
                # Reply with error message
                await context.send("Something went wrong!")
                


def setup(client):
    client.add_cog(Moderation(client))