import pytest
from check_post import get_login
import requests
import yaml


with open("config.yaml", "r") as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def token():
    return get_login()

@pytest.fixture()
def login():
    res1 = requests.post(data["path_1"], data={"username": data["username"], "password": data["password"]})
    return res1.json()["token"]

@pytest.fixture()
def find_id():
    return 91749

@pytest.fixture()
def title():
    return "Зимушка зима"

@pytest.fixture()
def description():
    return "Я люблю зимушку - зиму за эту чистоту на улицах, за веселые игры, за то волшебство, в которое так ве"
