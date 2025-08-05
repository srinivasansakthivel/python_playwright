import os
import pytest

PASSWORD = os.environ['PASSWORD']

# try:
#     PASSWORD = os.environ['PASSWORD']
# except:
#     import utils.secret_config
#     PASSWORD = utils.secret_config.PASSWORD


@pytest.fixture(scope="function")
def set_up(browser):
    # browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # page.set_default_timeout(15000)
    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    yield page
    page.close()


@pytest.fixture(scope="function")
def login_set_up(set_up, email, password):
    page = set_up
    page.wait_for_load_state("networkidle")
    page.get_by_test_id("handle-button").click(timeout=3000)
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").click()
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill(email)
    page.get_by_role("textbox", name="Password").click(timeout=3000)
    page.get_by_role("textbox", name="Password").fill(PASSWORD, timeout=2000)
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()

    yield page


@pytest.fixture
def go_to_new_collection_page(page):
    page.goto("/new-collection")
    page.set_default_timeout(30000)

    yield page
