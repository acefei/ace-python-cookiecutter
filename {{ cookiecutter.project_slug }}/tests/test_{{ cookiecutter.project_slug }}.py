#!/usr/bin/env python
import unittest
from unittest import mock
from {{ cookiecutter.project_slug  }} import {{ cookiecutter.project_slug  }}


class Test{{ cookiecutter.project_slug }}(unittest.TestCase):
    # About mock, there are two things need to clarify:
    # 1. Mock an attribute where it is used, not where it came from.
    # 2. mock.patch format is '<path>.<module>.<attribute>'
    #    instead of '<module>.<attribute>' even 'from path import module'
    @mock.patch('{{ cookiecutter.project_slug }}.{{ cookiecutter.project_slug }}.subprocess')
    def test_call(self, mock_subprocess):
        {{ cookiecutter.project_slug   }}.call("test call")
        mock_subprocess.call.assert_called_with("test call")
