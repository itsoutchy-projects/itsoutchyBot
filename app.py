import config
import discord
import ids

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot online as {client.user}")

@client.event
async def on_member_join(member : discord.Member):
    dm = await member.create_dm()
    await dm.send(f"Hi! Thanks for joining itsoutchy cave, to get access to the server, please verify via this link: https://itsoutchy-cave-verification.netlify.app/?id={member.id}")

@client.event
async def on_message(msg : discord.Message):
    if client.user.mention in msg.content:
        await msg.reply("Beep boop! I'm keeping the server cool!") # its dead but idfc
    if msg.channel == client.get_channel(ids.verification_dump):
        member = msg.guild.get_member(int(msg.content))
        if not member == None:
            # discord, screw you and your shitty buggy ahh client, your mobile app barely fucking works, i cant even update perms on my own server,
            # and not to mention the stupid amount of hidden features you like to shove in the weirdest menus :/
            await member.add_roles(msg.guild.get_role(ids.verified))
            print(f"Verified member: {member}")

client.run(config.TOKEN)