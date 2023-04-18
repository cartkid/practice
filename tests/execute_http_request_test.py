import src.execute_http_request as execute_http_request


def test_execute_get_request_with_type():
    url = "https://dog.ceo/api/breeds/image/random"
    expected = "success"

    result = execute_http_request.execute_get_request(
        url=url, tpe=execute_http_request.DogBreeds
    )
    print(result)
    assert result.status == expected


def test_execute_get_request_without_type():
    url = "https://dog.ceo/api/breeds/image/random"
    expected = "success"

    result = execute_http_request.execute_get_request(url=url)
    print(result)
    assert result.status == expected
