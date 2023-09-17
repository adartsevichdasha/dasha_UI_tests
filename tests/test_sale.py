def test_sale_page(sale_page):
    sale_page.open()
    sale_page.cart_button_is_on_page()
    sale_page.button_name('Shop Women’s Deals')
    sale_page.search_item('shorts')
