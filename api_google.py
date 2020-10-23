import sys, json, requests
from GrandPyBot.config_perso import API_KEY

class Api_google:
    """Google map requesting."""

    @staticmethod
    def search(target):
        #Make a request to google place api.
        find_place = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
        params = {
            "key": API_KEY,
            "input": target,
            "inputtype": "textquery",
            "fields": "formatted_address,place_id,types,geometry"
        }
        r = requests.get(url=find_place, params=params)
        r = r.json()
        if r["status"] == "OK":
            formatted_address = r["candidates"][0]["formatted_address"]
            location = r["candidates"][0]["geometry"]["location"]
            wiki_call = Api_google.cut_adress(formatted_address)
            data = {"status": "OK", "formatted_address:": formatted_address, "location:": location, "wiki_call": wiki_call}
            return data
        elif r["status"] == "ZERO_RESULTS":
            return {"status": "ZERO_RESULTS"}
        else:
            return {"status": "INVALID_REQUEST"}

    @staticmethod
    def cut_adress(formatted_address):
        #Format data to be used by wiki api.
        tuples = formatted_address.rpartition(",")
        tuples = tuples[0].partition(",")
        street = "".join([l for l in tuples[0] if not l.isdigit()])
        city = "".join([l for l in tuples[2] if not l.isdigit()])
        wiki_search = street + " (" + city + ")"
        return wiki_search