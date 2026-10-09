import requests
from pprint import pprint
import json
from dotenv import load_dotenv
import os

load_dotenv()

BOARD_TOKEN = os.getenv('GREENHOUSE_BOARD_TOKEN')

BASE_URL = 'https://boards-api.greenhouse.io/v1/boards'

response = requests.get(f'{BASE_URL}/{BOARD_TOKEN}/jobs?content=true')

pprint(response.json())

with open('artifacts/playground/greenhouse_response.json', 'w', encoding='utf-8') as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=4)
    f.write('\n')