
from datetime import datetime

class Tweet:
    id = None

    def __init__(self, text: str):
        self.text = text
        self.created_at = datetime.now()

    def __str__(self):
        return self.text
