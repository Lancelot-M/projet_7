import requests
from GrandPyBot.api_wiki import ApiWiki

def test_find_pageid(monkeypatch):
    """return the pageid from wiki_call"""
    def mock_get_requests(url, params):
        """mock request.get()"""
        class MockRequest:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code
            def json(self):
                return self.json_data
        data = {'query': {'search': [{'pageid': 156862, 'size': 10181}]}}
        return MockRequest(data, 200)
    monkeypatch.setattr('requests.get', mock_get_requests)
    assert ApiWiki.find_pageid("Quai de la Charente (Paris)") == 156862

def test_page_info(monkeypatch):
    """return dict with url + page info"""
    def mock_get_requests(url, params):
        """mock request.get()"""
        class MockRequest:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code
            def json(self):
                return self.json_data
        data = {'query': {'pages': {'156862': {'pageid': 156862, 'ns': 0, 'title': "Quai d'Orsay", 
        'contentmodel': 'wikitext', 'pagelanguage': 'fr', 'pagelanguagehtmlcode': 'fr', 
        'pagelanguagedir': 'ltr', 'touched': '2020-11-05T01:28:41Z', 'lastrevid': 173066585, 
        'length': 10181, 'fullurl': 'https://fr.wikipedia.org/wiki/Quai_d%27Orsay', 
        'editurl': 'https://fr.wikipedia.org/w/index.php?title=Quai_d%27Orsay&action=edit', 
        'canonicalurl': 'https://fr.wikipedia.org/wiki/Quai_d%27Orsay', 
        'extract': "Le quai d’Orsay est un quai situé sur la rive gauche de la Seine dans le 7e arrondissement de Paris, où se trouvent notamment le ministère des Affaires étrangères, surnommé « quai d'Orsay », et le palais Bourbon.\n\n\n== Situation et accès ==\nCe quai débute au pont de la Concorde et rue Aristide-Briand et se termine au pont de l'Alma et place de la Résistance.\nIl désigne communément, par métonymie, le ministère des Affaires étrangères, qui y a son siège au no 37, dans un hôtel construit expressément pour abriter l’institution au milieu du XIXe siècle."}}}}
        return MockRequest(data, 200)
    monkeypatch.setattr('requests.get', mock_get_requests)
    assert ApiWiki.page_info(156862) == {"fullurl": 'https://fr.wikipedia.org/wiki/Quai_d%27Orsay', "extract": "Le quai d’Orsay est un quai situé sur la rive gauche de la Seine dans le 7e arrondissement de Paris, où se trouvent notamment le ministère des Affaires étrangères, surnommé « quai d'Orsay », et le palais Bourbon.\n\n\n== Situation et accès ==\nCe quai débute au pont de la Concorde et rue Aristide-Briand et se termine au pont de l'Alma et place de la Résistance.\nIl désigne communément, par métonymie, le ministère des Affaires étrangères, qui y a son siège au no 37, dans un hôtel construit expressément pour abriter l’institution au milieu du XIXe siècle."}
