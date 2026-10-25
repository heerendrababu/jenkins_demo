# """
# BasePage → generic methods
# AlertsPage → alert locators + alert actions
# test_alerts.py → test flow + assertions
# alertconfig.json → alert environment/configuration
# """
# import time
#
# import pytest
#
# from UIAuto.Pages.alertsPage import AlertsPage
#
# class TestAlerts:
#     # @pytest.mark.smoke
#     # @pytest.mark.alert
#     def test_alerts(self, page):
#         """
#         Handling the alerts with dialog
#         """
#         try:
#             page.locator('[href="#OKTab"]').click()
#             page.wait_for_timeout(2000)
#             with page.expect_event("dialog") as d:
#                 page.locator('[onclick="alertbox()"]').click()
#             #page.wait_for_timeout(2000)
#             dialog = d.value
#             print(d.message)
#             print(d.type)
#             dialog.accept()
#             time.sleep(1000)
#         except Exception as e:
#             print("Got the execpetion", e)
#
#
#
#     # def test_alerts(self,page):
#     #     alerts = AlertsPage(page)
#     #     alerts.click_alert()
#         #ok alert
#         # dialog = alerts.click_alert()
#         # print(dialog.type)
#         # print(dialog.message)
#         # page.wait_for_timeout(3000)
#         # dialog.accept()
#
#         # #cancel alert
#         # dialog = alerts.click_confirm()
#         # print(dialog.type)
#         # print(dialog.message)
#         # dialog.dismiss()
#         #
#         # #prompt alert
#         # dialog = alerts.click_prompt()
#         # print(dialog.type)
#         # print(dialog.message)
#         # dialog.accept("Heerendra Babu")
#
