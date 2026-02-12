import re
from playwright.sync_api import Page, expect

def select_multiple_subjects(page: Page, subjects: list):
    """
    Generic method to select multiple items from the DemoQA subjects autosuggestion.
    """
    subject_input = page.locator("#subjectsInput")
    
    for subject in subjects:
        # 1. Type the first letter of the subject to trigger the menu
        subject_input.fill(subject[0])
        
        # 2. Locate the specific suggestion in the menu list
        # We use a locator that targets the menu list items specifically
        suggestion = page.locator(".subjects-auto-complete__menu-list div").get_by_text(subject, exact=True)
        
        # 3. Wait for it to be visible and click
        suggestion.wait_for(state="visible")
        suggestion.click()
        
        # 4. Verify it was added to the selection container
        # This ensures the UI is ready for the next iteration
        expect(page.locator(".subjects-auto-complete__multi-value__label").get_by_text(subject)).to_be_visible()

# --- Implementation in your Test ---

def test_autosuggestion(page: Page):
    page.goto("https://demoqa.com/automation-practice-form")
    
    # Define the list of items you want to select
    items_to_select = ["English", "Maths"]
    
    # Call the generic method
    select_multiple_subjects(page, items_to_select)
    
    # Final Verification: Check all items are displayed
    for item in items_to_select:
        expect(page.locator(f"//div[text()='{item}']")).to_have_text(item)
    
    print(f"Successfully selected: {items_to_select}")