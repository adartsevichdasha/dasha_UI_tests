from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


title_of_page = (By.XPATH, '//*[@data-ui-id="page-title-wrapper"]')
product = (By.XPATH, '//*[@class="product-item-link"]')
size = (By.XPATH, '//*[@id="option-label-size-143-item-171"]')
color = (By.XPATH, '//*[@id="option-label-color-93-item-58"]')
add_button = (By.XPATH, '//*[@title="Add to Cart"]')
show_button = (By.XPATH, '//*[@class="action showcart"]')
added_product = (By.XPATH, '//*[@class="product-item-name"]')
message = (By.XPATH, '//*[@data-ui-id="message-success"]')
list_of_all_items = (By.XPATH, '//*[@data-container="product-grid"]')
filter_tab = (By.XPATH, '//*[@class="filter-options-title"]')
filter_options = (By.XPATH, '//*[@class="item"]')
clear_button = (By.XPATH, '//*[@class="action clear filter-clear"]')
list_of_returned_items = (By.XPATH, '//*[@data-container="product-grid"]')


class EcoFriendlyPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    def page_title(self, title):
        page_title = self.find(title_of_page)
        assert page_title.text == title

    def add_item_to_cart(self):
        self.driver.maximize_window()
        item = self.find_all(product)[1]
        self.find_all(size)[1].click()
        self.find(color).click()
        self.driver.set_window_size(400, 700)
        self.find_all(add_button)[1].click()
        self.driver.maximize_window()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                              '//*[@data-ui-id="message-success"]')))
        self.find(show_button).click()
        added_item = self.find(added_product)
        displayed_success_message = self.find(message)
        assert displayed_success_message is not None
        assert added_item.text == item.text

    def clear_filter(self):
        self.driver.maximize_window()
        displayed_items = self.find_all(list_of_all_items)
        self.find_all(filter_tab)[0].click()
        self.find_all(filter_options)[6].click()
        self.find(clear_button).click()
        returned_items = self.find_all(list_of_returned_items)
        assert len(displayed_items) == len(returned_items)
