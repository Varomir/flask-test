def test_api_funny(flask_test_client):
    responce = flask_test_client.get('api/funny')

    assert responce.status_code == 200
    assert responce.mimetype == 'application/json'
    assert len(responce.data) > 20
