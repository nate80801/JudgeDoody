import chat as doody
import bot


class Person:
    # Class used for defendant or plaintiff

    def __init__(self):
        self = None
    def __init__(self, name, next, title):
        self.name = name
        self.next = next
        self.title = title




class Trial:
    # Pass in the names of defendant and plaintiff
    def __init__(self, defend, plaint, crime, channel):
        self.defendant = Person(defend, None, "defendant")
        self.plaintiff = Person(plaint, self.defendant, "plaintiff")
        self.crime = crime
        self.transcript = open("log.txt", 'w')
        self.channel = channel

        #Current holds the name of the next speaker
        self.current = self.plaintiff

    def log(self, msg, author):
        self.transcript.write(f"\n{author}: {msg} \n")
    async def call(self):
        # User sends message to discord, so we move to next person
        if self.current is None:
            return
        self.current = self.current.next







    # Log everything from now on...

    # Judge makes opening statements
    async def get_opening(self):
        opening = await doody.opening_statement(self.defendant.name, self.plaintiff.name, self.crime)
        return opening

    # Calls the plaintiff


        # Plaintiff can call witnesses if they want
        # If they don't they can just say their piece
    # Calls defendant
        # Can call witness if want
    # Pass the log back to the judge for final judgement
