import requests
import pytest
import json


def test_delete_api_students():
    endpoint = "http://127.0.0.1:8000/api/students/123/"
    response = requests.delete(endpoint)
    assert response.status_code == 204
    print("Student deleted successfully")
