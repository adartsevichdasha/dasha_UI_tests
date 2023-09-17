from pages.base_page import BasePage
from selenium.webdriver.common.by import By


page_cart_button = (By.XPATH, '//*[@class="action showcart"]')
page_button = (By.XPATH, '//*[@class="more button"]')
page_search_result = (By.XPATH, '//*[@data-ui-id="page-title-wrapper"]')


class SalePage(BasePage):
    page_url = '/sale.html'

    def cart_button_is_on_page(self):
        cart_button = self.find(page_cart_button)
        assert cart_button is not None

    def button_name(self, button_name):
        button = self.find(page_button)
        assert button.text == button_name

    def search_item(self, item):
        page_title = f"Search results for: '{item}'"
        self.driver.find_element(By.ID, 'search').send_keys(f'{item}\n')
        search_result_title = self.find(page_search_result)
        assert page_title == search_result_title.text
