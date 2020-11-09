"""testing file for system.py"""

import pytest
from grandpybot.system import System
from grandpybot.stop_words import STOP_WORDS

@pytest.fixture
def object_test():
    """setup who initialize a objet System for test"""
    
    question = "Bonjour GrandPyBot ! Je recherche l'adresse d'Openclassrooms."
    test = System(question)
    yield test

def test_questionning_return_dict(monkeypatch, object_test):
    """return a dict of datas"""

    def mock_parse_pass(self):
        """mock parsing_question()"""
        pass
    def mock_google_pass(self):
        """mock google_caller()"""
        pass
    def mock_wiki_pass(self):
        """mock wiki_caller()"""
        pass
    monkeypatch.setattr('grandpybot.system.System.parse_question', mock_parse_pass)
    monkeypatch.setattr('grandpybot.system.System.google_caller', mock_google_pass)
    monkeypatch.setattr('grandpybot.system.System.wiki_caller', mock_wiki_pass)
    
    assert object_test.questionning() == {"question": "Bonjour GrandPyBot ! Je recherche l'adresse d'Openclassrooms.",
                                            "wiki_call": "",
                                            "wiki_answ": {},
                                            "maps_call": [],
                                            "maps_answ": {}}

def test_parsing(monkeypatch, object_test):
    """keep only essential of the informations"""
    
    def mock_cut_from_last(list1, list2):
        """mock cut_from_last()"""
        return ["adresse", "d", "Openclassrooms"]
    #monkeypatch.setattr('grandpybot.system.System.cut_from_last', mock_cut_from_last)
    object_test.parse_question()
    
    assert object_test.data["maps_call"] == "adresse Openclassrooms"

def test_cutfromlast():
    """cut list on the before last stop word"""
    
    list_test = ["Je", "suis", "a", "la", "recherche", "des", "bureaux", "d", "Openclassrooms"]
    assert System.cut_from_last(list_test, STOP_WORDS) == ["bureaux", "d", "Openclassrooms"]

def test_google_caller(monkeypatch, object_test):
    """add data from maps call on object"""
    
    def mock_randrange(number):
        """mock random.randrange()"""
        return 0
    monkeypatch.setattr('random.randrange', mock_randrange)
    
    def mock_search_is_ok(maps_call):
        """mock ApiGoogle.search()"""
        results = {"status": "OK", "formatted_address": "10 Quai de la Charente, \
75019 Paris, France",
                    "location": {"lat": 0.000, "lng": 0.000 }, "wiki_call": 'wiki_call'}
        return results
    monkeypatch.setattr('grandpybot.api_google.ApiGoogle.search', mock_search_is_ok)
    
    object_test.google_caller()
    expected = {"formatted_address": 'Je connais bien cet endroit mon petit chat. \
Il se situe au 10 Quai de la Charente, 75019 Paris, France',
        "location": {"lat": 0.000, "lng": 0.000 }}
    assert object_test.data["maps_answ"] == expected

    def mock_search_no_result(maps_call):
        """mock ApiGoogle.search()"""
        results = {"status": "ZERO_RESULTS"}
        return results
    monkeypatch.setattr('grandpybot.api_google.ApiGoogle.search', mock_search_no_result)
    object_test.google_caller()
    assert object_test.data["maps_answ"] == "Oula! Je ne connais pas l'adresse de cet\
                                        établissement. Quelle déception !!!"

    def mock_search_is_error(maps_call):
        """mock ApiGoogle.search()"""
        results = {"status": "INVALID_REQUEST"}
        return results
    monkeypatch.setattr('grandpybot.api_google.ApiGoogle.search', mock_search_is_error)
    
    object_test.google_caller()
    assert object_test.data["maps_answ"] == "Que me demandes tu mon petit? Tu sais avec\
                                        papy il faut bien expliquer!"

def test_wiki_caller(monkeypatch, object_test):
    """add data from wiki call if status == 1"""
    
    def mock_findpage(wiki_call_data):
        """mock ApiWiki.fing_pageid()"""
        return "nothing"
    def mock_page_info(findpage_data):
        """mock ApiWiki.page_info"""
        return {"fullurl": 'text_url', "extract": 'text_wiki_page'}
    monkeypatch.setattr('grandpybot.api_wiki.ApiWiki.find_pageid', mock_findpage)
    monkeypatch.setattr('grandpybot.api_wiki.ApiWiki.page_info', mock_page_info)
    
    object_test.wiki_caller()
    assert object_test.data["wiki_answ"] == {}
    
    object_test.data["maps_call"] = 1
    object_test.wiki_caller()
    assert object_test.data["wiki_answ"] == {"fullurl": 'text_url', 
                                            "extract": 'text_wiki_page'}
