

class Jury:
    def __vote__(self, vote):
        if vote == 1:
            self.vote = "Not Guilty"
        else:
            self.vote = "Guilty"


class Defendant:
    def __init__(self, name, argument, evidence, crime):
        self.name = name
        self.argument = argument
        self.evidence = evidence
        self.crime = crime

    def describe(self):
        return f"Defendant: {self.name}, Argument: {self.argument}"


def total_jury_vote(jlist):
    i = 0
    j = 0
    for item in jlist:
        if item.vote == "Guilty":
            i += 1
        else:
            j+=1
    if i > j:
        return f"The jury finds the defendant guilty"
    else:
        return f"The jury finds the defendant not guilty"

