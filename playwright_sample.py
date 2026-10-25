import time
from cProfile import label

import pytest
from playwright.sync_api import sync_playwright

from conftest import browser


# with sync_playwright() as p:
#     browser = p.chromium.launch(headless = False, slow_mo = 3000)
#     #browser1 = p.firefox.launch(headless = False)
#     page = browser.new_page()
#     page.goto("https://automationexercise.com/")
#     page.get_by_role("link" ,name = " Products").click()
#     page.get_by_placeholder(text="Search Product").fill("tshirts")
#     page.get_by_text(text = "Cart").first.click()

"""
def test_contact_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False, slow_mo = 3000)
        #browser1 = p.firefox.launch(headless = False)
        page = browser.new_page()
        page.goto("https://www.rapido.bike/Contact")
        page.get_by_placeholder(text="Enter your name").fill("Heerendra Babu")
        page.get_by_placeholder(text = "Enter your email").fill("heerendra@gmail.com")
        page.get_by_placeholder(text = "Enter your mobile number").fill("8688465312")
        page.locator("select").nth(0).select_option(label = "customer")
        page.locator("select").nth(1).wait_for(state="visible")
        page.locator("select").nth(1).select_option(label="Driver Appreciation")
        page.get_by_placeholder(text = "Enter your comment").fill("i registered")
        page.get_by_role("button",name = "Submit").click()
        assert page.get_by_text("Thank you for reaching out,").is_visible()
        page.get_by_role("button",name = "Done").click()
        browser.close()
"""
"""
@pytest.mark.demo
def test_play_lab():
    with sync_playwright() as p:
        browser1 = p.chromium.launch(headless=False,slow_mo=3000)
        page = browser1.new_page()
        page.goto("https://playwrightlab.github.io/?utm_source=chatgpt.com")
        page.get_by_role('link',name = "Login", exact=True).click()
        #page.locator('a[href="login.html"]').click()
        assert page.get_by_text("Welcome back",exact=True).is_visible()
        #or [above is preferred]
        #assert page.locator('//*[contains(text(),"Welcome back")]').is_visible()
        page.get_by_placeholder(text="you@example.com").fill("test@playlab.com")
        page.get_by_placeholder(text ="Enter your password").fill("Password123")
        page.get_by_role("button", name="Sign In").click()
        page.locator('[id="goToDashboard"]').click()
        page.locator('[href="locators.html"]').click()
        page.locator('[href="#get-by-role"]').nth(1).click()
        page.get_by_placeholder(text="Search…").fill("Hi babu")
        page.get_by_role("radio",name = "Express shipping").check()
        #page.locator("select").nth(1).select_option(label="India")
        #or
        page.get_by_role("combobox",name = "Country").select_option("India")
        slider = page.locator('input[aria-label="Volume"]')
        for i in range(20,31):
            slider.fill(str(i))
            page.wait_for_timeout(0.2)
        count = page.locator(".loc-demo li").count()
        print("count of list: ",count)
        browser1.close()
"""


# Notepad :
"""
“I prefer Playwright's user-facing locators 
like get_by_role() when possible. I use CSS/XPath locators when a unique role-based locator isn't available.”

get_by_role() → Role-based locator
               Example: get_by_role("radio", name="Express shipping")

locator()     → CSS/attribute-based locator
               Example: locator('input[aria-label="Express shipping"]')
count():
ul li              → all lists
.loc-demo li       → list inside that container
.nth(0).locator()  → specific container's list
"""
# XPath vs CSS + nth()
#
# XPath:
# (//select)[1]
# → First element = [1]
# → Index starts from 1
#
# CSS + nth():
# select.nth(0)
# → First element = nth(0)
# → Index starts from 0
#
# Remember:
# XPath        → 1, 2, 3
# nth()        → 0, 1, 2






# from playwright.sync_api import sync_playwright, expect
#
# url = "https://practicetestautomation.com/practice-test-login/"
#
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page=browser.new_page()
#     page.goto(url)
#     page.locator("#username").fill("student")
#     page.locator("#password").fill("Password123")
#     page.locator("#submit").click()
#     page.wait_for_timeout(2000)
#     expect(page).to_have_url("https://practicetestautomation.com/logged-in-successfully/")
#     expect(page.locator("body")).to_contain_text("Congratulations student. You successfully logged in!")
#     expect(page.get_by_role("link",name="Log out")).to_be_visible()
#     print("positive login test passed")
#     browser.close()

with sync_playwright() as p:
    b = p.chromium.launch(headless=False,slow_mo=2000)#,args=["--start-maximized"]) # Launches the Chromium browser in maximized window
    # or page = b.new_page("no_viewport=True")#This lets the browser use the actual window size rather than a fixed Playwright viewport.
    context = b.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("#name").fill('Heerendra Babu')
    page.get_by_placeholder(text='Enter EMail').fill("heerendrababu9@gmail.com")
    page.get_by_role('textbox',name='phone').fill('9888009090')
    page.get_by_label(text='Address:').fill('Marathahalli,Bangalore,karnataka')
    #"Address:" automatically goes into the first parameter, which is text.
    #So get_by_label(text="Address:") and get_by_label("Address:") are the same.
    #page.get_by_label("Male", exact=True)
    #or
    page.locator('//input[@id="male"]').check()
    # or
    #page.locator("#male").check()
    #page.locator("#days").select_option(label="monday")
    page.get_by_role("checkbox", name="Monday", exact=True).check()
    page.get_by_role("combobox",name = "country").select_option(label="India")
    page.get_by_label('Colors:').select_option(['red','yellow'])
    page.locator('//select[@id="animals"]').select_option(['cat','cheetah','elephant'])
    page.locator('#datepicker').fill('09/29/0000')
    # page.locator('[name="SelectedDate"]').click()
    # page.locator(".ui-datepicker-month").select_option("8")  # September
    # page.locator(".ui-datepicker-year").select_option("2001")
    # page.get_by_role("link", name="2", exact=True).click()  # Select 2nd

    page.locator('#start-date').fill('25-09-2026')
    page.locator('#end-date').fill('30-09-2026')
    page.get_by_role("button",name='Submit').click()

    """
    "usa" → selects using the value attribute
     label="United States" → selects using the visible text
      select_option() with nothing → ❌ doesn't tell Playwright what to select.
    """
    b.close()
"""
# ID
page.locator("#phone")

# class
page.locator(".form-control")

# name
page.locator('[name="phone"]')

# any attribute
page.locator('[placeholder="Enter Phone"]')
Easy rule
id="phone" → #phone
class="form-control" → .form-control
name="phone" → [name="phone"]
type="text" → [type="text"]
"""



























