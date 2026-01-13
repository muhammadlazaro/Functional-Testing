import unittest, sys
from selenium import webdriver
from selenium.webdriver.common.by import By

class AutTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')

        # Selenium container name
        server = "http://selenium:4444"

        self.browser = webdriver.Remote(
            command_executor=server,
            options=options
        )
        self.addCleanup(self.browser.quit)

    def test_homepage(self):
        # AUT container name
        url = "http://aut"

        self.browser.get(url)

        expected_result = "Welcome back, Guest!"
        actual_result = self.browser.find_element(By.TAG_NAME, 'p')

        self.assertIn(expected_result, actual_result.text)

if __name__ == "__main__":
    unittest.main(
        argv=['first-arg-is-ignored'],
        verbosity=2,
        warnings='ignore'
    )
