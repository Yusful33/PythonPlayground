from selenium import webdriver

from selenium.webdriver.chrome.options import Options

import sys

import time

login = ('ycattaneo33@gmail.com','Playball!33')

chromedriver_path = r'C:\Users\ycattaneo\Downloads\chromedriver.exe'

chrome_options = Options()

chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chromedriver_path, options=chrome_options)

driver.implicitly_wait(5)

print('\nContacting Georgia Tech...\n')

driver.get('https://www.applyweb.com/cgi-bin/ustat?app_code=gatechg')

driver.find_element_by_name('j_username').send_keys(login[0])

driver.find_element_by_name('j_password').send_keys(login[1])

driver.find_element_by_xpath(r'//button[contains("Log In", text())]').click()

driver.find_element_by_xpath(r'//a[contains("View Checklist", text())]').click()

status = driver.find_element_by_xpath('//*[@id="checkListTrigger-73607350"]/div/div/div[2]/fieldset[2]/div[2]/div/dl/dd').text

driver.implicitly_wait(5)

print("The Current Status of Your Application is: ", status)

#driver.close()
#
#
#
#if status == "To Dept For Review":
#
#    print('Your application status is still "', status, '." Keep your fingers crossed!')
#
#else:
#
#    print('Your application status is now "', status, '!"')
#    
#print(status)