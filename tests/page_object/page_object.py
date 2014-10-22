import urlparse

from tests.page_object.component import *


class Page(object):
    BASE_URL = 'https://target.mail.ru'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)


class AuthPage(Page):
    PATH = '/login'

    @property
    def form(self):
        return AuthForm(self.driver)


class CreatePage(Page):
    PATH = '/ads/create'

    @property
    def top_menu(self):
        return TopMenu(self.driver)

    @property
    def base_setting(self):
        return BaseSetting(self.driver)

    @property
    def banner_form(self):
        return BannerForm(self.driver)

    @property
    def main_button(self):
        return MainButton(self.driver)

    @property
    def income_group(self):
        return IncomeGroup(self.driver)

    @property
    def interests(self):
        return Interests(self.driver)


class CompaignsPage(Page):
    PATH = '/ads/campaigns'

    @property
    def link_edit(self):
        return LinkEdit(self.driver)

    @property
    def link_delete(self):
        return LinkDelete(self.driver)


class EditPage(Page):
    @property
    def banner_preview(self):
        return BannerPreview(self.driver)

    @property
    def income_group(self):
        return IncomeGroup(self.driver)

    @property
    def interests(self):
        return Interests(self.driver)