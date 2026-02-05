import re
from pages.base_page import BasePage
from playwright.sync_api import expect

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        
        # --- Locators ---
        self.search_box = page.get_by_role("textbox", name="Search for Products, Brands")
        self.first_product = page.locator("div._1AtVbE, div.slp-item, a.V_7pKG").first
        
        # Add to Cart (Using the SVG-to-Button ancestor logic we discussed)
        self.add_to_cart_btn = page.locator("button").filter(has_text=re.compile("ADD TO CART", re.IGNORECASE))
        self.go_to_cart_btn = page.locator("button").filter(has_text=re.compile("GO TO CART", re.IGNORECASE))
        
        self.place_order_btn = page.get_by_role("button", name="Place Order")
        self.item_count_badge = page.locator("a[href*='/viewcart'] span").first
        
        # Price Locators
        self.total_payable = page.locator("div:has-text('Total Payable') + div span")
        self.order_item_name = page.locator("div._2-uG6-") # Standard Flipkart product title in cart

    # --- Actions ---
    
    def search_product(self, product_name: str):
        self.log.info(f"Searching for product: {product_name}")
        self.actions.fill(self.search_box, product_name)
        self.actions.press_key(self.search_box, "Enter")

    def select_first_product_and_switch(self):
        """Clicks product and returns the new tab/page object."""
        self.log.info("Selecting first product from results...")
        # Every product click opens a new tab on Flipkart
        new_tab = self.handle_popup(lambda: self.first_product.click())
        return CartPage(new_tab) # Return a new CartPage instance bound to the new tab

    def add_to_cart(self):
        self.log.info("Attempting to add product to cart")
        # Handle cases where item might already be in cart (GO TO CART instead of ADD TO CART)
        if self.add_to_cart_btn.is_visible(timeout=5000):
            self.actions.click(self.add_to_cart_btn)
        else:
            self.actions.click(self.go_to_cart_btn)

    def get_cart_count(self) -> int:
        if self.item_count_badge.is_visible():
            count_text = self.item_count_badge.inner_text()
            return int(count_text)
        return 0

    def get_total_payable_amount(self) -> str:
        self.log.info("Extracting total payable amount")
        # Ensure the element is visible before grabbing text
        expect(self.total_payable).to_be_visible()
        return self.total_payable.inner_text()

    def proceed_to_checkout(self):
        self.log.info("Clicking Place Order button")
        self.actions.click(self.place_order_btn)