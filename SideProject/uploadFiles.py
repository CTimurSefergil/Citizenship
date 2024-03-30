from openai import OpenAI
client = OpenAI()

client.files.create(
  file=open(r"C:\Users\90543\MiniDream\motoko_rust\smart_canister_examples\Contacts.txt", "rb"),
  purpose="assistants"
)

client.files.create(
  file=open(r"C:\Users\90543\MiniDream\motoko_rust\smart_canister_examples\HelloWorld.txt", "rb"),
  purpose="assistants"
)

client.files.create(
  file=open(r"C:\Users\90543\MiniDream\motoko_rust\smart_canister_examples\ToDoApp.txt", "rb"),
  purpose="assistants"
)