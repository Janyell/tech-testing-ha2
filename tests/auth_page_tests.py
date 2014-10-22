import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from tests.functions import *


class AuthPageTests(unittest.TestCase):
    def setUp(self):
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, Data.BROWSER).copy()
        )
        sign_in(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_sign_in(self):
        create_page = CreatePage(self.driver)
        create_page.open()
        email = create_page.top_menu.get_email()

        self.assertEqual(Data.USERNAME, email)