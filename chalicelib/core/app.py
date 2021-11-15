from chalicelib.config import settings
from requests import get, post


class PutIo:
    def __init__(self):
        self.params = {'oauth_token': settings.OAUTH_TOKEN}

    def download(self, doc_id):
        r = get("https://api.put.io/v2/files/{id}/url".format(id=doc_id), params=self.params)
        return r.json()

    def upload(self, filename, data, parent_id=0):
        files = {'file': (filename, data)}
        r = post("https://upload.put.io/v2/files/upload",
                 params=self.params,
                 data={'parent_id': parent_id},
                 files=files)

        return r.json()

    def list(self):
        r = get("https://api.put.io/v2/files/list", params=self.params)
        return r.json()
