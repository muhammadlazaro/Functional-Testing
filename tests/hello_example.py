import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')

        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=options
        )

    def test_open_example(self):
        self.driver.get("https://example.com")
        self.assertIn("Example Domain", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
