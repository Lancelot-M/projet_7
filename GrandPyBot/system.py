#!/usr/bin/python3
# coding: utf-8
"""File contain core the core class of application."""

import random
from GrandPyBot.api_google import ApiGoogle
from GrandPyBot.api_wiki import ApiWiki
from GrandPyBot.stop_words import STOP_WORDS

class System:
    """Core class."""

    def __init__(self, question):
        self.data = {"question": question,
        "wiki_call": "",
        "wiki_answ": {},
        "maps_call": [],
        "maps_answ": {}}

    def questionning(self):
        """Main function. Actived from view.py"""
        self.parse_question()
        self.google_caller()
        self.wiki_caller()
        data = self.data
        return data

    def parse_question(self):
        """take essential of information"""
        maps_call = self.data["question"].replace("\'", " ").replace("?", "").replace(".", "")\
                        .replace("!", "")
        maps_call = maps_call.split(" ", -1)
        for word in maps_call:
            if word == '':
                maps_call.remove(word)
        maps_call = System.cut_from_last(maps_call, STOP_WORDS)
        for word in maps_call:
            if word in STOP_WORDS:
                maps_call.remove(word)
        maps_call = " ".join(maps_call)
        self.data["maps_call"] = maps_call

    @staticmethod
    def cut_from_last(list1, list2):
        """Keep end from last stop word."""
        index = 0
        count = 0
        stop_words = 0
        for el1 in list1:
            for el2 in list2:
                if el1 == el2:
                    stop_words += 1
        if stop_words > 1:
            for el1 in list1:
                for el2 in list2:
                    if el1 == el2:
                        index += 1
                        if index + 1 == stop_words:
                            del list1[0: count + 1]
                            return list1
                count += 1
        return list1

    def google_caller(self):
        """Call ApiGoogle class."""
        memory = ["Je connais bien cet endroit mon petit chat. Il se situe au ", \
                    "GrandPy à toujours la solution! Tu trouveras l'objet de tes désirs au, ", \
                    "Ne t'inquiète pas ma caille, je sais où c'est... "]
        data = ApiGoogle.search(self.data["maps_call"])
        if data["status"] == "OK":
            del data["status"]
            self.data["wiki_call"] = data["wiki_call"]
            del data["wiki_call"]
            data["formatted_address"] = memory[random.randrange(3)] + data["formatted_address"]
            self.data["maps_answ"] = data
            self.data["maps_call"] = 1
        elif data["status"] == "ZERO_RESULTS":
            self.data["maps_answ"] = "Oula! Je ne connais pas l'adresse de cet\
                                        établissement. Quelle déception !!!"
            self.data["maps_call"] = 2
        else:
            self.data["maps_answ"] = "Que me demandes tu mon petit? Tu sais avec\
                                        papy il faut bien expliquer!"
            self.data["maps_call"] = 3

    def wiki_caller(self):
        """Call ApiWiki class"""
        if self.data["maps_call"] == 1:
            data = ApiWiki.find_pageid(self.data["wiki_call"])
            self.data["wiki_answ"] = ApiWiki.page_info(data)
