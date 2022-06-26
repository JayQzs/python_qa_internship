import pytest
import requests

from config import *

@pytest.fixture
def get_users():
    response = requests.get(url=BASE_URL)
    return response

@pytest.fixture
def create_user():
    headers = {'Authorization': f'Bearer {TOKEN}'}
    response = requests.post(url=BASE_URL, headers=headers, data=USERS_DATA)
    return response

@pytest.fixture
def find_user():
    response = requests.get(f'{BASE_URL}/8')
    return response