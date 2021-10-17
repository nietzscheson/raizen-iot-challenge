import json

import falcon

from model import Sensor


class Resource:
    def on_get(self, req, resp):
        doc = {"images": [{"href": "/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png"}]}
        resp.text = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200
