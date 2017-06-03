from base_page import BasePage


class Landing(BasePage):
    def __init__(self, context):
        super(Landing, self).__init__(context)
        self.url = 'https://testingstage.com'

    def buy_ticket(self, option):
        locator = '(//div[contains(@class, "card ticket-card")]//a)[{0}]'.format(option)
        self.browser.find_element_by_xpath(locator).click()




