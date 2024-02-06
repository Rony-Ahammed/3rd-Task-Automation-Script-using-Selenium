from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get("https://dhiofur.texrootsourcing.com/")

menu = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "site-menu")))

menu_items = menu.find_elements_by_tag_name("li")

for item in menu_items:
    driver.execute_script("arguments[0].scrollIntoView(true);", item)
    item_text = item.text
    print("Clicking on menu item:", item_text)
    item.click()

    print("Page title:", driver.title)

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.some-element")))
        print("Found the specific element.")
    except:
        print("Timed out waiting for specific element.")

    driver.back()

driver.quit()
