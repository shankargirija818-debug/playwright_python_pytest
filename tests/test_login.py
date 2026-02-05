from playwright.sync_api import Page, expect

class TestFlipkartLogin:
    """
    A simplified, single-method class for Flipkart OTP Login.
    All logic is contained within the test method itself.
    """

    def test_flipkart_login_flow(self, page: Page):
        # 1. Configuration & Navigation
        mobile_number = "8310807037"  # Replace with your number
        page.goto("https://www.flipkart.com/")
        # page.locator("xpath=//span[text()='✕']").click()  # Close any initial popups if they appear

        # 2. Open Login Modal
        # We use a try-except because Flipkart often shows the login popup automatically
        try:
            header_login = page.locator('span:has-text("Login")').first
    
            if header_login.is_visible():
                header_login.hover()  # Hover to ensure any hover effects are triggered
                header_login.click()

        except Exception:
            print("Login modal already present or link not found.")
        # 3. Enter Credentials & Request OTP
        # We use 'expect' here to ensure the field is ready before typing
        # Replace your current phone_input line with this:
        # 3. Enter Credentials & Request OTP
        # We search for the input field specifically using its class or placeholder
        #phone_input = page.locator("xpath=//span[text()='Enter Email/Mobile number']/ancestor::div[@id='container']")
        # Matches even if the casing changes (e.g., "ENTER EMAIL")
        expect(page.locator("form").filter(has_text="Enter Email/Mobile numberBy").get_by_role("textbox")).to_be_visible()
        page.locator("form").filter(has_text="Enter Email/Mobile numberBy").get_by_role("textbox").click()
        page.locator("form").filter(has_text="Enter Email/Mobile numberBy").get_by_role("textbox").fill(mobile_number)
        # phone_input = page.get_by_text("Enter Email/Mobile number", exact=False).click()
        # phone_input.fill(mobile_number)

        # If the class above fails, try this alternative:
        # phone_input = page.get_by_placeholder("Enter Email/Mobile number")

        #expect(phone_input).to_be_visible(timeout=10000)
        page.get_by_role("button", name="Request OTP").click()

        # 4. The 'Human' Gap
        # Execution stops here. You type the OTP in the browser.
        # You MUST click 'Resume' in the Playwright Inspector to proceed.
        print(">>> ACTION REQUIRED: Enter OTP in the browser and click 'Resume' in Inspector.")
        page.pause()

        # 5. Post-Login Validation
        # We wait up to 30 seconds for the 'My Account' text to appear after OTP submission
        grocery_link = page.get_by_role("link", name="Grocery")
        #my_account_label = page.get_by_text("My Account")
        expect(grocery_link).to_be_visible(timeout=30000)
        
        print("Successfully logged into Flipkart!")

        #Search Box Interaction
        search_box = page.get_by_role("textbox", name="Search for Products, Brands")
        search_box.click()
        search_box.fill("i phone 15")
        search_box.press("Enter")
        expect(page.get_by_role("heading", name="iPhone 15")).to_be_visible(timeout=30000)
        print("Search results for 'i phone 15' are visible.")
        page.get_by_role("link", name="Apple iPhone 15 (Black, 128 GB)", exact=True).click()
        page.locator("xpath=//*[local-name()='svg' and contains(@class, 'kV7kR_')]/ancestor::button").click()
        page.locator("xpath=//*[local-name()='svg' and contains(@class, 'v_7pKG')]/ancestor::a").click()
        page.locator("xpath=//span[text()='Place Order']/ancestor::button").click()
        page.locator("xpath=//span[text()='Continue']/ancestor::button").click()
        total_payable = page.locator("xpath=//div[text()='Total Payable']").inner_text()
        print(f"Total Payable: {total_payable}")
        #page.locator("xpath=//button[text()='Accept & Continue']/ancestor::div[@id='container']").click()


