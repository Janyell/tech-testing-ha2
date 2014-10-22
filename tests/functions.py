from tests.page_object.page_object import AuthPage, CreatePage, CompaignsPage
from tests.res.data import Data


def sign_in(driver):
    auth_page = AuthPage(driver)
    auth_page.open()

    auth_form = auth_page.form
    auth_form.set_domain(Data.DOMAIN)
    auth_form.set_login(Data.USERNAME)
    auth_form.set_password(Data.PASSWORD)
    auth_form.submit()


def set_base_setting_and_submit_banner_form(driver):
    create_page = CreatePage(driver)
    create_page.open()

    base_setting = create_page.base_setting
    base_setting.set_product_type__group_event_videochannel()
    base_setting.set_pad__mobile_odnoklassniki()

    banner_form = create_page.banner_form
    banner_form.set_image(Data.IMAGE)
    banner_form.set_promo_image(Data.PROMO_IMAGE)
    banner_form.set_title(Data.TITLE)
    banner_form.set_text(Data.TEXT)
    banner_form.set_url(Data.URL)
    banner_form.submit()

    return create_page


def go_to_edit_page(driver):
    compaigns_page = CompaignsPage(driver)
    compaigns_page.open()
    link_edit = compaigns_page.link_edit
    link_edit.click()


def delete_compaign(driver):
    compaigns_page = CompaignsPage(driver)
    compaigns_page.open()
    link_delete = compaigns_page.link_delete
    link_delete.click()
