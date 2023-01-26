import json
import pytest
import requests
import logging
import os
from assertpy import assert_that

base_url = "https://www.aqa.science"


login = "admin"
password = "admin123"

@pytest.fixture(autouse=True, scope="module")
def log():
    logging.basicConfig(filename='test.log', encoding='utf8', level=logging.DEBUG)

@pytest.fixture(autouse=True, scope="module")
def change_data():
    return {
    }  #пустая структура для передачи данных.

def test_get(change_data):
    response = requests.get(base_url)
    data = response.json()
    assert_that(data).contains_key("users", "groups")
    change_data.update(data)   #передали весь json


def test_get_users(change_data):
    user_link = change_data['users']
    expected_keys = ['count', 'next', 'previous', 'results']
    response = requests.get(user_link, auth=(login, password)).json()
    assert_that(response).contains_key(* expected_keys)
    with open("response.json", "w") as f:
        json.dump(response, f, sort_keys=True, indent=4)


def test_get_next_users(change_data):
    next_url = "https://www.aqa.science/users/?page=2"
    expected_keys = ['count', 'next', 'previous', 'results']
    response = requests.get(next_url, auth=(login, password)).json()
    assert_that(response).contains_key(*expected_keys)
    with open("response.json", "a+") as f:
        f.seek(0, os.SEEK_END)
        json.dump(response, f, sort_keys=True, indent=4)


def test_create_new_user(change_data):
    user_post_data = {
                    "username": "IbragimHuseyn",
                    "email": "ibragimhy70@gmail.com",
                    "groups": []
    }
    user_link = change_data["users"]
    response = requests.post(user_link, user_post_data, auth=(login, password)).json()
    print(response)
    resp_success = ['url', 'username', 'email', 'groups']
    created_user_url = response['url']
    change_data["created_user_url"] = created_user_url
    assert_that(response).contains_key(*resp_success)


    #Добавляем данние по юзеру  в json файл.
    with open("response.json", "a+") as f:
        json.dump(response, f, sort_keys=True, indent=4)


#ф-н для апдейта существующего польщователя
def test_update_user(change_data):
    user_post_update_data = {
        "username": "IbragimHUSEYN",
        "email": "ibragimhy709230@gmail.com",
        "groups": []
    }



    user_link = change_data["created_user_url"]
    response = requests.post(user_link, user_post_update_data, auth=(login, password)).json()
    assert response.status_code == 200
    if response.status_code !=200:
        test_create_new_user(change_data)
    else:
        print(response)

#ф-н для удаления юзера по линку
def test_delete_user(change_data):
    user_link = change_data["created_usr_url"]
    response = requests.delete(user_link, auth=(login, password)).json()
    assert  response.status_code == 200
