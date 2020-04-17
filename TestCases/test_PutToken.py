import requests
import json
import jsonpath

# API Get Token
url = "http://127.0.0.1:8000/v1/api-token-auth/"


def test_post_token():
    file = open("../flowApiRest/TestCases/body.json")
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    print(response.content)
    response_json = json.loads(response.text)
    token = jsonpath.jsonpath(response_json, 'token')
    assert token[0] == '3289b551c28b65b32fe6c8b94215121d2bc36b7c'


def test_post_token_other():
    file = open("../flowApiRest/TestCases/body.json")
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    print(response.content)
    response_json = json.loads(response.text)
    token = jsonpath.jsonpath(response_json, 'token')
    assert response.status_code == 200
