from openai import OpenAI
client = OpenAI()

thread_message = client.beta.threads.messages.create(
  "thread_G3WRBbT1l066ttJpfZn7er3X",
  role="user",
  content="Convert this Motoko code to the Rust code",
  file_ids=["file-taRhhWA4q231oQCkCJuKYz1i"]
)
'msg_lbJHQe1L2Alv7rFVDGBPq0JB'

print(thread_message)