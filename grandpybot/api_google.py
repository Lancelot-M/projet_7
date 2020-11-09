"""Calling google api class file."""

import requests
from config import GOOGLE_KEY

class ApiGoogle:
    """Google map requesting."""

    @staticmethod
    def search(target):
        """Make a request to google place api."""
        find_place = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
        params = {
            "key": GOOGLE_KEY,
            "input": target,
            "inputtype": "textquery",
            "fields": "formatted_address,place_id,types,geometry",
            "locationbias": "circle:1000000@48.856614,2.3522219"
        }
        place_reqested = requests.get(url=find_place, params=params)
        place_reqested = place_reqested.json()
        if place_reqested["status"] == "OK":
            formatted_address = place_reqested["candidates"][0]["formatted_address"]
            location = place_reqested["candidates"][0]["geometry"]["location"]
            wiki_call = ApiGoogle.cut_adress(formatted_address)
            data = {"status": "OK", "formatted_address": formatted_address, \
                    "location": location, "wiki_call": wiki_call}
            return data
        if place_reqested["status"] == "ZERO_RESULTS":
            return {"status": "ZERO_RESULTS"}
        return {"status": "INVALID_REQUEST"}

    @staticmethod
    def cut_adress(formatted_address):
        """Format data to be used by wiki api."""
        tuples = formatted_address.rpartition(",")
        tuples = tuples[0].partition(",")
        street = "".join([l for l in tuples[0] if not l.isdigit()])
        city = "".join([l for l in tuples[2] if not l.isdigit()])
        wiki_search = street + " (" + city + ")"
        return wiki_search
