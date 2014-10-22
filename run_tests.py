#!/usr/bin/env python2.7

import sys
import unittest
from tests.auth_page_tests import AuthPageTests
from tests.create_page_tests import CreatePageTests


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(AuthPageTests),
        unittest.makeSuite(CreatePageTests),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
