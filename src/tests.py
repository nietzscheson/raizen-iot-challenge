from falcon import testing
from app import application
from model import Base
from database import session, engine

import sqla_yaml_fixtures


class MyAppTestCase(testing.TestCase):
    def setUp(self):
        super(MyAppTestCase, self).setUp()
        self.app = application


class TestMyApp(MyAppTestCase):
    def setUp(self):
        super(TestMyApp, self).setUp()

        fixture = """
        - Sensor:
          - time: 2015-08-01 00:00:28
            power: 0
            temp: 32
            humidity: 40
            light: 0
            CO2: 973
            dust: 27.8
          - time: 2015-08-03 17:19:37
            power: 0.572
            temp: 34
            humidity: 37
            light: 12
            CO2: 900
            dust: 13.74
          - time: 2015-08-06 10:25:47
            power: -1
            temp: 33
            humidity: 36
            light: 16
            CO2: 1362
            dust: 11.21
          - time: 2015-08-06 10:35:50
            power: -1
            temp: 33
            humidity: 36
            light: 16
            CO2: 1362
            dust: 11.21
        """
        sqla_yaml_fixtures.load(Base, session, fixture)

    def tearDown(self):
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    def test_images(self):
        doc = """{"images": [{"href": "/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png"}]}"""

        result = self.simulate_get("/images")
        self.assertEqual(result.text, doc)

    def test_highest_co2(self):
        data = """{"data": {"3": {"time": "2015-08-06 10:25:47", "CO2": 1362}, "4": {"time": "2015-08-06 10:35:50", "CO2": 1362}}, "count": 2}"""
        result = self.simulate_get("/highest-co2")
        self.assertEqual(result.text, data)

    def test_hottest_temperature(self):
        data = """{"data": {"2": {"time": "2015-08-03 17:19:37", "temperature": 34}}, "count": 1}"""
        result = self.simulate_get("/hottest-temperature")
        self.assertEqual(result.text, data)

    def test_highest_humidity(self):
        data = """{"data": {"1": {"time": "2015-08-01 00:00:28", "humidity": 40}}, "count": 1}"""
        result = self.simulate_get("/highest-humidity")
        self.assertEqual(result.text, data)
