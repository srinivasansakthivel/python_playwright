from playwright.sync_api import expect
from pytest_playwright_visual.plugin import assert_snapshot

from pom.home_page_elements import HomePage


def test_visual_landing_1_1(page, assert_snapshot) -> None:
    #Assess - Given
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    homepage = HomePage(page)
    # expect(homepage.celebrate_body).to_be_visible()
    assert_snapshot(page.screenshot())


def test_visual_landing_1_2(page, assert_snapshot) -> None:
    #Assess - Given
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    homepage = HomePage(page)
    # expect(homepage.celebrate_body).to_be_visible()
    assert_snapshot(page.screenshot())