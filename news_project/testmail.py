import os
from dotenv import load_dotenv

load_dotenv()
user = os.getenv('mailuser')

print(user)