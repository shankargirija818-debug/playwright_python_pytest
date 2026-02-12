from playwright.sync_api import Page, expect

# 1. Rename function to start with 'test_'
# 2. Use 'context' fixture provided by the pytest-playwright plugin
def test_handle_multiple_window(page: Page):
    # 'page' is already open and ready to use
    page.goto("https://the-internet.herokuapp.com/windows")
    
    # Get popup after a specific action (e.g., click)
    with page.expect_popup() as popup_info:
        page.get_by_text("Click Here").click()
    page1 = popup_info.value

    # Interact with the popup normally
    expect(page1.locator("h3")).to_have_text("New Window")
    print(page1.title())

    page.bring_to_front()
    page.wait_for_timeout(1000)  # Optional: Wait for a moment to see the original page
    print(f"\nOriginal page title: {page.title()}")