from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
print("sample test case started")
options = Options()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
#open Google Chrome browser
driver = webdriver.Chrome(options = options, executable_path = r"C:\Users\bhanu\PycharmProjects\SeleniumTest\Browsers\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.google.com")
driver.find_element_by_name("q").send_keys("peppapig")
time.sleep(3)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(3)
driver.close()
print("sample test sucessfully completed")
