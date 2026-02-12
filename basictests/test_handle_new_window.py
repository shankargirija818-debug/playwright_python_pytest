from playwright.sync_api import Page, expect, BrowserContext

# 1. Rename function to start with 'test_'
# 2. Use 'context' fixture provided by the pytest-playwright plugin
def test_handle_new_window(context: BrowserContext, page: Page):
    # 'page' is already open and ready to use
    page.goto("https://the-internet.herokuapp.com/windows")
    
    # This captures the new tab triggered by target="_blank"
    with context.expect_page() as new_page_info:
        page.get_by_text("Click Here").click()
    
    new_page = new_page_info.value
    
    # Assertions
    expect(new_page.locator("h3")).to_have_text("New Window")
    print(f"\nNew page title: {new_page.title()}")

    page.bring_to_front()  # Bring the original page back to the front
    page.wait_for_timeout(1000)  # Optional: Wait for a moment to see the original page
    print(f"\nOriginal page title: {page.title()}")
    
    # No need to manually close the browser; pytest handles it!
    new_page.close()

