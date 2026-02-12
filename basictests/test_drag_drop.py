
from playwright.sync_api import Page, expect

def test_drag_drop(page: Page):
    page.goto("https://the-internet.herokuapp.com/drag_and_drop")
    page.locator("#column-a").drag_to(page.locator("#column-b"))
    expect(page.locator("#column-a header")).to_have_text("B")