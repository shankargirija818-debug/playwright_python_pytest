from playwright.sync_api import sync_playwright

def save_auth():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) # Keep it visible
        context = browser.new_context()
        page = context.new_page()
        
        page.goto("https://www.flipkart.com")
        
        # STOP HERE: Manually log in to Flipkart in the browser window
        print("Please log in manually, then press Enter here...")
        input() 
        
        # Save the cookies and storage
        context.storage_state(path="flipkart_state.json")
        print("Auth state saved to flipkart_state.json")
        browser.close()

if __name__ == "__main__":
    save_auth()