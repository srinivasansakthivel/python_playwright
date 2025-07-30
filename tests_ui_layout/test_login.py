import re
import time

import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("email", ["symon.storozhenko@gmail.com", pytest.param("fakeemail", marks=pytest.mark.xfail)])
@pytest.mark.parametrize("password", ["test123", pytest.param("pass123", marks=pytest.mark.xfail)])
def test_logged_user_can_view_my_orders_menu(login_set_up, email, password) -> None:
    page = login_set_up
    # page.wait_for_load_state("networkidle")
    # expect (page.locator("text= Log In")).to_be_visible()
    # page.get_by_test_id("handle-button").click(timeout=3000)
    # page.get_by_test_id("signUp.switchToSignUp").click()
    # page.get_by_role("button", name="Log in with Email").click()
    # page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").click()
    # page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("symon.storozhenko@gmail.com")
    # page.get_by_role("textbox", name="Password").click(timeout=3000)
    # page.get_by_role("textbox", name="Password").fill("test123", timeout=2000)
    # page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    # page.pause()
    # page.wait_for_load_state("networkidle")
    expect(page.get_by_test_id("handle-button")).not_to_have_text("Log In")
    page.get_by_role("link", name="Shop Women", exact=True).click()
    product = page.get_by_role("link", name="Shop Women", exact=True).text_content()
    assert product != "Socks"
    print("Product found: ", product)
    all_links = page.get_by_role("link").all()
    for link in all_links:
        if link.text_content() == "$85":
            assert "socks" not in link.text_content().lower()
            print(link)
    print("Test - Passed")

    # playwright codegen https://symonstorozhenko.wixsite.com/website-1

