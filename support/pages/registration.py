#-* coding: utf-8

from base_page import BasePage
import re

class Registration(BasePage):
    def __init__(self, context):
        super(Registration, self).__init__(context)
        self.url = 'https://testingstage.com/tickets/?ticket=1'

    @property
    def price(self):
        ui.Link(context, 'Купить билет').click()
        locator = '//div[@class="price"]'
        price = self.browser.find_element_by_xpath(locator).text
        price = re.findall('\d', price)[0]
        return price


