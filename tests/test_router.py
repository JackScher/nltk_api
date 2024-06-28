import json
from flask.testing import FlaskClient


def test_tokenize(client: FlaskClient) -> None:
    response = client.post("/tokenize", data={"text": "At eight o'clock on Thursday morning. Arthur didn't feel very good."})
    assert response.status_code == 415
    assert "Content-Type must be application/json" in response.data.decode()

    response = client.post("/tokenize", json={"wrong_field": "At eight o'clock on Thursday morning. Arthur didn't feel very good."})
    assert response.status_code == 400
    assert "No text received" in response.data.decode()

    response = client.post("/tokenize", json={"text": "At eight o'clock on Thursday morning. Arthur didn't feel very good."})
    expected_list = ["At", "eight", "o'clock", "on", "Thursday", "morning", ".", "Arthur", "did", "n't", "feel", "very", "good", "."]
    r_data = response.json
    assert response.status_code == 200
    assert expected_list == r_data["response"]


def test_post_tag(client: FlaskClient) -> None:
    response = client.post("/post_tag", data={"text": "At eight o'clock on Thursday morning. Arthur didn't feel very good."})
    assert response.status_code == 415
    assert "Content-Type must be application/json" in response.data.decode()

    response = client.post("/post_tag", json={"wrong_field": "At eight o'clock on Thursday morning. Arthur didn't feel very good."})
    assert response.status_code == 400
    assert "No text received" in response.data.decode()

    response = client.post("/post_tag", json={"text": "At eight o'clock on Thursday morning. Arthur didn't feel very good."})
    expected_list = [
        ["At", "IN"], ["eight", "CD"], ["o'clock", "NN"], ["on", "IN"], ["Thursday", "NNP"], ["morning", "NN"], [".", "."], ["Arthur", "NNP"], ["did", "VBD"], ["n't", "RB"], ["feel", "VB"], ["very", "RB"], ["good", "JJ"], [".", "."]
    ]
    r_data = response.json
    assert response.status_code == 200
    assert expected_list == r_data["response"]


def test_ner(client: FlaskClient) -> None:
    response = client.post("/ner", data={"text": "At eight o'clock on Thursday morning. Arthur didn't feel very good."})
    assert response.status_code == 415
    assert "Content-Type must be application/json" in response.data.decode()

    response = client.post("/ner", json={"wrong_field": "At eight o'clock on Thursday morning. Arthur didn't feel very good."})
    assert response.status_code == 400
    assert "No text received" in response.data.decode()

    response = client.post("/ner", json={"text": "At eight o'clock on Thursday morning. Arthur didn't feel very good."})
    expected_list = [
        ["Arthur", "PERSON"]
    ]
    r_data = response.json
    assert response.status_code == 200
    assert expected_list == r_data["response"]
