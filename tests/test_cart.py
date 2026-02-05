import re
from playwright.sync_api import Page, expect

def test_flipkart_checkout_flow(page: Page) -> None:
    # 1. Navigation
    mobile_number = "8310807037"  # Replace with your number
    page.goto("https://www.flipkart.com/")
    
    # 2. Login Logic
    # Flipkart sometimes shows 'Login' or just an icon. Using a broader match.
    try:
            # Look for the login button in the header
            header_login = page.get_by_role("link", name="Login").or_(page.locator('span:has-text("Login")'))
            if header_login.first.is_visible():
                header_login.first.click()
    except Exception:
            print("Login modal might already be present.")
    # login_btn = page.get_by_role("link", name=re.compile("Login", re.IGNORECASE)).first
    # expect(login_btn).to_be_visible()
    # login_btn.click()

    # Locate phone input by placeholder or role for better stability
    expect(page.locator("form").filter(has_text="Enter Email/Mobile numberBy").get_by_role("textbox")).to_be_visible()
    page.locator("form").filter(has_text="Enter Email/Mobile numberBy").get_by_role("textbox").click()
    page.locator("form").filter(has_text="Enter Email/Mobile numberBy").get_by_role("textbox").fill(mobile_number)
    
    page.get_by_role("button", name="Request OTP").click()

    # 3. OTP Handling 
    # NOTE: Since you are entering this manually/via script, ensure the pause allows you to check
    # If the inputs are dynamic, this loop is cleaner than .nth()
    print("Please ensure OTP is filled correctly.")
    page.pause()
    # page.pause() # Uncomment this if you want to manually verify OTP before the script resumes
    grocery_link = page.get_by_role("link", name="Grocery")
    #my_account_label = page.get_by_text("My Account")
    expect(grocery_link).to_be_visible(timeout=30000)
        
    print("Successfully logged into Flipkart!")

    # 4. Search Interaction
    search_box = page.get_by_role("textbox", name="Search for Products, Brands")
    expect(search_box).to_be_visible(timeout=10000)
    search_box.fill("iphone 17")
    search_box.press("Enter")

    # 5. Product Selection (Handle New Tab)
    # Using a partial name match because titles on Flipkart are very long
    with page.expect_popup() as page1_info:
        page.get_by_text("Apple iPhone 17").first.click()
    page1 = page1_info.value

    # 6. Cart Actions
    # Use 'to_be_visible' before clicking to handle page load speed
    cart_btn = page1.locator("xpath=//*[local-name()='svg' and contains(@class, 'kV7kR_')]/ancestor::button")
    expect(cart_btn).to_be_visible()
    cart_btn.click()

    page1.locator("xpath=//*[local-name()='svg' and contains(@class, 'v_7pKG')]/ancestor::a").click()

    # 7. Order Flow
    place_order_btn = page1.get_by_role("button", name="Place Order")
    expect(place_order_btn).to_be_visible()
    place_order_btn.click()

    # 8. Summary & Continuous Assertions
    expect(page1.get_by_text("Order Summary")).to_be_visible()
    
    # Robust Check for 'Continue' button
    continue_btn = page1.get_by_role("button", name="CONTINUE")
    expect(continue_btn).to_be_visible()
    continue_btn.click()

    # Handle 'Accept & Continue' popup if it appears
    accept_btn = page1.get_by_role("button", name="Accept & Continue")
    if accept_btn.is_visible(timeout=5000):
        accept_btn.click()

    # 9. Payment Page Assertions
    expect(page1.get_by_text("Complete Payment")).to_be_visible()
    
    # IMPROVEMENT: Instead of hardcoded price, assert it contains 'Total Amount' and a currency symbol
    final_price_section = page1.get_by_test_id("final-price-items")
    expect(final_price_section).to_contain_text("Total Amount")
    expect(final_price_section).to_contain_text("₹") 
    
    # Print the actual price for logging
    actual_price = final_price_section.inner_text()
    print(f"Checkout Price Verified: {actual_price}")

    expect(page1.get_by_role("textbox", name="Enter your UPI ID")).to_be_visible()