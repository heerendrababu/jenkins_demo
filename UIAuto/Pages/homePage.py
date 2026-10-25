# we can have homepage file to verify all the elements in home page present or not and
# we can have methods to perform actions on those elements.
from UIAuto.Pages.basepage import BasePage


class HomePage(BasePage):

    home_icon = '[class="fa fa-home"]'
    products = '[class="material-icons card_travel"]' # or # [ href="/products"]
    cart = '[href="/view_cart"]'
    signup_login_link = '[href="/login"]'
    test_cases =  '[href="/test_cases"]'
    api_testing = '[href="/api_list"]'
    video_tutorials = '[href="https://www.youtube.com/c/AutomationExercise"]'
    contact_us = '[href="/contact_us"]'

    def launch_url(self, url):
        self.navigate(self.home_icon)

    def locator_is_visible(self,locator):
        return self.is_visible(locator)

    def click_signup(self):
         self.click(self.signup_login_link)