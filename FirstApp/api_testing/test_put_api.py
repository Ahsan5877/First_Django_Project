import requests
import pytest
import json

def test_put_api_students():
    endpoint = "http://127.0.0.1:8000/api/students/123/"
    data = {
        "stu_name": "Updated Student",
        "stu_city": "Los Angeles",
        "stu_id": 123,
        "stu_marks": 90
    }
    response = requests.put(endpoint, data)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert isinstance(data, dict)
    assert data['stu_name'] == "Updated Student"
    assert data['stu_city'] == "Los Angeles"
    assert data['stu_id'] == 123
    assert data['stu_marks'] == 90