import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

class ExampleTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')

        self.driver = webdriver.Remote(
            command_executor="http://localhost:4444",
            options=options
        )

        os.makedirs("screenshots", exist_ok=True)

    def test_example(self):
        self.driver.get("https://example.com")
        self.driver.save_screenshot("screenshots/example.png")
        self.assertIn("Example Domain", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()