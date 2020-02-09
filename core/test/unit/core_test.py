import unittest

from core import facade, setuptools


class FacadeTest(unittest.TestCase):
    tools = setuptools.SetUpTools(__name__)

    def test_put_get(self):
        with self.subTest("base_configuration"):
            _id = facade.get("_id")
            self.assertEqual(_id, "a3853ec5adce446095e9038a29cd5604")

        with self.subTest("get_empty_key"):
            key = self.tools.unique_key()
            value = facade.get(key)
            self.assertIsNone(value)

    def test_get_int(self):
        pass

    def test_function_annotation(self):
        pass

    def test_get_database_url(self):
        pass
