import os
from dotenv import load_dotenv
import plaid
from plaid.api import plaid_api



load_dotenv()
PLAID_CLIENT_ID = os.getenv("PLAID_CLIENT_ID")
PLAID_SECRET = os.getenv("PLAID_SECRET")

configuration = plaid.Configuration(host=plaid.Environment.Sandbox, 
    api_key={
        'clientId': PLAID_CLIENT_ID,
        'secret': PLAID_SECRET
    }
)