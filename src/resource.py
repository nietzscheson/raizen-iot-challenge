import json

import falcon
from sqlalchemy import func, desc, extract, and_
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

        subquery = session.query(func.max(Sensor.CO2)).scalar()
        query = session.query(Sensor).filter(Sensor.CO2 == subquery).all()

        data = {}
        for row in query:
            data[row.id] = {"time": str(row.time), "CO2": row.CO2}

        resp.text = json.dumps(
            {
                "data": {
                    "highest_co2": str(subquery),
                    "records": data,
                    "count": len(query),
                }
            },
            ensure_ascii=False,
        )
        resp.status = falcon.HTTP_200


class HottestTemperatureResource:
    def on_get(self, req, resp):
        session = req.context["session"]

        subquery = session.query(func.max(Sensor.temp)).scalar()
        query = (
            session.query(func.max(Sensor.time))
            .filter(Sensor.temp == subquery)
            .scalar()
        )

        resp.text = json.dumps(
            {"data": {"month": query.month, "day": query.day, "temperature": subquery}},
            ensure_ascii=False,
        )
        resp.status = falcon.HTTP_200


class HighestHumidityResource:
    def on_get(self, req, resp):
        session = req.context["session"]

        subquery = session.query(func.max(Sensor.humidity)).scalar()
        query = (
            session.query(func.max(Sensor.time))
            .filter(Sensor.humidity == subquery)
            .scalar()
        )

        resp.text = json.dumps(
            {
                "data": {
                    "day": query.day,
                    "hour": query.hour,
                    "highest_humidity": subquery,
                }
            },
            ensure_ascii=False,
        )
        resp.status = falcon.HTTP_200
