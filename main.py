from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from time import sleep
import base64
import csv

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

wait = WebDriverWait(driver, 25)

driver.get('https://SITE.com/')

username = driver.find_element(By.ID, 'ctl00_txtUsername')
username.send_keys("")

sleep(1)

password = driver.find_element(By.ID, 'ctl00_txtPassword')
password.send_keys("")

sleep(1)

ques = driver.find_element(By.ID, 'ctl00_lblQuestion')
eq = ques.text
eqf = eq[:-1]
ans = eval(eqf)
ansbox = driver.find_element(By.ID, 'ctl00_txtCaptcha')

sleep(1)

ansbox.send_keys(ans)

sleep(1)

login = driver.find_element(By.ID, 'ctl00_ImageButton1')
login.click()

driver.get('https://SITE.com/Institution/OnlineTabulationByCollege.aspx')

select = Select(driver.find_element(By.ID, 'DDLSession'))
select.select_by_value("32")

wait.until(ec.element_to_be_clickable((By.ID, 'ctl00_ContentPlaceHolder1_RadGrid2_ctl00__2__0')))

arrows = driver.find_elements(By.XPATH, '//td[1]/input')

data = []

with open('data/record.csv', 'r') as record:
    rec = csv.reader(record)
    for row in rec:
        data.append(row[0])

with open('data/record.csv', 'a') as addition:
    add = csv.writer(addition)

    for arrow in arrows:
        wait.until(ec.element_to_be_clickable(arrow)).click()
        download = driver.find_elements(By.XPATH, '//td[9]/input')
        notification = driver.find_elements(By.XPATH, '//td[7]')
        n = len(download)
        for i in range(0, n):
            name = notification[i].text

            if name not in data:
                download[i].click()

                wait.until(ec.presence_of_element_located(
                    (By.XPATH, '//*[@id="dispatch_data"]/div/div[1]/div[2]/object/embed')))
                pdf = driver.find_element(By.XPATH, '//*[@id="dispatch_data"]/div/div[1]/div[2]/object/embed')
                src = pdf.get_attribute("src")

                decodedData = base64.b64decode(src[29:])
                pdfFile = open('files/' + str(name) + '.pdf', 'wb')
                pdfFile.write(decodedData)
                pdfFile.close()
                add.writerow(name)

            arrow.click()
