import json
import requests

class Quote:

    def __init__(self, quote_request) -> str:
        self.quote_request = quote_request
        self.quote_url = "https://zenquotes.io/api/"

    def quotes(self) -> str:
        """
        Returns Quote and author

        random or today, needs to be passed in quote_request
        [
          {
            "q": "To do two things at once is to do neither.",
            "a": "Publilius Syrus",
            "h": "<blockquote>&ldquo;To do two things at once is to do neither.&rdquo; &mdash; <footer>Publilius Syrus</footer></blockquote>"
          }
        ]
        """
        if self.quote_request in ['today', 'random']:
            url = self.quote_url+self.quote_request
            data = requests.get(url, timeout=5)
            json_data = json.loads(data.text)
            quote, author = json_data[0]["q"], json_data[0]["a"]
            return f"{quote}\n\n*{author}*"
        else:
            return "Please enter today or random"