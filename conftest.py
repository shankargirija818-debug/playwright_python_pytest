import pytest
import os
from datetime import datetime
from playwright.sync_api import Page

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    page.set_viewport_size({"width": 1536, "height": 695})
    yield page
    # Notice: We don't strictly need page.close() here as context closing handles it,
    # but keeping it is fine as long as the hook runs first.

@pytest.fixture
def logged_in_page(page, base_url):
    """
    Now generic! It uses whatever URL is passed 
    via CLI or pytest.ini.
    """
    if base_url:
        page.goto(base_url)
    else:
        # Fallback if no URL is provided
        page.goto("https://www.flipkart.com") 
    yield page

@pytest.fixture(scope="function")
def browser_context_args(browser_context_args):
    state_path = "flipkart_state.json"
    if os.path.exists(state_path):
        return {
            **browser_context_args,
            "storage_state": state_path
        }
    return browser_context_args

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    # Only trigger on test failure during the actual call
    if report.when == "call" and report.failed:
        # Get the page object from fixtures
        page = item.funcargs.get('page') or item.funcargs.get('logged_in_page')
        
        if page:
            try:
                # 1. Create directory if missing
                if not os.path.exists("screenshots"):
                    os.makedirs("screenshots")
                
                # 2. Define path
                file_name = f"screenshots/fail_{item.name}_{datetime.now().strftime('%H%M%S')}.png"
                
                # 3. Final check: Is the page still responsive?
                if not page.is_closed():
                    # We avoid full_page=True to prevent font-loading timeouts
                    page.screenshot(path=file_name, timeout=5000)
                    print(f"\n[Screenshot saved]: {file_name}")
            
            except Exception as e:
                # This prevents a screenshot error from crashing the whole test suite
                print(f"\n[Warning]: Could not take screenshot: {e}")