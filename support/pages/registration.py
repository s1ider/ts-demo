#-* coding: utf-8

from base_page import BasePage
import re

class Registration(BasePage):
    def __init__(self, context):
        super(Registration, self).__init__(context)
        self.url = 'https://testingstage.com/tickets/?ticket=1'

    @property
    def price(self):
        locator = '//div[@class="price"]'
        price = self.browser.find_element_by_xpath(locator).text
        price = int(re.findall('\d', price)[0])
        return price


