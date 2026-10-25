"""
as per the pytest convention test file name, test class name and
test defination name must be starts with test

fixtues: we can write setup and teardown in fixtures
ex: opening browser is setup and closing the browser at the end is teardown
scopes: function, class, module, session, package
by default is the function scope

assert: we can use to verification.
TO run : pytest testpath -s -v
-s : to display logs in console
-v : verbose to get the detailed information
-k : to collect the test case with test case name
-m : to collect the test case with marker name
-n : to run the test cases in parallel

"""
import json
import time

import os

import pytest

from UIAuto.Pages.signupLoginPage import SignupLogin
from UIAuto.Pages.homePage import HomePage
import random
import string

class TestSignupLogin:
    with open(r"C:\Users\lenova\PycharmProjects\Playwright_Project\UIAuto\Test_data\input_data.json") as file:
        test_data = json.load(file) # Converts JSON data into a list of dictionaries
        print(type(test_data))

    @pytest.mark.user_reg
    # data1 is the parameter that receives one dictionary at a time from test_data during parameterization
    @pytest.mark.parametrize("data",test_data)
    def test_signup(self,page,data):
        auto = random.choices(string.ascii_lowercase, k=8) #a-z
        email = "".join(auto) + "_" + data["email"]    # dict["key"] -> gives the corresponding value
        name = "".join(auto) + "" + data["name"]
        print(f"name: {name} and email: {email}")
        #page = page
        signup_login = SignupLogin(page)
        home_page = HomePage(page)
        assert home_page.locator_is_visible(home_page.home_icon), "Home page is not loading"
        home_page.click_signup()
        signup_login.do_signup(name,email)
        assert home_page.page.get_by_text(signup_login.enter_acct_info).is_visible(), "Signup account info page is not loaded"
        signup_login.fill_signup_account_info_form('Mr','Babu@123','26','December','2000')
        signup_login.fill_address_info("Heerendra", "babu", "Kandanathi",
                                       "Bangalore","Bommanahalli", "Karnataka", "Bengaluru", "560038","9666110520")

        signup_login.click_create_account_button()
        assert signup_login.is_account_created(),"Account creation failed"

