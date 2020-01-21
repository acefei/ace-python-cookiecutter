#!/usr/bin/env python
import logging
import unittest
from unittest import mock
from {{ cookiecutter.project_slug  }} import {{ cookiecutter.project_slug  }}


class Test{{ cookiecutter.project_slug }}(unittest.TestCase):
    # About mock, there are two things need to clarify:
    # 1. Mock an attribute where it is used, not where it came from.
    # 2. mock.patch format is '<path>.<module>.<attribute>'
    #    instead of '<module>.<attribute>' even 'from path import module'
    @mock.patch("{{ cookiecutter.project_slug }}.{{ cookiecutter.project_slug }}.subprocess")
    def test_call(self, mock_subprocess):
        logging.info(f"Start: {self._testMethodName}")
        {{ cookiecutter.project_slug   }}.call("test call")
        mock_subprocess.call.assert_called_with("test call")
        logging.info(f"End: {self._testMethodName}")

if __name__ == '__main__':
    logging.basicConfig(
        format=('%(asctime)s %(name)s: [%(filename)s:%(lineno)s - %(funcName)s()] [%(levelname)s] %(message)s'),
        level=logging.DEBUG)

    unittest.main(verbosity=2)
