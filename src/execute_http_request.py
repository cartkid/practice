import requests
import json
from collections import namedtuple
from typing import Union, TypeVar, Type, cast


T = TypeVar("T")


def execute_get_request(
    url: str, tpe: Union[Type[T], None] = None, attempt: int = 0
) -> T:
    # headers = {"Authorization": f"Bearer {TWITTER_BEARER_TOKEN}"}
    response: requests.Response = requests.get(url=url)
    if (response.status_code != 200) and (attempt < 5):
        # try again
        return execute_get_request(url=url, tpe=tpe, attempt=attempt + 1)

    def genericDecoder(objDict):
        return namedtuple("Generic" if T is None else T.__name__, objDict.keys())(
            *objDict.values()
        )

    responseJson = json.loads(
        response.text,
        object_hook=genericDecoder,
    )
    if tpe is not None:
        return cast(tpe, responseJson)
    return responseJson


class DogBreeds:
    message: str = ""
    status: str = ""

    def __init__(self, message, status):
        self.message = message
        self.status = status

    @staticmethod
    def from_json(json_dct):
        return DogBreeds(json_dct["message"], json_dct["status"])


def test_execute_get_request():
    url = "https://dog.ceo/api/breeds/image/random"
    expected = "success"

    result = execute_get_request(url=url, tpe=DogBreeds)
    print(result)
    assert result.status == expected


def test_execute_get_request_no_type():
    url = "https://dog.ceo/api/breeds/image/random"
    expected = "success"

    result = execute_get_request(url=url)
    print(result)
    assert result.status == expected
