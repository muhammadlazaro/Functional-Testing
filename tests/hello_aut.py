import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class AUTTestCase(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')

        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=options
        )

    def test_open_aut_home(self):
        # Akses AUT
        self.driver.get("http://host.docker.internal:8080")

        # Validasi teks khas AUT
        self.assertIn("Welcome back", self.driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
