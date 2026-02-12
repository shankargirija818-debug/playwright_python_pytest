from playwright.sync_api import Page, expect, Playwright
def test_handle_js_alerts(playwright: Playwright):
    browser=playwright.chromium.launch(headless=False)
    browser_context=browser.new_context(http_credentials={"username": "admin", "password": "admin"})
    page=browser_context.new_page()
    page.goto("https://the-internet.herokuapp.com/basic_auth")
    expect(page.locator("div.example p")).to_have_text("Congratulations! You must have the proper credentials.")

