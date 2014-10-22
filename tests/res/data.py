import os


class Data:
    USERNAME = 'tech-testing-ha2-31@bk.ru'
    PASSWORD = os.environ['TTHA2PASSWORD']
    DOMAIN = '@bk.ru'

    BROWSER = os.environ.get('TTHA2BROWSER', 'CHROME')

    TITLE = u'title'
    TEXT = u'text'
    URL = u'http://www.odnoklassniki.ru/event/1'
    IMAGE = os.getcwd() + '/tests/res/100_100.png'
    PROMO_IMAGE = os.getcwd() + '/tests/res/1080_607.jpg'

    def __init__(self):
        pass
