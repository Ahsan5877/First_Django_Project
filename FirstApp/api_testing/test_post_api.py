import requests
import pytest
import json




def test_post_api_students():
    endpoint = "http://127.0.0.1:8000/api/students/"
    data = {
    "stu_name": "Dummy Student",
    "stu_city": "New York",
    "stu_id": 123,
    "stu_marks": 85
}
    response = requests.post(endpoint, data)
    assert response.status_code == 201
    data = response.json()
    print(data)
    assert isinstance(data, dict)
    assert data['stu_name'] == "Dummy Student"
    assert data['stu_city'] == "New York"
    assert data['stu_id'] == 123
    assert data['stu_marks'] == 85