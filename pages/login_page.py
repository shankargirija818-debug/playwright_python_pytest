from pages.base_page import BasePage
import re

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.login_trigger = page.get_by_role("link", name=re.compile("Login", re.IGNORECASE))
        self.phone_input = page.locator("form").get_by_role("textbox")
        self.otp_btn = page.get_by_role("button", name="Request OTP")

    def navigate(self):
        self.page.goto("https://www.flipkart.com")

    def login(self, mobile):
        if self.login_trigger.first.is_visible():
            self.login_trigger.first.click()
        self.phone_input.fill(mobile)
        self.otp_btn.click()