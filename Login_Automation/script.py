
from selenium import webdriver
import yaml

conf = yaml.load(open('loginDetails.yml'))
myUserName = conf['userDetails']['Username']
myPassword = conf['userDetails']['Password']

driver = webdriver.Chrome('./chromedriver')

def login(url, userNameId, userName, passwordId, password):
    driver.get(url);
    driver.find_element_by_id(userNameId).send_keys(userName)
    driver.find_element_by_id(passwordId).send_keys(password)
    driver.find_element_by_id("submit-id-submit").click()
     

login("https://www.udemy.com/join/login-popup/", "email--1", myUserName, "id_password", myPassword)
