from playwright.sync_api import Page, expect

def test_handle_windows_simple(page: Page):
    page.goto("https://the-internet.herokuapp.com/windows")

    # We do it 3 times total (1 initial + 2 more)
    for i in range(3):
        with page.expect_popup() as popup_info:
            page.get_by_text("Click Here").click()
        
        popup = popup_info.value
        
        # Interact with the popup immediately
        print(f"Tab {i+1} Title: {popup.title()}")
        expect(popup.locator("h3")).to_have_text("New Window")
        
        # Close it right away so focus naturally stays on the main page
        popup.close()

    # Verify we are back on the main page
    expect(page.get_by_role("heading")).to_have_text("Opening a new window")
    print(f"Final Page Title: {page.title()}")