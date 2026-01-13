import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class AutTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')

        # Selenium diakses dari HOST
        self.browser = webdriver.Remote(
            command_executor="http://localhost:4444",
            options=options
        )
        self.addCleanup(self.browser.quit)

    def test_homepage(self):
        # AUT diakses dari HOST
        self.browser.get("http://localhost:8080")

        expected_result = "Welcome back, Guest!"
        actual_result = self.browser.find_element(By.TAG_NAME, 'p')

        self.assertIn(expected_result, actual_result.text)

if __name__ == "__main__":
    unittest.main(
        argv=['first-arg-is-ignored'],
        verbosity=2,
        warnings='ignore'
    )
