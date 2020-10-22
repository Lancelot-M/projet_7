<<<<<<< HEAD
#!/usr/bin/python3

from GrandPyBot import parse
import sys

class Api_google:
	"""Google map requesting."""

	def search(list_word):
		url = ""
		params = {}

		r = requests.get(url=url, params=params)
		r = r.json()
		return(???)

if __name__ == "__main__":

	print(Api_google.search(sys.argv[1]))
=======
import sys, json, requests
from config_perso import API_KEY

class Api_google:
    """Google map requesting."""

    def search(target):
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
            data = {"formatted_address:": formatted_address, "location:": location, "wiki_call": wiki_call}
            return data
        else:
            return "not found"

    def cut_adress(formatted_address):

        tuples = formatted_address.rpartition(",")
        tuples = tuples[0].partition(",")

        street = "".join([l for l in tuples[0] if not l.isdigit()])
        city = "".join([l for l in tuples[2] if not l.isdigit()])

        wiki_search = street + " (" + city + ")"

        return wiki_search

if __name__ == "__main__":

    Api_google.search(sys.argv[1])
>>>>>>> e062b41... try connect
