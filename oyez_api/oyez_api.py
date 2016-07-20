import requests

BASE_URL = 'https://www.oyez.org/'
BASE_API_URL = 'https://api.oyez.org/'

def cases(term):
    url = BASE_API_URL + "cases?filter=term:" + str(term)
    return requests.get(url).json()

def case(term, docket_num):
    url = BASE_API_URL + "cases/" + str(term) + "/" + docket_num
    return requests.get(url).json()

def transcript_data(term, docket_num):
    case_data = case(term, docket_num)
    return [ requests.get(data["href"]).json() for data in case_data["oral_argument_audio"] ]
