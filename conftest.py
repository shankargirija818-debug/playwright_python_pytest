import pytest
import os
from datetime import datetime

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()

# --- ADD YOUR NEW FIXTURE HERE ---
@pytest.fixture
def logged_in_page(page):
    """Navigates to Flipkart before the test starts."""
    page.goto("https://www.flipkart.com")
    yield page 

@pytest.fixture(scope="function")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "storage_state": {
            "cookies": [
                {
                    "name": "SOCS",
                    "value": "CAISHAgBEhJnd3NfMjAyMzA4MzAtMF9SQzEaAmVuIAEaBgiA_LKmBg",
                    "domain": ".google.com",
                    "path": "/",
                }
            ]
        }
    }

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        # Check for 'page' or 'logged_in_page'
        page = item.funcargs.get('page') or item.funcargs.get('logged_in_page')
        if page:
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")
            file_name = f"screenshots/fail_{item.name}_{datetime.now().strftime('%H%M%S')}.png"
            page.screenshot(path=file_name, full_page=True)