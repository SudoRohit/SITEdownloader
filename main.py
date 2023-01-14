from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
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
url = config['result']['resultUrl']
session = config['result']['session']
timeout = int(config['result']['timeout'])

print('Result program started')

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

select = Select(driver.find_element(By.ID, 'DDLSession'))
select.select_by_visible_text(session)

sleep(2)

wait.until(ec.element_to_be_clickable((By.ID, 'ctl00_ContentPlaceHolder1_RadGrid2_ctl00__2__0')))

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

with open('data/'+session+'.csv', 'a') as ses:
    ses = csv.writer(ses)

    with open('data/record.csv', 'a') as addition:
        add = csv.writer(addition)
        download = driver.find_elements(By.XPATH, '//td[9]/input')

        n = len(download)

        count = 0

        for i in range(0, n):
            download = driver.find_elements(By.XPATH, '//td[9]/input')
            notification = driver.find_elements(By.XPATH, '//td[7]')
            branch = driver.find_elements(By.XPATH, '//td[3]')
            semester = driver.find_elements(By.XPATH, '//td[4]')
            scheme = driver.find_elements(By.XPATH, '//td[5]')
            rtype = driver.find_elements(By.XPATH, '//td[6]')
            udate = driver.find_elements(By.XPATH, '//td[8]')
            noti = notification[i]
            driver.execute_script("arguments[0].scrollIntoView(true);", noti)
            br = branch[i].text
            name = noti.text
            sem = semester[i].text
            sch = scheme[i].text
            rt = rtype[i].text
            ud = udate[i].text

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
                ses.writerow([session, br, sem, sch, rt, name, ud])
                rsleep()
                wait.until(ec.element_to_be_clickable((By.XPATH, '//div[1]/div/div[2]/button')))
                rsleep()
                driver.find_element(By.XPATH, '//div[1]/div/div[2]/button').click()
                rsleep()
                count += 1
                print('Notification number', name, 'downloaded')

        print(count, 'files downloaded')

print('Result program ended')

driver.close()