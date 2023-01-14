from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
import base64
import csv
import configparser
from random import randint

def rsleep():
    x = randint(1, 3)
    sleep(x)

config = configparser.ConfigParser()
config.read('config.ini')

un = config['login']['Username']
pw = config['login']['Password']
loginUrl = config['login']['loginUrl']
url = config['thesis']['thesisUrl']
timeout = int(config['thesis']['timeout'])

print('Thesis program started')

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

wait = WebDriverWait(driver, timeout)

driver.get(loginUrl)

username = driver.find_element(By.ID, 'ctl00_txtUsername')
username.send_keys(un)

rsleep()

password = driver.find_element(By.ID, 'ctl00_txtPassword')
password.send_keys(pw)

rsleep()

ques = driver.find_element(By.ID, 'ctl00_lblQuestion')
eq = ques.text
eqf = eq[:-1]
ans = eval(eqf)
ansbox = driver.find_element(By.ID, 'ctl00_txtCaptcha')

rsleep()

ansbox.send_keys(ans)

rsleep()

login = driver.find_element(By.ID, 'ctl00_ImageButton1')
login.click()

driver.get(url)

rsleep()

arrows = driver.find_elements(By.XPATH, '//td[1]/input')
an = len(arrows)
for i in range(0, an):
    driver.execute_script("arguments[0].scrollIntoView(true);", arrows[i])
    sleep(1)
    arrows[i].click()

rsleep()

data = []

with open('data/record.csv', 'r') as record:
    rec = csv.reader(record)
    for row in rec:
        data.append(row)

with open('data/record.csv', 'a') as addition:
    add = csv.writer(addition)
    download = driver.find_elements(By.XPATH, '//tr/td[5]/input')

    n = len(download)

    count = 0

    for i in range(0, n):
        download = driver.find_elements(By.XPATH, '//tr/td[5]/input')
        notification = driver.find_elements(By.XPATH, '//tr/td[3]')
        noti = notification[i]
        driver.execute_script("arguments[0].scrollIntoView(true);", noti)
        name = noti.text

        rsleep()

        if [name] not in data:
            driver.execute_script("arguments[0].click();", download[i])

            wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="dispatch_data"]/div/div[1]/div[2]/object/embed')))
            pdf = driver.find_element(By.XPATH, '//*[@id="dispatch_data"]/div/div[1]/div[2]/object/embed')
            src = pdf.get_attribute("src")

            rsleep()

            decodedData = base64.b64decode(src[29:])
            pdfFile = open('files/' + str(name) + '.pdf', 'wb')
            pdfFile.write(decodedData)
            pdfFile.close()
            add.writerow([name])
            rsleep()
            wait.until(ec.element_to_be_clickable((By.XPATH, '//div[1]/div/div[2]/button')))
            rsleep()
            driver.find_element(By.XPATH, '//div[1]/div/div[2]/button').click()
            rsleep()
            count += 1
            print('Notification number', name, 'downloaded')

    print(count, 'files downloaded')

print('Thesis program ended')

driver.close()