# ============================================================
# ALERTS / DIALOGS
# ============================================================

    @pytest.mark.smoke
    @pytest.mark.alert
    def test_alerts(self, page):
        """
        Handling JavaScript alerts using page.on("dialog")
        """

        # --------------------------------------------------------
        # 1. OK ALERT
        # --------------------------------------------------------

        def handle_alert(dialog):
            print(f"Dialog type: {dialog.type}")
            print(f"Dialog message: {dialog.message}")
            dialog.accept()

        # Register dialog handler
        page.on("dialog", handle_alert)

        # Click OK Tab
        page.locator('[href="#OKTab"]').click()

        # Click Alert button
        # When dialog appears, handle_alert() automatically executes
        page.locator('[onclick="alertbox()"]').click()

        # --------------------------------------------------------
        # 2. CONFIRM ALERT - OK
        # --------------------------------------------------------

        # Click Cancel Tab
        page.locator('[href="#CancelTab"]').click()

        # Click Confirm button
        # Dialog automatically goes to handle_alert()
        page.locator('[onclick="confirmbox()"]').click()

        # handle_alert() calls dialog.accept()
        # So OK is clicked automatically

        # --------------------------------------------------------
        # 3. PROMPT ALERT
        # --------------------------------------------------------

        # For prompt we need to enter text,
        # so we need a different handler.

        page.remove_listener("dialog", handle_alert)

        def handle_prompt(dialog):
            print(f"Dialog type: {dialog.type}")
            print(f"Dialog message: {dialog.message}")
            dialog.accept("hello")

        page.on("dialog", handle_prompt)

        # Click Textbox Tab
        page.locator('[href="#Textbox"]').click()

        # Click Prompt button
        page.locator('[onclick="promptbox()"]').click()


    # ============================================================
    # DEFAULT ALERT HANDLING
    # ============================================================

    @pytest.mark.default_alert
    def test_alerts_default(self, page):

        def handle_dialog(dialog):
            print(f"Dialog type: {dialog.type}")
            print(f"Dialog message: {dialog.message}")
            dialog.accept()

        # Register automatic dialog handler
        page.on("dialog", handle_dialog)

        # Click OK Tab
        page.locator('[href="#OKTab"]').click()

        # Click Alert button
        page.locator('[onclick="alertbox()"]').click()

    # window handling / multiplepage handling:
    @pytest.mark.windows
    def test_windows_pages(self, page):
        page = page
        page.locator('[href="#Tabbed"]').click()
        page.locator('[href="http://www.selenium.dev"]').click()
        print(page.title())
        page.context.pages[0].bring_to_front()
        print(page.context.pages[0].url)
        #assert page.context.pages[0].url == "https://demo.automationtesting.in/Windows.html","page not redirected" # no need we checked and confirmed by 'print[page.context.pages[0].url]'
        # flow
        # page.context → gets the current BrowserContext
        # .pages → gets all Pages/Tabs in that context
        # [0] → selects the first page/tab
        # .bring_to_front() → switches focus to that page
        # .url → gets the current URL of that page

    @pytest.mark.frames
    def test_iframes(self, page):
        # Open Single iframe tab
        page.locator('[href="#Single"]').click()

        # Locate Single iframe
        frame = page.frame_locator('[id="singleframe"]')

        # Fill input inside Single iframe
        frame.locator('[type="text"]').fill("hello hai")

        # Open Multiple Frames tab
        page.locator('[href="#Multiple"]').click()

        # Locate outer/parent iframe
        frame1 = page.frame_locator('[src="MultipleFrames.html"]')

        # Print text from outer iframe
        print(frame1.get_by_text('Nested iFrames').text_content())

        # Locate inner/child iframe
        frame2 = frame1.frame_locator('[src="SingleFrame.html"]')
        time.sleep(10)

        # Fill input inside inner iframe
        frame2.locator('[type="text"]').fill("Heerendra Babu")

    @pytest.mark.files
    def test_file_upload(self,page):

        # Open the file upload page
        page.goto("https://the-internet.herokuapp.com/upload")

        # Store the path of the file that we want to upload
        file_path = r"C:\Users\lenova\PycharmProjects\Playwright_Project\UIAuto\Test_data\sample.txt"

        # Locate the file input element and attach the file
        page.locator("#file-upload").set_input_files(file_path)

        # Click the Upload button
        page.locator("#file-submit").click()

        # Verify that the upload was successful
        # Get the text from the <h3> element and compare it with expected text
        assert page.locator("h3").inner_text() == "File Uploaded!"

    @pytest.mark.download
    def test_file_download(self,page):
        # Open the page containing the download link
        page.goto("https://the-internet.herokuapp.com/download")

        # Wait for the download to start when we click the file
        with page.expect_download() as download_info:
            # Click the file that we want to download
            page.get_by_text("examplefile.json").click()

        # Get the downloaded file object
        download = download_info.value

        # Save the downloaded file to the specified location
        download.save_as(r"C:\Users\lenova\PycharmProjects\Playwright_Project\UIAuto\Test_data\downloaded_example_file.json")

    @pytest.mark.dom
    def test_shadow_dom(self,page):
        # Open the Shadow DOM practice page
        page.goto("https://www.playwrightautomation.com/shadow-dom-lab.html")

        # Locate the input inside the open Shadow DOM
        page.locator("#sd-email").fill("admin@playwrightlab.com")

        # Verify the value
        assert page.locator("#sd-email").input_value() == "admin@playwrightlab.com"

    @pytest.mark.sst
    def test_login(self,page):
        # Open login page
        page.goto("https://the-internet.herokuapp.com/login")

        # Enter username and password
        page.locator("#username").fill("tomsmith")
        page.locator("#password").fill("SuperSecretPassword!")

        # Login
        page.locator("button[type='submit']").click()

        # Save cookies and local storage
        page.context.storage_state(path="auth.json")

    @pytest.mark.sst_used
    def test_secure_page(self,browser):
        # Create a browser context using the saved session
        context = browser.new_context(storage_state="auth.json")

        # Create a new page
        page = context.new_page()

        # Open secure page
        page.goto("https://the-internet.herokuapp.com/secure")
        page.wait_for_timeout(10)
        # Verify that we are already logged in
        assert page.locator("h2").inner_text() == "Secure Area"

        # Close the context
        context.close()

    @pytest.mark.s_shot
    def test_screenshot(self,page):
        # Open the website
        page.goto("https://the-internet.herokuapp.com/")

        # Create Screenshots folder inside the project
        os.makedirs("Screenshots", exist_ok=True)

        # Take screenshot and save it inside Screenshots folder
        page.screenshot(
            path=r"Screenshots\homepage.png",
            full_page=True
        )

    @pytest.mark.video
    def test_video(self,browser):
        context = browser.new_context(record_video_dir="Videos/")

        page = context.new_page()

        page.goto("https://the-internet.herokuapp.com/")

        # Simple action
        page.locator("h1").is_visible()

        # Close context to save video
        context.close()


"""
Shadow DOM isolates a component's internal HTML and CSS from the rest of the web page, 
preventing main-page styles or scripts from accidentally breaking it.
"""

#----------------------------------------------------------------------------------------------------------------------
# dynamic way:
"""
    def handle_dialog(self, dialog):
        print(f"Message: {dialog.message}")
        print(f"Type: {dialog.type}")
        time.sleep(3)
        dialog.accept()
        print("popup ok got clicked...")

    @pytest.mark.alert
    def test_alerts(self, page):
        page.on("dialog", self.handle_dialog)

        page.locator('[href="#OKTab"]').click()
        page.locator('[onclick="alertbox()"]').click()
"""


#--------------------------------------------------------------------------------
    # @pytest.mark.smoke
    # @pytest.mark.alert
    # def test_alerts(self, page):
    #     # 1. Press 'Escape' just in case a full-screen ad popped up
    #     #page.keyboard.press("Escape")
    #
    #     # 2. Click the tab to make sure we are on the right section
    #     page.locator('[href="#OKTab"]').click()
    #
    #     # 3. Tell Playwright to watch out for the pop-up alert box
    #     with page.expect_event("dialog") as dialog_info:
    #         # 4. Click the button to trigger the alert box
    #         page.locator('[onclick="alertbox()"]').click()
    #
    #     # 5. Grab the alert box and click "OK"
    #     dialog = dialog_info.value
    #     dialog.accept()


# by using self keyword in function we can use class variables
"""
test_data → list
              ↓
        ┌──────────────┐
        ↓              ↓
     dictionary      dictionary
        ↓              ↓
    name, email    name, email
"""
