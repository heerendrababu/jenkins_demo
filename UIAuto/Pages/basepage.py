"""
Playwright : it is open source to perform ui, api and mobile automation testing.
it is developed by microsoft and it is used to test web applications.

Page : Fixture
Base page/Base class : will contain generic methods that we can use in other classes.
Methods: navigate,fill, click,select_option(to select drop_down we need to use select_option) -- once we inherit this base page in another-
classes we are able to access all the above methods of base page in other classes.
"""
from playwright.sync_api import Page

# pep8 standards : mentioning argument along with its type in the method signature
class BasePage:
    def __init__(self,page:Page): # constructor
        self.page = page # instance attribute

    def navigate(self,url:str): # or url only you can mention instead of along with str
        self.page.goto(url)

    def click(self,locator):
        try:
            self.page.click(locator)
        except TimeoutError as e:
            print(f"got the exception: {e}")

    def fill(self,locator,text):
        try:
            self.page.fill(locator,text)
        except TimeoutError as e:
            print(f"got the exception: {e}")

    def get_text(self,locator):
        return self.page.locator(locator).text_content()

    def is_visible(self,locator):
        return self.page.locator(locator).is_visible(timeout=2000) # 3 seconds

    def is_checked(self,locator):
        return self.page.locator(locator).is_checked(timeout=3000) # 3 seconds

    def select_dropdown_option(self,dropdown_locator,dropdown_value,dropdown_value_type):
        """
        THis method will select the dropdown option from dropdown
        :param dropdown_locator: it is a web element for dropdown item
        :param dropdown_value: dropdown value to select the dropdown option, ex: label, index, value
        :param dropdown_value_type: it is a dropdown value type, ex: label, index, value type
        """
        dropdown = self.page.locator(dropdown_locator)
        if dropdown_value_type == 'label':
            dropdown.select_option(label=dropdown_value)
        elif dropdown_value_type == 'value':
            dropdown.select_option(value= dropdown_value)
        else:
            dropdown.select_option(index=dropdown_value)

    def check_checkbox(self, locator):
        if self.is_checked(locator):
            print("Already checkbox is checked")
        else:
            print("select check box")
            self.page.locator(locator).click()


