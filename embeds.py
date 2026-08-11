import discord

def message_delete(msg : discord.Message):
    embed = discord.Embed(colour=discord.Colour.red(), title="Message deleted", description=f"User ID: {msg.author.id}\nUser Mention: {msg.author.mention}\n\nContent: {msg.content}")
    return embed

def get_guide(permission : str):
    if permission.lower() == "staff_team":
        return "You must be a staff member"
    if permission.lower() == "manage_roles":
        return "You need to be able to manage roles"
    return "No guide has been found for this permission, either the name should imply it or it has not been implemented, Google it"

def insufficient_permissions(permission : str):
    # Use SPECIFIC names, if you dont, it will never return a guide
    embed = discord.Embed(colour=discord.Colour.red(), title="Insufficient Permissions", description=f"You do not have the required permission {permission}\n\nGuide:\n{get_guide(permission)}")
    return embed