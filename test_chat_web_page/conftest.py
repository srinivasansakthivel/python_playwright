import pytest


@pytest.fixture(scope='session')
def context_1(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.chat-avenue.com/general/
    page.goto("https://www.chat-avenue.com/general/")

    # Click button: has-text("Login")
    page.click("button:has-text(\"Login\")")

    # Click input[name="username"]
    page.click("input[name=\"username\"]")

    # Double click input[name="username"]
    page.dblclick("input[name=\"username\"]")

    # Triple click input[name="username"]
    page.click("input[name=\"username\"]", click_count=3)

    # Fill input[name="username"]
    page.fill("input[name=\"username\"]", "stosymon")

    # Press Tab
    page.press("input[name=\"username\"]", "Tab")

    # Fill input[name="password"]
    page.fill("input[name=\"password\"]", "123test")

    # Wait for navigation after login
    with page.expect_navigation():
        page.click("#login_form_box >> text=Login")

    # Yield context so it can be used in tests
    yield context


@pytest.fixture(scope='session')
def context_2(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=300)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.chat-avenue.com/general/
    page.goto("https://www.chat-avenue.com/general/")

    # Click button: has-text("Login")
    page.click("button:has-text(\"Login\")")

    # Click input[name="username"]
    page.click("input[name=\"username\"]")

    # Double click input[name="username"]
    page.dblclick("input[name=\"username\"]")

    # Triple click input[name="username"]
    page.click("input[name=\"username\"]", click_count=3)

    # Fill input[name="username"]
    page.fill("input[name=\"username\"]", "symon_storozhenko")

    # Press Tab
    page.press("input[name=\"username\"]", "Tab")

    # Fill input[name="password"]
    page.fill("input[name=\"password\"]", "123test")

    # Wait for navigation after login
    with page.expect_navigation():
        page.click("#login_form_box >> text=Login")

    # Yield context so it can be used in tests
    yield context


@pytest.fixture()
def login_set_up_for_chat(context_1, context_2, browser):
    page1 = context_1.new_page()
    page2 = context_2.new_page()
    page1.goto("https://www.chat-avenue.com/general/")
    page2.goto("https://www.chat-avenue.com/general/")
    page1.set_default_timeout(5000)
    page1.set_default_timeout(5000)

    yield page1, page2
    # time.sleep(5)
    page1.close()
    page2.close()
