import discord

def message_delete(msg : discord.Message):
    embed = discord.Embed(colour=discord.Colour.red(), title="Message deleted", description=f"User ID: {msg.author.id}\nUser Mention: {msg.author.mention}\n\nContent: {msg.content}")
    return embed