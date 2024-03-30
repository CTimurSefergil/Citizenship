from openai import OpenAI
client = OpenAI()

mainThread = client.beta.threads.create()
'thread_G3WRBbT1l066ttJpfZn7er3X'
print(mainThread)