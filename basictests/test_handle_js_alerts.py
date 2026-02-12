from playwright.sync_api import Page, expect
def test_handle_js_alerts(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    
    # Set up the dialog listener to click "Cancel"
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_text("Click for JS Confirm").click()

    # Pass the LOCATOR, not the text string
    result_locator = page.locator("#result")
    expect(result_locator).to_have_text("You clicked: Cancel")


def test_handle_js_prompt(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    
    # Set up the dialog listener to enter text and click "OK"
    # page.once("dialog", lambda dialog: dialog.accept("Playwright"))
    page.on("dialog", lambda dialog: print(dialog.message))
    page.once("dialog", lambda dialog: dialog.accept("Hi Playwright"))
    page.get_by_text("Click for JS Prompt").click()

    result_locator = page.locator("#result")
    expect(result_locator).to_have_text("You entered: Hi Playwright")
    