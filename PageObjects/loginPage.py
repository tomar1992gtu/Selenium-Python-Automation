from Config.Locators import Locators

class LoginPage() :

    def __init__(self, driver):
        self.driver = driver

        self.username = driver.find_element_by_id(Locators.username_textbox_id)
        self.password = driver.find_element_by_id(Locators.password_textbox_id)
        self.login_button = driver.find_element_by_id(Locators.login_button_id)

    def enter_username(self,username):
        self.username.clear()
        self.username.send_keys(username)

    def enter_password(self,password):
        self.password.clear()
        self.password.send_keys(password)

    def click_login(self):
        self.login_button.click()
