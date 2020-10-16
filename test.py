import requests

class Wiki_api:
    """Wiki class."""

    def load_page(page_title):
        url = "https://fr.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "format": "json",
            "formatversion": "2",
            "titles": page_title,
            "prop": "extracts",
            "explaintext": "1",
            "exsentences": "3"
            }

        r = requests.get(url=url, params=params)
        r = r.json()
        return(r["query"]["pages"][0]["extract"])