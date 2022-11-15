from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
import time

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

wait = WebDriverWait(driver, 20)

driver.get('https://SITE.com/')

username = driver.find_element(By.ID, 'ctl00_txtUsername')
username.send_keys("")

password = driver.find_element(By.ID, 'ctl00_txtPassword')
password.send_keys("")

ques = driver.find_element(By.ID, '//*[@id="ctl00_lblQuestion"]')
eq = ques.text
ans = eval(eq)
ansbox = driver.find_element(By.ID, '//*[@id="ctl00_txtCaptcha"]')
ansbox.send_keys(ans)

login = driver.find_element(By.ID, 'ctl00_ImageButton1')
login.click()

wait.until(ec.url_changes("https://SITE.com/Account/Default.aspx"))
driver.get('https://SITE.com/Institution/OnlineTabulationByCollege.aspx')

wait.until(ec.element_to_be_clickable((By.XPATH, 'DDLSession')))
select = Select(driver.find_element(By.ID, 'DDLSession'))
select.select_by_value("32")

wait.until(ec.element_to_be_clickable((By.ID, 'ctl00_ContentPlaceHolder1_RadGrid2_ctl00__2__0'))).click()
time.sleep(1)
download = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_RadGrid2_ctl00_ctl05_btnDownload')
download.click()

time.sleep(10)
driver.find_element(By.XPATH, '//*[@id="icon"]/iron-icon')
