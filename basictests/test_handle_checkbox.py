import time
from playwright.sync_api import Page, expect

def test_handle_checkbox(page: Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    
    # Corrected filter syntax
    checkbox = page.locator("input").filter(has_text="checkbox 1")
    
    # For checkboxes, it's better to use .check() instead of .click()
    checkbox.check(timeout=50000)
    
    expect(checkbox).to_be_checked()