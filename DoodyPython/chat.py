import openai
openai.api_key = "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"

# Make prompt is to be used in opening_statement
def make_prompt(plaintiff, defendant, crime) -> str:
  # Make the prompt based on the parameters
  return f"""
  Today's trial:
  The defendant {defendant} is accused by plaintiff {plaintiff} of {crime}\n
  You are to introduce yourself as Judge Doody and give an introduction to the court.
  Do not give a final verdict, only introduce us.
  End your statement commencing the beginning of the trial
  """


async def opening_statement(defendant, plaintiff, crime):
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": make_prompt(defendant, plaintiff, crime)},
      {"role": "user", "content": "We will now let Judge Doody introduce the case"},

    ]
  )
  return str(response['choices'][0]['message']['content'])



# Pass in the full log of evidence statements (EXPENSIVE FOR API!!)
# Return [verdict, sentence]
async def final_judgement(evidence, crime):
  judge = f"""
    Review the statements and decide whether the defendant is guilty.
    You must declare whether they are "Guilty" or "Not Guilty" of {crime} then give closing remarks as to why.
    Take the jury's decision into account, you may go against the jury's judgement.
  """

  # This function takes in a string and generates a response from chatGPT
  verdict_statement = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": evidence},
      {"role": "user", "content": judge},

    ]
  )
  verdict_statement = str(verdict_statement['choices'][0]['message']['content'])

  verdict = verdict_statement.split()
  for i in verdict:
    if i[0] == "\"":
        if(i[1].lower()) == "n":
            verdict = "Not Guilty"
            break
        elif(i[1].lower() == "g"):
            verdict = "Guilty"
            break
  sentence_statement = await(sentence(verdict, crime))

  return [verdict_statement, sentence_statement]


async def sentence(verdict, crime):
  context = f"The defendant has been found {verdict} of {crime}"
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": context},
      {"role": "user", "content": "You must decide on a funny and wacky sentence for him. Only say the sentence"},

    ]
  )
  return str(response['choices'][0]['message']['content'])