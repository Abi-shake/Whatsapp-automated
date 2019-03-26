
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Paste the path of chromedriver below where it says 'Your Path'
driver = webdriver.Chrome('Your Path')
driver.get('http://web.whatsapp.com')
wait = WebDriverWait(driver, 600)

#taking inputs from user

name = input('Enter the name of user or group : ')
msg = input('Enter the message : ')
count = int(input('Enter the count : '))

#Scan the code before proceeding further
input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

#providing the input xpath of text-box

inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))

#looping for the desired number of times

for i in range(count):
    input_box.send_keys(msg + Keys.ENTER)
    time.sleep(1)

input_box.send_keys('Closing the connection' + Keys.ENTER)
driver.quit()
