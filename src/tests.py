from falcon import testing
from app import application


class MyAppTestCase(testing.TestCase):
    def setUp(self):
        super(MyAppTestCase, self).setUp()
        self.app = application


class TestMyApp(MyAppTestCase):
    def test_images(self):
        doc = """{"images": [{"href": "/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png"}]}"""

        result = self.simulate_get("/images")
        self.assertEqual(result.text, doc)
