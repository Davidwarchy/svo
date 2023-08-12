import os
import sys# add the parent directory of the "database" package to the Python path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)
from dotenv import load_dotenv
import openai
import time
from openai.error import RateLimitError
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)  # for exponential backoff
import json

load_dotenv()

openai.api_key = os.getenv("OPENAI_KEY")

if openai.api_key == 'OPEN_AI_KEY_WITHOUT_QUOTES':
    print("Please enter a valid OpenAI key in the .env file. You can obtain one from https://platform.openai.com/account/api-keys")
    exit()

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def completion_with_backoff(**kwargs):
    return openai.ChatCompletion.create(**kwargs)

def complete( system_msg, prompt ):
    try:
        completion = completion_with_backoff(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": system_msg },
                    {"role": "user", "content": prompt }
                ]
        )
    except RateLimitError as e:
        print("RateLimitError occurred:", e)
        print("Retrying after 5 seconds...")
        time.sleep(5)   
    return completion.choices[0].message["content"]

def extract_subject_action_object(json_str):
    try:
        data_json = json.loads(json_str)
        subject = data_json["subject"]
        action = data_json["action"]
        object_ = data_json["object"]
        return subject, action, object_
    except (json.JSONDecodeError, KeyError):
        return None