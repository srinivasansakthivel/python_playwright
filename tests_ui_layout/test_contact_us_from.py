import time

from playwright.sync_api import Playwright, sync_playwright
import pytest
from pom.contact_us_page import ContactUsPage


@pytest.mark.smoke
@pytest.mark.regression
def test_submit_form(set_up):
    page = set_up
    contact_us = ContactUsPage(page)
    contact_us.navigate()
    contact_us.submit_form(
        name="Symon",
        address="123 Main St",
        email="test@email.com",
        phone="9842714115",
        subj="Subject Test",
        message="Test Message"
    )
