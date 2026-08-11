import config
import discord
import ids
import embeds
import discord.app_commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Client(intents=intents)

tree = discord.app_commands.CommandTree(client=client)

prefix = "i!"

#create_button = None

@client.event
async def on_ready():
    print(f"Bot online as {client.user}")

@client.event
async def on_member_join(member : discord.Member):
    try:
        dm = await member.create_dm()
        await dm.send(f"Hi! Thanks for joining itsoutchy cave, to get access to the server, please verify via this link: https://itsoutchy-cave-verification.netlify.app/?id={member.id}")
    except:
        channel = client.get_channel(ids.unverified)
        await channel.send(f"{member.mention}, I could not DM you, perhaps you have DMs off? Please enable them temporarily as it's required to verify you, you can disable them after")

@client.event
async def on_message(msg : discord.Message):
    if msg.author == client.user:
        return
    if client.user.mention in msg.content:
        await msg.reply("Beep boop! I'm keeping the server cool!") # its dead but idfc
    if msg.channel == client.get_channel(ids.verification_dump):
        member = msg.guild.get_member(int(msg.content))
        if not member == None:
            # discord, screw you and your shitty buggy ahh client, your mobile app barely fucking works, i cant even update perms on my own server,
            # and not to mention the stupid amount of hidden features you like to shove in the weirdest menus :/
            await member.add_roles(msg.guild.get_role(ids.verified))
            print(f"Verified member: {member}")
    if msg.channel == client.get_channel(ids.music_drops) and msg.author == msg.guild.get_member(ids.monitoRSS):
        # music drops channel and MonitoRSS bot
        await msg.publish() # automatically publish notifs, saves me a job

    # commands
    if msg.content.lower().startswith(f"{prefix}tsetup"):
        # sets up a message with a button to let you make a ticket
        tchannel = msg.guild.get_channel(ids.tickets)
        view = discord.ui.View(timeout=None)
        global create_button
        create_button = discord.ui.Button(style=discord.ButtonStyle.primary, label="Create Ticket")
        view.add_item(create_button)
        await tchannel.send(content="Press the button to open a ticket, then describe your issue in the channel I send to you", view=view)

@client.event
async def on_message_delete(msg : discord.Message):
    # hehe you cant delete your messages to get away with doing something naughty >:)
    message_logs = msg.guild.get_channel(ids.message_logs)
    await message_logs.send(embed=embeds.message_delete(msg), silent=True)

@tree.command(name="delete-ticket", description="Deletes the ticket this command is used in. If it's actually a ticket")
async def delete_ticket_command(interaction : discord.Interaction):
    if interaction.guild.get_role(ids.staff_team) in interaction.user.roles:
        ticket_id = interaction.channel.name.removeprefix("ticket-")
        await interaction.response.send_message("Successfully deleted ticket (this'll go away it needs to be sent)")
        delete_ticket(ticket_id)
    else:
        await interaction.response.send_message(embed=embeds.insufficient_permissions("STAFF_TEAM"))
    
async def delete_ticket(id : int | str):
    t_category = discord.utils.get(client.guilds[0].categories, id=ids.tickets_cat)
    for c in t_category.channels:
        if c.name == f"ticket-{id}":
            await c.delete()
            return
    # if it gets here it means the ticket doesnt exist

client.run(config.TOKEN)