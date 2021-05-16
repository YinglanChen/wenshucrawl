# Reference https://www.taodudu.cc/news/show-3444802.html

from selenium import webdriver
import time

# direct to login page
driver = webdriver.Chrome()
driver.get('https://wenshu.court.gov.cn/')
driver.maximize_window()
login_tag = driver.find_element_by_xpath('//*[@id="loginLi"]/a')
time.sleep(2)
login_tag.click()
driver.switch_to.frame("contentIframe")

# input username and password
username_path = driver.find_element_by_xpath(
    '//*[@id="root"]/div/form/div[1]//input[@class="phone-number-input"]')
password_path = driver.find_element_by_xpath(
    '//*[@id="root"]/div/form/div[1]//input[@class="password"]')
login_path = driver.find_element_by_xpath(
    '//*[@id="root"]/div/form/div[1]/div[3]/span')

time.sleep(1)
username_path.send_keys('YOUR_USERNAME') # better to setup env var
time.sleep(1)
password_path.send_keys('YOUR_PASSWORD') # better to setup env var
time.sleep(1)
login_path.click()

time.sleep(2)

# search
search_input = driver.find_element_by_xpath('//*[@id="_view_1540966814000"]//input[@class="searchKey search-inp"]')
search_button = driver.find_element_by_xpath('//*[@id="_view_1540966814000"]/div/div/div[3]')

search_input.send_keys('YOUR_SEARCH')

time.sleep(2)
search_button.click()
time.sleep(5)

# TODO find download all button, and click next page