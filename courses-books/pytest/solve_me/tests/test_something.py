import requests

from src.enums.global_enums import GlobalErrorMessages


URL = 'https://my-json-server.typicode.com/typicode/demo/posts'


def test_getting_posts():
    response = requests.get(url=URL)
    posts = response.json()

    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert len(posts) == 3, GlobalErrorMessages.WRONG_ELEMENT_SIZE.value

    print(response.json())