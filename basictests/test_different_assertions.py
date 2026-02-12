# expect(page).to_have_title(re.compile(r".*checkout"))
# expect(page).to_have_url(re.compile(".*checkout"))
# expect(page).not_to_have_url(url_or_reg_exp)

import time
from playwright.sync_api import Page, expect
def test_different_assertions(page: Page):
    page.goto("https://the-internet.herokuapp.com/dynamic_loading")
    time.sleep(5)
    page.reload()
    time.sleep(5)
    expect(page).not_to_have_url("https://the-internet.herokuapp.com/dynamic_loading")

    