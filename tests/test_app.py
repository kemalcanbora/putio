from chalice.test import Client
from app import app
from requests import get, post

params = {'oauth_token': "UKEAFQB5AJ4JSYFCRBLT"}



def test_upload_function():
    data = open("./static/img.png", 'rb')
    r = post("https://upload.put.io/v2/files/upload", params=params, files={"file": data, "filename": "test.png"})
    print( r.json())
    assert r.json()["file"]["file_type"] == "FILE"


def test_download_function():
    with Client(app) as client:
        r = get("https://api.put.io/v2/files/{id}/url".format(id="1"), params=params)
        if "status" in list(r.json().keys()):
            assert True == True
        else:
            assert True == False


def test_list_function():
    with Client(app) as client:
        response = client.http.get('/application/list')
        assert response.json_body["status"] == "OK"
