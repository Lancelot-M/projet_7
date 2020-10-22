import requests, sys, json

class Api_wiki:
    """Wiki class."""

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
        print(r["query"]["search"][0]["pageid"])

        return(r["query"]["search"][0]["pageid"])

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

        """
        with open("google_result.json", "w") as f:
            f.write(json.dumps(page_dict))
        """

        data = {"fullurl": page_dict["fullurl"], "extract": page_dict["extract"]}

        return data

if __name__ == "__main__":

    Api_wiki.find_pageid("rue de villiers ( Poissy)")