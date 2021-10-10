import discord

client = discord.Client()

@client.event
async def on_ready():
    print("Le bot est prêt ma gueule")

@client.event
async def on_message(message):
    if message.content.lower() == "pong":
        await message.channel.send("ping")



client.run("ODgwNDQzODM4MTkwMjExMDky.YSeXOA.WemNVG1NB8z_Kiq7R1fx3ZTegFc")