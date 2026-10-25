from playwright.sync_api import sync_playwright

def check_movie_rating():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com/")
        search_box = page.locator('[id="ti6dpd"]')
        search_box.fill('imdb')
        search_box.press('Enter')


        browser.close()