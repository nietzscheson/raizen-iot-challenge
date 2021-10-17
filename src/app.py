import falcon
import falcon_sqla

from images import Resource
from database import init_session, engine

init_session()

manager = falcon_sqla.Manager(engine)

app = application = falcon.App(middleware=[manager.middleware])

images = Resource()
app.add_route("/images", images)