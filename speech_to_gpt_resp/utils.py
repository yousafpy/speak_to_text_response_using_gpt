import openai
openai.api_key = ""
def chat_bot_message_gpt3(messages):
    chat_compleion_obj = openai.ChatCompletion.create(
        model="gpt-4",
        max_tokens=1100,
        messages=[{"role": "user", "content": messages}],
        temperature=0.2
    )
    return chat_compleion_obj.choices[0].message['content']