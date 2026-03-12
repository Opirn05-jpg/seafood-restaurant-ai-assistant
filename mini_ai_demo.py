import json
from openai import OpenAI

client = OpenAI()

with open("prompt_template.txt") as f:
    prompt = f.read()

with open("menu_template.json") as f:
    menu = json.load(f)

system_prompt = prompt + "\n\nMenu Database:\n" + json.dumps(menu)

while True:
    user = input("Customer: ")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user}
        ]
    )

    print("\nAI:", response.choices[0].message.content)
