import falcon
import falcon_sqla

from resource import (
    HighestCO2Resource,
    HottestTemperatureResource,
    HighestHumidityResource,
)
from database import init_session, engine

init_session()

manager = falcon_sqla.Manager(engine)

app = application = falcon.App(middleware=[manager.middleware])

app.add_route("/highest-co2", HighestCO2Resource())
app.add_route("/hottest-temperature", HottestTemperatureResource())
app.add_route("/highest-humidity", HighestHumidityResource())
