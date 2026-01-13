from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

driver.get("http://localhost:8080")
time.sleep(3)

# Validasi teks halaman
assert "Welcome back" in driver.page_source

print("SELENIUM TEST BERHASIL")

driver.quit()
