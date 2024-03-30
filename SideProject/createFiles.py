from openai import OpenAI
client = OpenAI()

assistant_file = client.beta.assistants.files.create(
  assistant_id="asst_tOUKOrCw6chGZHjDO7dciDpU",
  file_id="file-SQMFFnW1OO4zWlnrHOb76qt8"
)

assistant_file = client.beta.assistants.files.create(
  assistant_id="asst_tOUKOrCw6chGZHjDO7dciDpU",
  file_id="file-e9PPKXQFO55dMfV2CpOneqGE"
)

assistant_file = client.beta.assistants.files.create(
  assistant_id="asst_tOUKOrCw6chGZHjDO7dciDpU",
  file_id="file-taRhhWA4q231oQCkCJuKYz1i"
)