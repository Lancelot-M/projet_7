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