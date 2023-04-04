import requests

from jsonschema import validate

from configuration import SERVICE_URL

from src.enums.global_enums import GlobalErrorMessages
from src.schemas.post import POST_SCHEMA

def test_getting_posts():
    response = requests.get(url=SERVICE_URL)
    received_posts = response.json()
    print(received_posts)
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert len(received_posts) == 6, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value
    validate(received_posts, POST_SCHEMA)



def test_getting_posts2():
    response = requests.get(url=SERVICE_URL)
    received_posts = response.json()
    print(received_posts)
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert len(received_posts) == 6, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value
    for item in received_posts:
        validate(item, POST_SCHEMA)
#Для тестов, где атомарная часть повторяется в схеме