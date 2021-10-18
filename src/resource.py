import json

import falcon
from sqlalchemy import func
from model import Sensor


class SensorResourceQuery:
    @staticmethod
    def query(session, field):
        subquery = session.query(func.max(field)).scalar_subquery()
        query = session.query(Sensor).filter(field == subquery).all()

        return query


class HighestCO2Resource:
    def on_get(self, req, resp):
        session = req.context["session"]

        query = SensorResourceQuery.query(session=session, field=Sensor.CO2)

        data = {}
        for row in query:
            data[row.id] = {"time": str(row.time), "CO2": row.CO2}

        resp.text = json.dumps({"data": data, "count": len(query)}, ensure_ascii=False)
        resp.status = falcon.HTTP_200


class HottestTemperatureResource:
    def on_get(self, req, resp):
        session = req.context["session"]

        query = SensorResourceQuery.query(session=session, field=Sensor.temp)

        data = {}
        for row in query:
            data[row.id] = {"time": str(row.time), "temperature": row.temp}

        resp.text = json.dumps({"data": data, "count": len(query)}, ensure_ascii=False)
        resp.status = falcon.HTTP_200


class HighestHumidityResource:
    def on_get(self, req, resp):
        session = req.context["session"]

        query = SensorResourceQuery.query(session=session, field=Sensor.humidity)

        data = {}
        for row in query:
            data[row.id] = {"time": str(row.time), "humidity": row.humidity}

        resp.text = json.dumps({"data": data, "count": len(query)}, ensure_ascii=False)
        resp.status = falcon.HTTP_200
