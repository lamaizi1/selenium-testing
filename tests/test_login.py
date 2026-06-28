from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Lancer Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Ouvrir SauceDemo
driver.get("https://www.saucedemo.com/")

# Attendre au maximum 10 secondes que le champ username soit présent
wait = WebDriverWait(driver, 10)

# Username
username = wait.until(
    EC.presence_of_element_located((By.ID, "user-name"))
)
username.send_keys("standard_user")

# Password
password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")

# Login
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# Vérifier que le titre "Products" apparaît
products_title = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "title"))
)

assert products_title.text == "Products"

print("✅ Test Passed : Login réussi")

driver.quit()