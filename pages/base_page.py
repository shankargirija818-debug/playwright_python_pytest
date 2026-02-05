import os
from datetime import datetime
from playwright.sync_api import Page, Response, expect
from utils.ui_actions import UIActions

class BasePage:
    """
    Parent class for all Page Objects.
    Provides shared utilities and initializes the action driver.
    """

    def __init__(self, page: Page):
        self.page = page
        # Initialize the Action Driver utility
        self.actions = UIActions(page)

    def navigate_to(self, url: str) -> Response:
        """Navigates to the given URL with a basic load check."""
        return self.page.goto(url, wait_until="domcontentloaded")
    
    def wait_for_url(self, url_pattern):
        self.page.wait_for_url(url_pattern)
        

    def wait_for_page_load(self):
        """Waits for the network to be idle."""
        self.page.wait_for_load_state("networkidle")

    def handle_popup(self, trigger_task):
        """
        Handles actions that open a new tab/window.
        Usage: new_tab = base_page.handle_popup(lambda: page.click('selector'))
        """
        with self.page.context.expect_page() as new_page_info:
            trigger_task()
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        return new_page

    def get_element_screenshot(self, selector: str, element_name: str):
        """Captures a screenshot of a specific element on failure."""
        folder = "screenshots/elements"
        if not os.path.exists(folder):
            os.makedirs(folder)
        
        timestamp = datetime.now().strftime("%H%M%S")
        path = f"{folder}/{element_name}_{timestamp}.png"
        self.page.locator(selector).screenshot(path=path)
        return path

    def switch_to_frame(self, frame_selector: str):
        """Returns a frame locator for interacting with iFrames."""
        return self.page.frame_locator(frame_selector)

    def accept_alert(self, prompt_text: str = None):
        """Configures the page to automatically accept the next dialog."""
        self.actions.handle_dialog(action="accept", prompt_text=prompt_text)

    def dismiss_alert(self):
        """Configures the page to automatically dismiss the next dialog."""
        self.actions.handle_dialog(action="dismiss")