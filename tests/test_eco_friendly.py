def test_eco_friendly_page(eco_friendly_page):
    eco_friendly_page.open()
    eco_friendly_page.page_title('Eco Friendly')
    eco_friendly_page.add_item_to_cart()
    eco_friendly_page.clear_filter()
