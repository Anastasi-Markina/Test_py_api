import yaml

with open('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)


def get_login():
    path = data['path_1']
    post = requests.post(url=path, data={'username': data['username'], 'password': data['password']})
    if post.status_code == 200:
        return post.json()['token']


def get_post(token):
    path_1 = 'https://test-stand.gb.ru/api/posts'
    get = requests.get(url=path_1, params={"owner": "notMe"}, headers={"X-Auth-Token": token})
    if get.status_code == 200:
        return get.json()
    
    
def test_1(login, find_id):
    res = requests.get(data["path"], params={"owner":"notMe"}, headers={"X-Auth-Token": login})
    list_id = [i["id"] for i in res.json()["data"]]
    assert find_id in list_id, "test_1 failed"


def test_2(login, title, description, content, find_description):
    res1 = requests.post(data["path"], params={"title": title, "description": description, "content": content},
                         headers={"X-Auth-Token": login})
    res2 = requests.get(data["path"], params={"description": find_description}, headers={"X-Auth-Token": login})
    assert res1 and res2, "test_2 failed"


if __name__ == '__main__':
    token = get_login()
    print(get_post(token))
