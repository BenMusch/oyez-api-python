import requests

BASE_URL = "https://www.oyez.org/"
BASE_API_URL = "https://api.oyez.org/"
BASE_SEARCH_URL = "https://beta-search.oyez.org/elasticsearch_index_scotus_nodes/_search"

def __get(path, base_url=BASE_API_URL):
    url = "{}{}".format(BASE_API_URL, path)
    return requests.get(url).json()

def search(keyword):
    data = { "size": 20, "query": {
        "multi_match": {
            "query": keyword,
            "type": "cross_fields",
            "fields":["field_docket_number^3","field_additional_docket_numbers^3","title^2","field_court_term","field_first_party","field_second_party"]}}}

    return requests.post(BASE_SEARCH_URL, json=data).json()

def cases(term):
    path = "cases?filter=term:{}".format(term)
    return __get(path)

def case(term, docket_num):
    path = "cases/{}/{}".format(term, docket_num)
    return __get(path)

def transcript_data(term, docket_num):
    case_data = case(term, docket_num)
    return [ requests.get(data["href"]).json() for data in case_data["oral_argument_audio"] ]
