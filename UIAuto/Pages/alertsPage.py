# from UIAuto.Pages.basepage import BasePage
#
# class AlertsPage(BasePage):
#     # Alert locators:
#     ok_tab = '[href="#OKTab"]'
#     alert_button = '[onclick="alertbox()"]'
#
#     cancel_tab = '[href="#CancelTab"]'
#     confirm_button = '[onclick="alertbox()"]'
#
#     text_tab = '[href="#Textbox"]'
#     prompt_button = '[onclick="promptbox()"]'
#
#     def click_alert(self):
#         self.click(self.ok_tab)
#
#         with self.page.expect_event("dialog") as d:
#             self.page.locator(self.alert_button).click()
#
#         dialog = d.value
#         print(dialog.message)
#         dialog.accept()
#     # def click_alert(self):
#     #     print("*** click_alert started ***")
#     #     self.click(self.ok_tab)
#     #
#     #     with self.page.expect_event("dialog") as d:
#     #         self.page.locator(self.alert_button).click(force=True)
#     #     return d.value
#
#     # def click_confirm(self):
#     #     self.click(self.cancel_tab)
#     #
#     #     with self.page.expect_event("dialog") as d:
#     #         self.page.locator(self.confirm_button).click(force=True)
#     #
#     #     return d.value
#     #
#     # def click_prompt(self):
#     #     self.click(self.text_tab)
#     #
#     #     with self.page.expect_event("dialog") as d:
#     #         self.page.locator(self.prompt_button).click(force=True)
#     #     return d.value