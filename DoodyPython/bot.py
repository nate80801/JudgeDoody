import discord
import chat as doody
import traceback
import trial

class doc:
    def __init__(self):
        self.f = open("log.txt", 'w')
    def log(self, msg):
        self.f.write(msg)

class case:
    def __init__(self, defendant, plaintiff, crime):
        self.defendant = defendant
        self.plaintiff = plaintiff
        self.crime = crime
    def change(self, defendant, plaintiff, crime):
        self.defendant = defendant
        self.plaintiff = plaintiff
        self.crime = crime


CASE = case("default", "default", "default")
evidence = doc()

CASE_ON = False

def flip_bool():
    global CASE_ON
    CASE_ON = not(CASE_ON)



def run_discord_bot():
    print("running")
    intents = discord.Intents.default()
    intents.message_content = True
    TOKEN = 'MTE1MjQ1MzcyMzU5MTgyMzQyMg.GNV8p9.gqGt4UtvZiB0nKOEN8II5AbCeHyaPU-VdQRsdA'
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print("Judge Doody on duty")

    async def send_message(message):
        await message.channel.send(message.content)




    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.content == "/quit":
            # Quit
            print("Quit")
            return
        user = str(message.author)
        chan = (message.channel)
        msg = str(message.content)
        if CASE_ON:
            # Sent a message DURING a case
            if msg == "/done":
                # Break give verdict
                flip_bool()
                response = doody.final_judgement(evidence.f, CASE.crime)

                await send_message(response)

                return
            doc.log(str(message.content))
            await send_message("The other side may speak now")
        else:
            if msg[:4] == "/sue":
                flip_bool()
                msg = msg[4:]
                CASE.change(msg[:msg.index(" ")], user, msg[msg.index(" ") + 1:])
                await send_message(message)






            # Case is on, so we alternate between people talking
