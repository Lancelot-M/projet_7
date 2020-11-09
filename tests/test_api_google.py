"""testing file api_google"""

import pytest
from grandpybot.api_google import ApiGoogle
from config import GOOGLE_KEY

def test_search_is_ok(monkeypatch):
    """"""
    
    def mock_get_requests(url, params):
        """mock request.get()"""
        class MockRequest:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code
            def json(self):
                return self.json_data
        data = {'candidates': [
        {'formatted_address': '10 Quai de la Charente, 75019 Paris, France', 
        'geometry': {'location': {'lat': 48.8975156, 'lng': 2.3833993}, 
        'viewport': {'northeast': {'lat': 48.89886702989273, 'lng': 2.384756379892722}, 
        'southwest': {'lat': 48.89616737010729, 'lng': 2.382056720107278}}}, 
        'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8', 'types': [
        'point_of_interest', 'establishment']}], 'status': 'OK'}
        return MockRequest(data, 200)

    def mock_cut_adress(formatted_address):
        """mock APiGoogle.cut_adress()"""
        return "Quai de la Charente (Paris)"
    monkeypatch.setattr('requests.get', mock_get_requests)
    monkeypatch.setattr('grandpybot.api_google.ApiGoogle.cut_adress', mock_cut_adress)
    assert ApiGoogle.search("maps_call") == {"status": "OK", 
        "formatted_address": "10 Quai de la Charente, 75019 Paris, France",
        "location": {'lat': 48.8975156, 'lng': 2.3833993}, 
        "wiki_call": "Quai de la Charente (Paris)"}

def test_search_no_result(monkeypatch):
    """test if api doesn't find anything"""

    def mock_get_requests(url, params):
        """mock request.get()"""
        class MockRequest:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code
            def json(self):
                return self.json_data
        return MockRequest({"status": "ZERO_RESULTS"}, 200)
    monkeypatch.setattr('requests.get', mock_get_requests)
    assert ApiGoogle.search("maps_call") == {"status": "ZERO_RESULTS"}

def test_search_is_ko(monkeypatch):
    """test if api got a error from request"""

    def mock_get_requests(url, params):
        """mock request.get()"""
        class MockRequest:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code
            def json(self):
                return self.json_data
        return MockRequest({"status": "INVALID_REQUEST"}, 200)
    monkeypatch.setattr('requests.get', mock_get_requests)
    assert ApiGoogle.search("maps_call") == {"status": "INVALID_REQUEST"}

def test_cut_adress():
    """return street (city)"""
    adress = "10 Quai de la Charente, 75019 Paris, France"
    assert ApiGoogle.cut_adress(adress) == " Quai de la Charente (  Paris)"