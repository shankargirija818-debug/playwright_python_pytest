from enum import auto
import re
from playwright.sync_api import Page, expect

def test_autosuggestion(page: Page):
    page.goto("https://demoqa.com/automation-practice-form")
    page.locator(".subjects-auto-complete__value-container").click()
    subject_input=page.locator("#subjectsInput")
    subject_input.fill("e")
    auto_suggestion_elements=page.locator("css=div.subjects-auto-complete__menu-list div")
    #auto_suggestion_elements.first.wait_for(state="visible", timeout=5000)

    auto_suggestion_elements_count=auto_suggestion_elements.count()

    print(f"Found {auto_suggestion_elements_count} auto-suggestion elements:")

    for i in range(auto_suggestion_elements_count):

        text=auto_suggestion_elements.nth(i).inner_text()

        print(f"- {text}")

        if text == "English":
            auto_suggestion_elements.nth(i).click(force=True)
            break
    

    page.wait_for_timeout(4000)
    # Verify that the selected subject is displayed in the input field
    
    expect(page.locator("//div[text()='English']")).to_have_text("English")