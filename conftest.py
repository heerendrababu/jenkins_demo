"""
fixtures: we can write setup and tear down in fixtures.
ex : opening browser is set up and closing the browser at the end is teardown
scopes : function, class, module, package, session
by default 'scope = function' but we can change it to class, module, package, session
"""

import pytest
from playwright.sync_api import sync_playwright
from UIAuto.utils.config_reader import get_config


@pytest.fixture(scope="session") # it will execute only once per the session
def config():
    print("Config fixture executed") # you can check in terminal that this fixture is executed only once per the session
    return get_config()


@pytest.fixture() # by default scope is function and function also called as "test definition"
def browser(config):
    # this is setup
    print("*** Browser fixture start ****")
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=config["headless"], slow_mo=500
        )
        yield browser
        # teardown
        browser.close()
    print("*** Browser fixture end ***")


@pytest.fixture
def page(browser, config):
    print("*** page started ***")
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(config["timeout"])
    # 🌟 ADD THESE TWO LINES HERE TO BLOCK THE ADS completely:
    page.route("**/*google*", lambda route: route.abort())
    page.route("**/*adsbygoogle*", lambda route: route.abort())
    page.goto(config["base_url"])
    yield page
    context.close()
    print("*** page end ***")

# @pytest.fixture()
# # creating new browser
# def browser():
#     print("*** Browswer fixture starts ***")
#     #setup code
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False,slow_mo=4000)
#         yield browser
#         # teardown
#         browser.close()
#     print("*** Browser fixture ends ***")
#
# # creating page in the above browser
# @pytest.fixture
# def page(browser):
#     print("page started")
#     context = browser.new_context()
#     page = context.new_page()
#     yield page
#     context.close()
#     print("page ended")