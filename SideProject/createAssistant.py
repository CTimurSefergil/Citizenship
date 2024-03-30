from openai import OpenAI
client = OpenAI()

my_assistant = client.beta.assistants.create(
    instructions="You are an experienced Rust and Motoko developer tasked with converting Rust code to Motoko code. Provide the code without any commentary.",
    name="MotoRust",
    model="gpt-4-turbo-preview",
    tools=[{"type": "retrieval"}]
)