import requests
import json
from collections import namedtuple
from typing import Any


def execute_get_request(url: str, attempt: int = 0) -> Any:
    return_me: bool = False
    # headers = {"Authorization": f"Bearer {TWITTER_BEARER_TOKEN}"}
    response: requests.Response = requests.get(url=url)
    if (response.status_code != 200) and (attempt < 5):
        # try again
        return execute_get_request(url=url, attempt=attempt + 1)

    def genericDecoder(objDict):
        return namedtuple("X", objDict.keys())(*objDict.values())

    responseJson = json.loads(response.text, object_hook=genericDecoder)
    return responseJson


class DogBreeds:
    message: str = ""
    status: str = ""


def test_execute_get_request():
    url = "https://dog.ceo/api/breeds/image/random"
    expected = "success"

    result = execute_get_request(url=url)
    print(result)
    assert result.success == expected
