from UIAuto.Pages.basepage import BasePage


class SignupLogin(BasePage):
    # we inherit the BasePage and written methods.
    # we can write all the locators and methods for signup and login features.

    Signup_Login_Link = '[href="/login"]'
    new_user_signup = 'New User Signup!'
    name = '[data-qa="signup-name"]'
    email = '[data-qa="signup-email"]'
    submit_btn = '[data-qa="signup-button"]'

    #account information:
    enter_acct_info = 'Enter Account Information'
    mr_btn = '[id="id_gender1"]'
    mrs_btn = '[id="id_gender2"]'
    password_field = '[name="password"]'
    days = '[id = "days"]'
    months = '[id = "months"]'
    year = '[id="years"]'
    news_letter_check = '[id="newsletter"]'
    receive_options_check = '[id="optin"]'

    #address info:
    first_name = '[id="first_name"]'
    last_name = '[id="last_name"]'
    company = '[id="company"]'
    address = '[id="address1"]'
    address2 = '[id="address2"]'
    state = '[id="state"]'
    city = '[id="city"]'
    zipcode = '[id="zipcode"]'
    mobile = '[id="mobile_number"]'

    create_account = '[data-qa="create-account"]'
    account_creation_verify = '[data-qa="account-created"]'

    def enter_username(self,username):
        self.fill(self.name,username)
    def enter_email(self,email):
        self.fill(self.email,email)
    def click_login(self):
        self.click(self.submit_btn)

   #Above we created 3 functions, iam calling all these functions in do_signup function. so this is the way of pom design pattern.
    def do_signup(self,username,email):
        print("*** do logging started ***")
        self.enter_username(username)
        self.enter_email(email)
        self.click_login()
        print("*** do logging ended ***")

    #2. fill signup form after clicking signup button
    def fill_signup_account_info_form(self,title,password,day,month,year):
        print("*** fill signup form started ***")
        if title == 'Mr':
            self.click(self.mr_btn)
        else:
            self.click(self.mrs_btn)
        self.fill(self.password_field,password)
        self.select_dropdown_option(self.days, 'day', 'value')
        self.select_dropdown_option(self.months, month, 'label')
        self.select_dropdown_option(self.year, year, dropdown_value_type='value')
        self.check_checkbox(self.news_letter_check)
        self.check_checkbox(self.receive_options_check)
        print("*** fill account signup form ended ***")

    def fill_address_info(self,first_name,last_name,company,address1,address2,state,city,zipcode,mobile):
        print("*** fill  address info started ***")

        self.fill(self.first_name, first_name)
        self.fill(self.last_name, last_name)
        self.fill(self.company, company)
        self.fill(self.address, address1)
        self.fill(self.address2, address2)
        self.fill(self.state, state)
        self.fill(self.city, city)
        self.fill(self.zipcode, zipcode)
        self.fill(self.mobile, mobile)
        print("*** fill  address info ended ***")

    def click_create_account_button(self):
        print("click create account button")
        self.click(self.create_account)

    def is_account_created(self):
        print("create account verification started")
        return self.page.get_by_text("ACCOUNT CREATED!").is_visible() # returns boolean

    # def click_create_account_button(self):
    #     print("create account verification started")
    #     self.click(self.create_account)
    #     return self.page.get_by_text("ACCOUNT CREATED!").is_visible()




# benefits of dividing like this ?
# ans : if we need any changes at any point of time we can easily understand where changes are needed and-
# we can easily make changes in that particular function instead of searching the whole code.

# 2 - fill_signup_form points :
# here page is a fixture that is coming from BaseClass (we are inheriting from BasePage[BaseClass])  in 'BaseClass' constructor -
# we have this 'page' . So using that 'page' we are going to use playwright methods either click, fill etc.
# so we are not using the above 2 points because if we use page directly we are accesing 'page browser' so we are using basepage methods -
# like click, fill etc. which are already defined in BasePage and we are using those methods in this class.
# Note :
# 1 - if type is input in html we can go with id,name,css selector, xpath etc. -
# 2 - but if type is button we can go with text, css selector, xpath etc. but not with id and name.