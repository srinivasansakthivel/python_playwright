from playwright.sync_api import Playwright, sync_playwright, expect
from pom.home_page_elements import HomePage
import pytest


@pytest.mark.regression
@pytest.mark.parametrize("email", ["symon.storozhenko@gmail.com"])
@pytest.mark.parametrize("password", ["test123"])
@pytest.mark.skip
def test_about_us_section_verbiage_1(login_set_up):
    page = login_set_up
    home_page = HomePage(page)
    expect(home_page.celebrate_body).to_be_visible()
    expect(home_page.celebrate_header).to_be_visible()
    page.close()


@pytest.mark.integration
# @pytest.mark.parametrize("email", ["symon.storozhenko@gmail.com"])
# @pytest.mark.parametrize("password", ["test123"])
def test_about_us_section_verbiage_2(set_up):
    page = set_up
    page.goto('https://symonstorozhenko.wixsite.com/website-1')
    page.set_default_timeout(3000)
    home_page = HomePage(page)
    expect(home_page.celebrate_body).to_be_visible()
    expect(home_page.celebrate_header).to_be_visible()
    page.close()
