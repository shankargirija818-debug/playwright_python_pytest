from playwright.sync_api import Page, expect

def test_handle_multiple_windows(page: Page):
    # 1. Navigate to the main page
    page.goto("https://the-internet.herokuapp.com/windows")
    
    # Store all our new pages in a list to keep track of them
    new_pages = []

    # 2. Open the first popup
    with page.expect_popup() as popup_info:
        page.get_by_text("Click Here").click()
    new_pages.append(popup_info.value)

    # 3. Go back to front page and click TWICE more
    for i in range(2):
        page.bring_to_front() # Ensure we are focused on the main page
        
        with page.expect_popup() as popup_info:
            page.get_by_text("Click Here").click()
        
        new_pages.append(popup_info.value)

    # 4. Capture titles and interact with all popups
    print(f"\nTotal tabs opened: {len(new_pages)}")
    
    for index, p in enumerate(new_pages, start=1):
        # We can switch focus to each tab to do work
        p.bring_to_front()
        expect(p.locator("h3")).to_have_text("New Window")
        print(f"Tab {index} Title: {p.title()}")
        p.close() # Clean up as we go

    # 5. Move back to front page at the end
    page.bring_to_front()
    print(f"Back to original page: {page.title()}")
    
    # Final assertion to make sure we are where we think we are
    expect(page.get_by_role("heading")).to_have_text("Opening a new window")