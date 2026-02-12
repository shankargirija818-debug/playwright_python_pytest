from os import error
from playwright.sync_api import Page, expect


def test_verify_error_message(page: Page):
    page.goto("https://www.saucedemo.com/")
    user_namepage = page.locator("input#user-name")
    user_namepage.click()
    user_namepage.fill("standard_user")
    page.locator("input#password").fill("ssecret_sauce")
    page.locator("input#login-button").click()
    error_message = page.locator("h3[data-test='error']")
    expect(error_message).to_contain_text("Epic sadface: Username and password do not match any user in this service")


def test_attribute_value(page: Page):
    page.goto("https://www.saucedemo.com/")
    user_namepage = page.locator("input#user-name")
    expect(user_namepage).to_have_attribute("data-test", "username")