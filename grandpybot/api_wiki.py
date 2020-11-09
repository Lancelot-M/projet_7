"""File contain the wikipedia requesting class."""

import requests

class ApiWiki:
    """Wiki class."""

    @staticmethod
    def find_pageid(wiki_call):
        """Loading page id function."""
        url = "https://fr.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "list": "search",
            "srlimit":"1",
            "srsearch": wiki_call,
            "format": "json"
            }
        wiki_request = requests.get(url=url, params=params)
        wiki_request = wiki_request.json()
        return wiki_request["query"]["search"][0]["pageid"]

    @staticmethod
    def page_info(pageid):
        """Loading page info with page id function."""
        url = "https://fr.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "prop": "info|extracts",
            "pageids": pageid,
            "inprop": "url",
            "explaintext": "1",
            "exsentences": "3",
            "format": "json"
            }
        wiki_request = requests.get(url=url, params=params)
        wiki_request = wiki_request.json()
        page_dict = wiki_request["query"]["pages"][str(pageid)]
        data = {"fullurl": page_dict["fullurl"], "extract": page_dict["extract"]}
        return data
