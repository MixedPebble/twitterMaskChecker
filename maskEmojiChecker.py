import requests
import os
from dotenv import load_dotenv

load_dotenv()

BEARER_TOKEN = os.getenv('BEARER_TOKEN')

# curl https://api.twitter.com/2/tweets/sample/stream -H "Authorization: Bearer $BEARER_TOKEN"

print("Connecting")
# 😷

headers = {
    'Authorization': BEARER_TOKEN,
}

# response = requests.get('https://api.twitter.com/2/tweets/sample/stream', headers=headers)
# print(response)
print("Finished")