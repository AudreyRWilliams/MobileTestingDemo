# tests/test_hello.py
import os
import time
import unittest
from appium import webdriver

APP_PATH = os.path.expanduser(
    "~/MobileTestingDemo/ios/HelloSim/build/Build/Products/Debug-iphonesimulator/HelloSim.app"
)

class HelloSimTests(unittest.TestCase):
    def setUp(self):
        caps = {
            "platformName": "iOS",
            "automationName": "XCUITest",
            "deviceName": "iPhone 8",         # choose an installed simulator
            "platformVersion": "12.4",        # match simulator runtime on your machine
            "app": APP_PATH,
            "newCommandTimeout": 120
        }
        # Appium 1.x default hub:
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    def tearDown(self):
        if hasattr(self, "driver"):
            self.driver.quit()

    def test_tap_changes_label(self):
        # initial text
        label = self.driver.find_element_by_accessibility_id("helloLabel")
        self.assertEqual(label.text, "Hello")
        # tap button
        btn = self.driver.find_element_by_accessibility_id("tapButton")
        btn.click()
        time.sleep(0.5)
        # verify change
        label = self.driver.find_element_by_accessibility_id("helloLabel")
        self.assertEqual(label.text, "Tapped!")

if __name__ == "__main__":
    unittest.main(verbosity=2)

