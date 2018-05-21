import unittest

import {{cookiecutter.package_name}}_flask


class {{cookiecutter.package_name.capitalize()}}FlaskViewTestCase(unittest.TestCase):

    def setUp(self):
        self.app = {{cookiecutter.package_name}}_flask.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to {{cookiecutter.application_name}}', rv.data.decode())


class {{cookiecutter.package_name.capitalize()}}FlaskApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = {{cookiecutter.package_name}}_flask.app.test_client()

    def test_index(self):
        rv = self.app.get('/sample')
        self.assertIn('Hi cookiecutter, Welcome to {{cookiecutter.application_name}}', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
