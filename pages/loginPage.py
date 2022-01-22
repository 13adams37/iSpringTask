from .locators import LoginPageLocators
from .headerPage import HeaderPage


class LoginPage(HeaderPage):
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.auth_frame), "Отсутсвует форма логина"
