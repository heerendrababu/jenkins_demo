"""
We can write utilities functions.
Env: Testing -> Lower env - >Staging, QA, Milestone -> Production

prod: https://automationexercise.com/
stag: https://staging.automationexercise.com/
qa: https://qa.automationexercise.com/
milestone: https://milestone.automationexercise.com/

"""
import json
from pathlib import Path

def get_config():
    config_path = Path(r"C:\Users\lenova\PycharmProjects\Playwright_Project\UIAuto\Config\config.json")
    #config_path = Path(r"C:\Users\lenova\PycharmProjects\Playwright_Project\UIAuto\Config\alertEx.json")

    with open(config_path, "r") as file:
        return json.load(file)

"""
alertEx.json
      ↓
config_reader.py reads JSON
      ↓
conftest.py gets base_url
      ↓
page fixture
      ↓
page.goto(base_url)
      ↓
Alerts.html opens
      ↓
test_alerts.py runs
"""