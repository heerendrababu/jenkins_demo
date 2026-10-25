import pytest
from playwright.sync_api import sync_playwright


# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False,slow_mo=2000)
#     page = browser.new_page()
#     page.goto("https://demo.automationtesting.in/Alerts.html")
#     page.locator('#OKTab').click()
#     with page.expect_event('dialog')as dailog_info:
#         page.locator('[onclick="alertbox()"]').click(force=True)
        #s

#     # — value is a property, not a method.
#     dialog = dailog_info.value
#     print(dialog.type)
#     print(dialog.message)
#     dialog.accept()


"""
# This function handles the alert when it appears
def handle_dialog(dialog):
    print(f"Alert message: {dialog.message}")
    dialog.accept()       # Clicks OK

with sync_playwright() as p:
    # 1. Launch browser
    b = p.chromium.launch(headless=False, slow_mo=2000)
    # 2. Create page
    page = b.new_page()
    # 3. Register alert handler
    page.on("dialog", handle_dialog)
    # 4. Open website
    page.goto("https://demo.automationtesting.in/Alerts.html")
    # 5. Open the Alert section
    # page.locator('#OKTab').click()
    # 6. Click the button that opens the alert
    page.locator('[onclick="alertbox()"]').click()
    # 7. Close browser
    b.close()
"""
"""
# window handling:-
@pytest.mark.win
def test_window_handling():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False, slow_mo=1000)

        context = browser.new_context()

        # Main page
        page = context.new_page()

        page.goto("https://demo.automationtesting.in/Windows.html")

        print("Main page:", page.title())

        # ==================================================
        # 1️⃣ NEW TAB
        # ==================================================

        with context.expect_page() as page_info:
            page.locator("text=Open New Tabbed Windows").click()

        new_tab = page_info.value

        new_tab.wait_for_load_state()

        print("New tab URL:", new_tab.url)

        new_tab.bring_to_front()

        # Close new tab
        new_tab.close()

        print("New tab closed:", new_tab.is_closed())

        # ==================================================
        # 2️⃣ NEW SEPARATE WINDOW
        # ==================================================

        with context.expect_page() as window_info:
            page.locator("text=Open New Seperate Windows").click()

        new_window = window_info.value

        new_window.wait_for_load_state()

        print("New window URL:", new_window.url)

        new_window.bring_to_front()

        # Close new window
        new_window.close()

        # ==================================================
        # 3️⃣ MULTIPLE WINDOWS
        # ==================================================

        with context.expect_page() as multiple_info:
            page.locator("text=Open Seperate Multiple Windows").click()

        first_window = multiple_info.value

        first_window.wait_for_load_state()

        print("First new window:", first_window.url)

        # Check all pages
        print("Total open pages:", len(context.pages))

        # Access another page directly
        if len(context.pages) > 2:
            second_window = context.pages[2]

            print("Second window:", second_window.url)

            second_window.bring_to_front()

            second_window.close()

        # Return to main page
        page.bring_to_front()

        print("Back to main page:", page.url)

        browser.close()
"""
"""
Register handler
      ↓
Open website
      ↓
Open Alert section
      ↓
Click alert button
      ↓
Alert appears
      ↓
handle_dialog() automatically runs
      ↓
dialog.accept() → OK
      ↓
Continue
      ↓
Close browser
"""

"""
why can't we write that handle_dialog method under the below line
page.locator("#alert-button").click()
Because JavaScript alerts are blocking—the moment you run page.locator("#alert-button").click(), 
the browser stops executing everything else until that alert is handled.

If you register page.on("dialog", handle_dialog) after clicking, Playwright will get stuck waiting for the alert 
to close before it can ever reach your handler code. Setting it up before ensures Playwright is ready to handle 
the alert the millisecond it pops up.
"""















