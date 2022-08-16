from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(time_to_wait=100)
driver.get("https://www.udemy.com/course/selenium-with-python/learn/lecture/12805019#overview")
driver.get("https://www.youtube.com/")
driver.maximize_window()
driver.get('https://www.google.com')
driver.quit()