import discord
import chat as doody
import traceback
import time

class doc:
    def __init__(self):
        self.t = []
    def log(self, msg):
        self.t.append(msg)
    def reed(self):
        return "".join(self.t)

class case:
    def __init__(self, defendant, plaintiff, crime):
        self.defendant = defendant
        self.plaintiff = plaintiff
        self.crime = crime
        self.turn = self.plaintiff

    def change(self, defendant, plaintiff, crime):
        self.defendant = defendant
        self.plaintiff = plaintiff
        self.crime = crime
        self.turn = self.plaintiff


    def turn_switch(self):
        if str(self.turn) == str(self.plaintiff):
            self.turn = self.defendant
        else:
            self.turn = self.plaintiff



CASE = case("default", "default", "default")
transcript = doc()

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
        print("Judge Truly on duty")


    Guilty = 0
    Not_guilty = 0





    async def jury_verdict(guilty, not_guilty):
        if guilty > not_guilty:
            return ("The jury finds the defendant guilty of all charges")
        elif guilty < not_guilty:
            return ("The jury finds the defendant not guilty of all charges")
        else:
            return("")

    async def send_message(message, chan, user):
        await chan.send(message)
        transcript.log(f"@{user}: {message}")




    @client.event
    async def on_message(message):

        if message.author == client.user:
            return
        if message.content == "/help":
            await send_message(doody.commands, message.channel, message.author)

        if message.content == "/quit":
            # Quit
            CASE.change("default", "default", "default")
            transcript.t.clear()

            print("Quit")
            return

        if CASE_ON:
            # Sent a message DURING a case
            if (CASE.turn == CASE.defendant) and str(message.content).lower() == "/rest":
                # Break give verdict
                await send_message("Gathering my thoughts...", message.channel, "Judge Truly")
                await send_message("Considering jury decision...", message.channel, "Judge Truly")

                # Wait 5 seconds to allow jury to decide
                time.sleep(5)
                chan = message.channel
                jury_vote = await chan.fetch_message(chan.last_message_id)
                rxns = jury_vote.reactions
                print(rxns)

                guilt, inn = 0, 0
                for i in rxns:
                    if i.emoji == "👎":
                        guilt += 1
                    elif i.emoji == "👍":
                        inn += 1



                flip_bool()
                jur = await (jury_verdict(guilt, inn))
                transcript.log(str(jur))
                print(jur)

                response = await doody.final_judgement(transcript.reed(), CASE.crime)


                await send_message("\n".join(response), message.channel, "Judge Truly")
                transcript.log(f"\nVERDICT: {response[0]}\nSENTENCE: {response[1]} ")

                f = open("log.txt", 'w')
                for i in transcript.t:
                    f.write(i)
                    f.write("\n")
                f.close()
                CASE.change("default", "default", "default")
                transcript.t.clear()

                return
            # Evidence bringer upper
            transcript.log(f"@{str(message.author)}: {str(message.content)}\n")

            CASE.turn_switch()
            await send_message(f"{CASE.turn} , could you briefly explain your side of the story?", message.channel, "Judge Truly")

        else:
            msg = str(message.content)
            user = "@" + str(message.author)
            if msg[:7] == "/accuse":
                flip_bool()
                msg = msg[8:]
                CASE.change(msg[:msg.index(" ")], user, msg[msg.index(" ") + 1:])
                await send_message("Court starts now", message.channel, "Judge Truly")
                transcript.log(f"DEFENDANT: {CASE.defendant}\nPLAINTIFF: {CASE.plaintiff}\nCHARGES: {CASE.crime}\n")
                await send_message(doody.opening_statement(CASE.defendant, CASE.plaintiff, CASE.crime), message.channel, "Judge Truly")

























    client.run(TOKEN)
