from playwright.sync_api import Page, expect

class UIActions:
    def __init__(self, page: Page):
        self.page = page

    # Text Input & Keys
    def fill(self, selector, text):
        self.page.locator(selector).fill(text)

    def press_key(self, selector, key):
        self.page.locator(selector).press(key)

    # Clicks & Mouse
    def click(self, selector):
        self.page.click(selector)

    def double_click(self, selector):
        self.page.dblclick(selector)

    # Selection & State
    def select_option(self, selector, value):
        self.page.select_option(selector, value)

    def check_checkbox(self, selector):
        self.page.locator(selector).check()

    # Advanced Actions
    def drag_and_drop(self, source, target):
        self.page.drag_and_drop(source, target)

    def scroll_to(self, selector):
        self.page.locator(selector).scroll_into_view_if_needed()

    # Dialogs (Alert, Confirm, Prompt)
    def handle_dialog(self, action="accept", prompt_text=None):
        def on_dialog(dialog):
            if action == "accept":
                dialog.accept(prompt_text)
            else:
                dialog.dismiss()
        self.page.on("dialog", on_dialog)

    # Frame Handling
    def get_frame_locator(self, frame_selector):
        return self.page.frame_locator(frame_selector)