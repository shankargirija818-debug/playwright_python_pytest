import time
from playwright.sync_api import Page, expect

def test_handle_readonly(page: Page):
    page.goto("http://127.0.0.1:5500/practice.html")
    readonly_field = page.locator("input#read-only-field")
    expect(readonly_field).not_to_be_editable()

    

def test_handle_editable(page: Page):
    page.goto("http://127.0.0.1:5500/practice.html")
    editable_field = page.locator("input#edit-me")
    expect(editable_field).to_be_editable()
    editable_field.click()
    editable_field.fill("This is an editable field.")


    # Click on the HTML panel to make it editable
    