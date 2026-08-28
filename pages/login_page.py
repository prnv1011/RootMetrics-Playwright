from config.settings import USERNAME, PASSWORD

class LoginPage():
    def __init__(self, page):
        self.page=page
        self.username_textbox = page.locator('input#input-email')
        self.password_textbox = page.locator('input#input-password')
        self.rememberme_checkbox = page.locator("input[type='checkbox']")
        self.reset_password_button = page.locator("a.pull-right")
        self.submit_button = page.locator("button[type='submit']")


    def enter_username(self):
        self.username_textbox.fill(USERNAME)

    def enter_password(self):
        self.password_textbox.fill(PASSWORD)

    def click_remember_me_cb(self):
        self.rememberme_checkbox.click()

    def click_reset_password(self):
        self.reset_password_button.click()

    def click_submit(self):
        self.submit_button.click()