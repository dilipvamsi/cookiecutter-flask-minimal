import unittest

import {{cookiecutter.package_name}}


class {{cookiecutter.package_name.capitalize()}}TestCase(unittest.TestCase):

    def test_sample(self):
        self.assertIn('Hi cookiecutter, Welcome to {{cookiecutter.application_name}}', {{cookiecutter.package_name}}.sample())


if __name__ == '__main__':
    unittest.main()
