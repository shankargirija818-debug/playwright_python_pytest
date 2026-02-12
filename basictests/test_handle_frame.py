from enum import auto
import re
from playwright.sync_api import Page, expect

def test_autosuggestion(page: Page):
    page.goto("https://practice.expandtesting.com/iframe")
    frame = page.frame_locator("iframe[id^='mce_']")
    input_box=frame.locator("body#tinymce")
    input_box.click()
    input_box.fill("This is a test")
    page.wait_for_timeout(1000)