import re

from playwright.sync_api import sync_playwright
from playwright.sync_api import expect


def search_docs(page, search_text):
    page.locator(".DocSearch-Button-Placeholder").click()
    page.get_by_placeholder("Search docs").fill(search_text)
    page.keyboard.press("Enter")
def test_demo(page):

        expect(page).to_have_title(re.compile("Playwright"))
        title = page.title()
        print("complete title : ",title)
        expect(page.get_by_role("heading",name = re.compile("Playwright")).nth(0)).to_be_visible()

        search_docs(page,'Python')
        expect(page).to_have_url('https://playwright.dev/python/docs/languages#python')

        search_docs(page,'Heerendra')
        expect(page.get_by_text("No results found for")).to_be_visible()

        browser.close()