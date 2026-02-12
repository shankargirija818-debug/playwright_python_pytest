from playwright.sync_api import Page, expect
def test_handle_js_alerts(page: Page):
    page.goto("https://the-internet.herokuapp.com/dynamic_loading")
    page.locator("css=div.example a").filter(has_text="Example 1").click(timeout=50000)
    page.locator("button").filter(has_text="Start").click()
    page.locator("h4").filter(has_text="Hello World!").wait_for(timeout=50000)
    expect(page.locator("h4").filter(has_text="Hello World!")).to_be_visible()
