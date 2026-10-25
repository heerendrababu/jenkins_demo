import re

from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

def test_practice():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,slow_mo=2000)
        page = browser.new_page()
        page.goto("https://playwright.dev/python/")
        expect(page).to_have_title(re.compile('Playwright'))
        title = page.title()
        print(title,'hi')
        expect(page.get_by_role("heading",name = "Playwright  enables reliable web automation for testing")).to_be_visible()
        expect(page).to_have_url('https://playwright.dev/python/')


