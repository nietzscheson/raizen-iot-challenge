import json

import falcon
from sqlalchemy import func
from model import Sensor


class HighestCO2Resource:
    def on_get(self, req, resp):
        session = req.context["session"]
    
        subquery = session.query(func.max(Sensor.CO2)).scalar_subquery()
        query = session.query(Sensor).filter(Sensor.CO2==subquery).all()
         
        data = {}
        for row in query:
            data[row.id] = {"time": str(row.time), "CO2": row.CO2}

        resp.text = json.dumps({"data": data, "count": len(query)}, ensure_ascii=False)
        resp.status = falcon.HTTP_200

class HottestTemperatureResource:
    def on_get(self, req, resp):
        session = req.context["session"]
    
        subquery = session.query(func.max(Sensor.temp)).scalar_subquery()
        query = session.query(Sensor).filter(Sensor.temp==subquery).all()
         
        data = {}
        for row in query:
            data[row.id] = {"time": str(row.time), "temperature": row.temp}

        resp.text = json.dumps({"data": data, "count": len(query)}, ensure_ascii=False)
        resp.status = falcon.HTTP_200
