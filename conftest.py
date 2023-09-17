import pytest
from selenium import webdriver
from pages.sale_page import SalePage
from pages.create_account_page import CreateAccountPage
from pages.eco_friendly_page import EcoFriendlyPage


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    return chrome_driver


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def create_account_page(driver):
    return CreateAccountPage(driver)


@pytest.fixture()
def eco_friendly_page(driver):
    return EcoFriendlyPage(driver)
