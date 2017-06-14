import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):    # Perfom unit tests on views
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from .views import my_view
        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info['project'], 'wikiapp')


class FunctionalTests(unittest.TestCase):   # Perform unit tests on wikiapp
    def setUp(self):
        from wikiapp import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_root(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(b'Pyramid' in res.body)
