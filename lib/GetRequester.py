import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return response.content

    def load_json(self):
        response= requests.get(self.url)
        response.raise_for_status()
        return response.json()