from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep

options = Options()

driver = webdriver.Firefox(options=options)

driver.get('https://play2048.co/')



# Cookies click - no needed as we load the profile
sleep(1)
manageSettingsButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ez-manage-settings")))
manageSettingsButton.click()

saveSettingsButton = driver.find_element(By.ID, "ez-save-settings")
saveSettingsButton.click()

sleep(1)

bodyElem = driver.find_element(By.TAG_NAME, "body") 

while True:
# for i in range(50):
    # sleep(0.1)
    for a in range(10):
        # sleep(0.1)
        bodyElem.send_keys(Keys.DOWN)
    for b in range(10):
        # sleep(0.1)
        bodyElem.send_keys(Keys.LEFT)
    for c in range(10):
        # sleep(0.1)
        bodyElem.send_keys(Keys.UP)
    for d in range(10):
        # sleep(0.1)
        bodyElem.send_keys(Keys.RIGHT)
    # sleep(0.1)
    try: 
        gameOver = WebDriverWait(driver, 0.1).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.game-message.game-over')))
    except TimeoutException:
        # print(gameOver.type())
        continue
    else:
        break

# driver.quit()
