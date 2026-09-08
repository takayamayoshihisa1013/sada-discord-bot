import os
import requests
import random

WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')
secret_message = os.getenv('SILLY_MESSAGES', 'デフォルトのメッセージ')

silly_messages = secret_message.split(",")

message = random.choice(silly_messages)
data = {"content": message}

response = requests.post(WEBHOOK_URL, json=data)

if response.status_code == 204:
    print("送信成功！")
else:
    print(f"失敗しました: {response.status_code}")

print(message)
