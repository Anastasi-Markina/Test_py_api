import pytest
from check_post import get_post

id_check = 91749


def test_1(token):
    output = get_post(token)['data']
    res = []
    for item in output:
        res.append(item['id'])
        assert id_check in res
