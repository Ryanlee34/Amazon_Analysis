import requests
import os
from dotenv import load_dotenv

def configure():
    load_dotenv()

class OpenExchangeClient:

    def __init__(self, app_id):
        self.app_id = app_id

    def latest(self):
        return requests.get(f"https://openexchangerates.org/api/latest.json?app_id={os.getenv('API_KEY')}").json()



    def convert(self, from_amount, from_currency):
        rates = self.latest["rates"]
        return from_amount * (1 / rates[from_currency])




