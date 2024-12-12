import time

from  selenium import webdriver
from selenium.webdriver.chrome.service import service, Service
from selenium.webdriver.support.ui import Select

options = webdriver.ChromeOptions()
options.add_experimental_option(name="detach",value=True)
s=Service('C:\\Users\\shivram.singh_infobe\\PycharmProjects\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(options=options,service=s)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()

driver.find_element(by='xpath',value="//a[contains(text(),'Register')]").click()
driver.find_element(by='xpath', value="//input[@id='gender-male']").click()
driver.find_element('xpath',"//input[@id='FirstName']").send_keys("Alex111")
driver.find_element('xpath',"//input[@id='LastName']").send_keys("Roger111")
driver.find_element('xpath',"//input[@id='Email']").send_keys("fl94y@goeschman.com")
driver.find_element('xpath',"//input[@name='Password']").send_keys("123456")
driver.find_element('xpath',"//input[@name='ConfirmPassword']").send_keys("123456")
driver.find_element('xpath',"//input[@name='register-button']").click()
row_data=driver.find_element('xpath',"//div[@class='result']")
print("Row 1:",row_data.text)
Actual_text = row_data
assert Actual_text == row_data
driver.find_element('xpath',"//a[contains(text(),'Computers')][1]").click()
driver.find_element('xpath',"//div[@class='picture'][1]").click()
driver.find_element('xpath',"//input[@class='button-2 product-box-add-to-cart-button']").click()
time.sleep(2)
driver.find_element('xpath',"//input[@class='button-1 add-to-cart-button']").click()
time.sleep(200)
driver.quit()




