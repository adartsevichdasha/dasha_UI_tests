def test_create_account(create_account_page):
    create_account_page.open()
    create_account_page.required_fields_error('This is a required field.')
    create_account_page.password_confirmation_error('Please enter the same value again.')
    create_account_page.successful_account_creation('Thank you for registering with Main Website Store.')
