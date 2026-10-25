import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,slow_mo=2000)
        page = browser.new_page()
        page.goto("https://playwright.dev/python/")
        browser.close()

