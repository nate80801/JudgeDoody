import discord
import chat as Doody
import traceback

async def send_message(message, message_content):
    await message.channel.send(message_content)




def run_discord_bot():
    print("running")
    intents = discord.Intents.default()
    intents.message_content = True
    TOKEN = 'MTE1MjQ1MzcyMzU5MTgyMzQyMg.GNV8p9.gqGt4UtvZiB0nKOEN8II5AbCeHyaPU-VdQRsdA'


    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print("Judge Doody on duty")


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        try:

            user = str(message.author)
            msg = str(message.content)
            chan = str(message.channel)

            print(f" {user} sent {msg} to {chan} \n")

            # Echo
            await send_message(message, msg)
        except:
            traceback.print_exc()



    client.run(TOKEN)
