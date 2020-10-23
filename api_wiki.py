import requests, sys, json

class Api_wiki:
    """Wiki class."""

    @staticmethod
    def find_pageid(wiki_call):
        url = "https://fr.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "list": "search",
            "srlimit":"1",
            "srsearch": wiki_call,
            "format": "json"
            }
        r = requests.get(url=url, params=params)
        r = r.json()
        return(r["query"]["search"][0]["pageid"])

    @staticmethod
    def page_info(pageid):
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
        r = requests.get(url=url, params=params)
        r = r.json()
        page_dict = r["query"]["pages"][str(pageid)]
        data = {"fullurl": page_dict["fullurl"], "extract": page_dict["extract"]}
        return data