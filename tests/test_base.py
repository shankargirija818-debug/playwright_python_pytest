import pytest
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from utils.logger import Logger

@pytest.mark.usefixtures("page")
class BaseTest:
    """
    Base class for all test classes.
    Automatically ensures that every test class has access to 
    Playwright's 'page' fixture and initializes Page Objects.
    """

    log = Logger.get_logger("BaseTest")

    @pytest.fixture(autouse=True)
    def setup_pages(self, page):
        """
        Initializes page objects before every test method.
        'autouse=True' ensures this runs without being explicitly called.
        """
        self.page = page
        self.login_page = LoginPage(page)
        self.cart_page = CartPage(page)
        self.log.info("Page objects initialized for the test case.")