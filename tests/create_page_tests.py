import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from tests.functions import *
from tests.page_object.component import IncomeGroup
from tests.page_object.page_object import EditPage


class CreatePageTests(unittest.TestCase):
    def setUp(self):
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, Data.BROWSER).copy()
        )
        sign_in(self.driver)
        self.create_page = set_base_setting_and_submit_banner_form(self.driver)

    def tearDown(self):
        delete_compaign(self.driver)
        self.driver.quit()

    def test_title(self):
        main_button = self.create_page.main_button
        main_button.submit()

        go_to_edit_page(self.driver)

        edit_page = EditPage(self.driver)
        banner_preview = edit_page.banner_preview
        self.assertEqual(Data.TITLE, banner_preview.get_title())

    def test_text(self):
        main_button = self.create_page.main_button
        main_button.submit()

        go_to_edit_page(self.driver)

        edit_page = EditPage(self.driver)
        banner_preview = edit_page.banner_preview
        self.assertEqual(Data.TEXT, banner_preview.get_text())

    def test_income_group_above_and_below_average_checked(self):
        income_group = self.create_page.income_group
        income_group.click_ignored()
        income_group.set_checked(IncomeGroup.ABOVE_AVERAGE)
        income_group.set_checked(IncomeGroup.BELOW_AVERAGE)

        main_button = self.create_page.main_button
        main_button.submit()

        go_to_edit_page(self.driver)

        edit_page = EditPage(self.driver)
        income_group__edit = edit_page.income_group
        income_group__edit.click_ignored()

        self.assertEqual(True, income_group__edit.is_checked(IncomeGroup.ABOVE_AVERAGE))
        self.assertEqual(True, income_group__edit.is_checked(IncomeGroup.BELOW_AVERAGE))
        self.assertEqual(False, income_group__edit.is_checked(IncomeGroup.AVERAGE))

    def test_income_group_average_checked(self):
        income_group = self.create_page.income_group
        income_group.click_ignored()
        income_group.set_checked(IncomeGroup.AVERAGE)

        main_button = self.create_page.main_button
        main_button.submit()

        go_to_edit_page(self.driver)

        edit_page = EditPage(self.driver)
        income_group__edit = edit_page.income_group
        income_group__edit.click_ignored()

        self.assertEqual(False, income_group__edit.is_checked(IncomeGroup.ABOVE_AVERAGE))
        self.assertEqual(False, income_group__edit.is_checked(IncomeGroup.BELOW_AVERAGE))
        self.assertEqual(True, income_group__edit.is_checked(IncomeGroup.AVERAGE))

    def test_business_checked(self):
        interests = self.create_page.interests
        interests.click_ignored()
        interests.check_business()
        main_button = self.create_page.main_button
        main_button.submit()

        go_to_edit_page(self.driver)

        edit_page = EditPage(self.driver)
        interests__edit = edit_page.interests
        interests__edit.click_ignored()
        interests__edit.click_business_collapse_icon()

        self.assertEqual(True, interests__edit.is_business_checked())

    def test_business_node_checked(self):
        business_node_1 = 0
        business_node_2 = 2
        not_checked_business_node = 1

        interests = self.create_page.interests
        interests.click_ignored()
        interests.click_business_collapse_icon()
        interests.check_business_node(business_node_1)
        interests.check_business_node(business_node_2)
        main_button = self.create_page.main_button
        main_button.submit()

        go_to_edit_page(self.driver)

        edit_page = EditPage(self.driver)
        interests__edit = edit_page.interests
        interests__edit.click_ignored()
        interests__edit.click_business_collapse_icon()

        self.assertEqual(True, interests__edit.is_business_node_checked(business_node_1))
        self.assertEqual(True, interests__edit.is_business_node_checked(business_node_2))
        self.assertEqual(False, interests__edit.is_business_node_checked(not_checked_business_node))
