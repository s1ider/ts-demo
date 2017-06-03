from base_page import BasePage


class Registration(BasePage):
    def __init__(self, context):
        super(Registration, self).__init__(context)
        self.url = 'https://testingstage.com/tickets/?ticket=1'


