import json
import requests

class NLPAPI:
    def __init__(self):
        self.base_url = "https://api.example.com/nlp"  # Corrected the attribute name

    def get_sentiment(self, text):
        """Gets the sentiment of the given text"""
        response = requests.get(f"{self.base_url}/sentiment?text={text}")
        if response.status_code == 200:
            data = json.loads(response.content)
            return data["sentiment"]
        else:
            return None
