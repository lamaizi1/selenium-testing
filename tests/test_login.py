from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login(driver):

    wait = WebDriverWait(driver, 10)

    # Ouvrir SauceDemo
    driver.get("https://www.saucedemo.com/")

    # Username
    username = wait.until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    username.send_keys("standard_user")

    # Password
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # Login
    driver.find_element(By.ID, "login-button").click()

    # Vérifier que le titre apparaît
    products_title = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    assert products_title.text == "Products"

    print("✅ Test Passed : Login réussi")