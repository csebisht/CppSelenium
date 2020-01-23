from selenium.webdriver.chrome.options import Options
from selenium import webdriver
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
#driver = webdriver.Chrome('C://Users/pradeep/Documents/chromedriver_win32/chromedriver.exe', options= options)
driver = webdriver.Chrome('C://Users/pradeep/Documents/chromedriver_win32/chromedriver.exe')
driver.get('http://cpp-sprint.s3-website-us-east-1.amazonaws.com/')
print(driver)