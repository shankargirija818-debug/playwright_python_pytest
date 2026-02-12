import re
from playwright.sync_api import Page, expect

def test_handle_submenu(page: Page):
    page.goto("https://www.globalsqa.com/")
    # Hover on the "Mouse Hover" element to reveal the submenu
    freebook_submenu=page.get_by_role("link", name="Free Ebooks")
    freebook_submenu.hover()
    expect(page.locator("#menu-item-7132")).to_contain_text("Free Machine Learning Ebooks")
      # Wait for the submenu to appear
    items_text = freebook_submenu.all_inner_texts()
    print(f"Found {len(items_text)} items:")
    for text in items_text:
        print(f"- {text}")
    print(freebook_submenu.count())

def test_select_all_elements_froms_submenu_after_hover(page: Page):
    page.goto("https://www.globalsqa.com/")
    # Hover on the "Mouse Hover" element to reveal the submenu
    freebook_dropDown=page.get_by_role("link", name="Free Ebooks")
    freebook_dropDown.hover()
    page.wait_for_timeout(2000)
    # page.pause()
      # Wait for the submenu to appear (adjust the timeout as needed)
    items = page.locator("xpath=//div[@id='menu']//ul[@class='sub-menu']").all_inner_texts()
    
    print(f"Found {len(items)} items in submenu:")
    for item in items:
        print(f"- {item}")

    #//a[contains(. , 'Machine Learning')]")            

    #expect(page.locator("#menu-item-7132")).to_contain_text("Free Machine Learning Ebooks")

    
    
    
