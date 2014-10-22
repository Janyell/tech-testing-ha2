from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AuthForm(Component):
    LOGIN = '#id_Login'
    PASSWORD = '#id_Password'
    DOMAIN = '#id_Domain'
    SUBMIT = '#gogogo>input'

    def set_login(self, login):
        self.driver.find_element_by_css_selector(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_css_selector(self.PASSWORD).send_keys(pwd)

    def set_domain(self, domain):
        select = self.driver.find_element_by_css_selector(self.DOMAIN)
        Select(select).select_by_visible_text(domain)

    def submit(self):
        self.driver.find_element_by_css_selector(self.SUBMIT).click()


class TopMenu(Component):
    EMAIL = '#PH_user-email'

    def get_email(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.EMAIL).text
        )


class BaseSetting(Component):
    PRODUCT_TYPE = '#product-type-5212'
    PADS_TARGETING = '#pad-mobile_odkl_feed_abstract'

    def set_product_type__group_event_videochannel(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.PRODUCT_TYPE)
        )
        element.click()

    def set_pad__mobile_odnoklassniki(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.PADS_TARGETING)
        )
        element.click()


class BannerForm(Component):
    TITLE = 'input[data-name="title"]'
    TEXT = 'textarea[data-name="text"]'
    URL = 'input[data-name="url"]'
    IMAGE = 'input[data-name="image"]'
    PROMO_IMAGE = 'input[data-name="promo_image"]'
    SAVE_BUTTON = 'input.banner-form__save-button'

    def set_title(self, title):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.TITLE)
        )
        element.send_keys(title)

    def set_text(self, text):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.TEXT)
        )
        element.send_keys(text)

    def set_url(self, url):
        elements = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_elements_by_css_selector(self.URL)
        )
        for element in elements:
            if element.is_displayed():
                element.send_keys(url)
                return

    def set_image(self, image):
        element = WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_css_selector(self.IMAGE)
        )
        element.send_keys(image)

    def set_promo_image(self, image):
        element = WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_css_selector(self.PROMO_IMAGE)
        )
        element.send_keys(image)

    def submit(self):
        element = WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_css_selector(self.SAVE_BUTTON)
        )
        element.click()


class MainButton(Component):
    MAIN_BUTTON = '.main-button-new'

    def submit(self):
        element = WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_css_selector(self.MAIN_BUTTON)
        )
        element.click()


class LinkEdit(Component):
    LINK_EDIT = '.control__link_edit'

    def click(self):
        element = WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_css_selector(self.LINK_EDIT)
        )
        element.click()


class BannerPreview(Component):
    BANNER_PREVIEW = '.added-banner__banner-preview'
    TITLE = '.banner-preview__title'
    TEXT = '.banner-preview__text'

    def get_title(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.BANNER_PREVIEW)
        )
        return element.find_element_by_css_selector(self.TITLE).text

    def get_text(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.BANNER_PREVIEW)
        )
        return element.find_element_by_css_selector(self.TEXT).text


class IncomeGroup(Component):
    IGNORED = 'li[data-name="income_group"] .campaign-setting__value'
    COMPARED_TO_AVERAGE = 'li[data-name="income_group"] .campaign-setting__input'

    ABOVE_AVERAGE = 0
    AVERAGE = 1
    BELOW_AVERAGE = 2

    def click_ignored(self):
        element = WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_css_selector(self.IGNORED)
        )
        element.click()

    def set_checked(self, compared_to_average):
        checkbox = WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_elements_by_css_selector(self.COMPARED_TO_AVERAGE)[compared_to_average]
        )
        checkbox.click()

    def is_checked(self, compared_to_average):
        checkbox = WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_elements_by_css_selector(self.COMPARED_TO_AVERAGE)[compared_to_average]
        )
        if checkbox.is_selected():
            return True
        return False


class Interests(Component):
    IGNORED = '.campaign-setting__value[data-node-id="interests"]'
    BUSINESS_COLLAPSE_ICON = '#interests60 > .tree__node__collapse-icon'
    BUSINESS_CHECKBOX = '#interests60 > .tree__node__input'
    BUSINESS_NODES_CHECKBOXES = '#interests60 > span > ul > li > input'

    def click_ignored(self):
        element = WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_css_selector(self.IGNORED)
        )
        element.click()

    def check_business(self):
        business = WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_css_selector(self.BUSINESS_CHECKBOX)
        )
        business.click()

    def click_business_collapse_icon(self):
        business_collapse_icon = WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_css_selector(self.BUSINESS_COLLAPSE_ICON)
        )
        business_collapse_icon.click()

    def check_business_node(self, business_node_number):
        business_node = WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_elements_by_css_selector(self.BUSINESS_NODES_CHECKBOXES)[business_node_number]
        )
        business_node.click()

    def is_business_checked(self):
        checkboxes = WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_elements_by_css_selector(self.BUSINESS_NODES_CHECKBOXES)
        )
        for checkbox in checkboxes:
            if not checkbox.is_selected():
                return False
        return True

    def is_business_node_checked(self, business_node_number):
        checkbox = WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_elements_by_css_selector(self.BUSINESS_NODES_CHECKBOXES)[business_node_number]
        )
        if checkbox.is_selected():
            return True
        return False


class LinkDelete(Component):
    LINK_DELETE = '.control__preset_delete'

    def click(self):
        element = WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_css_selector(self.LINK_DELETE)
        )
        element.click()
