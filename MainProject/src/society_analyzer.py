'''
Vatandaş verilerinin json uzantılı dosyadan okunup yapay zekaya aktarılmasını,
analiz edilmesini ve ardından analizlerin hem gelecekte kullanılması için hem de verilerin güvenliği için
bir başka json uzantılı dosyaya kayıt edildiği kodlar
'''

from openai import OpenAI
import json

with open("/home/timur/motoko_workshop/rfinal_project/Citizenship/src/Citizenship_backend/all_data/data.json") as json_file:
    data = json.load(json_file)
    data1 = json.dumps(data)
    json_file.close()


client = OpenAI()

completition = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a wise and inteligent sociologist, you will be given a list of citizens, your goal is to analyze this society"},
        {"role": "user", "content": "Analyze this data" + data1},
    ]
)

print(completition.choices[0].message)

with open("/home/timur/motoko_workshop/rfinal_project/Citizenship/src/Citizenship_backend/all_data/ai_responses.json", "w", newline="") as data:
        data.write(json.dumps(str(completition.choices[0].message)))
        data.close()



