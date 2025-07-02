import requests
import pytest
import json


endpoint = "http://127.0.0.1:8000/api/students/"

def test_get_api_students():
    response = requests.get(endpoint)
    assert response.status_code == 200
    data = response.json()
    print(data['results'][0])
    assert isinstance(data, dict)
    assert len(data) > 0
    assert 'stu_name' in data['results'][0]
    assert 'stu_city' in data['results'][0]
    assert 'stu_id' in data['results'][0]
    assert 'stu_marks' in data['results'][0]


def test_get_api_students_by_id():
    response = requests.get(endpoint + "333/")
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert isinstance(data, dict)
    assert 'stu_name' in data
    assert 'stu_city' in data
    assert 'stu_id' in data
    assert 'stu_marks' in data


