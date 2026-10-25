
import pytest
from playwright.sync_api import sync_playwright


@pytest.mark.win1
def test_win():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=2000)

        context = browser.new_context()

        # Open 1st tab - ChatGPT
        page = context.new_page()
        page.goto("https://chatgpt.com/")

        # Open 2nd tab - EPFO
        epfo = context.new_page()
        epfo.goto("https://passbook.epfindia.gov.in/")

        # Open 3rd tab - WhatsApp
        whatsapp = context.new_page()
        whatsapp.goto("https://web.whatsapp.com/")

        # Get all open pages (tabs)
        pages = page.context.pages
        print(pages)

        # Print total tabs
        print("Total tabs:", len(pages))

        # Switch from 2nd tab to 3rd tab
        pages[1].bring_to_front()
        print("page 1 loaded ")
        pages[2].bring_to_front()
        print("page 2 loaded")
        pages[0].bring_to_front()
        print("page 3 loaded")

        input("Press Enter to close...")
        browser.close()
