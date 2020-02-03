from selenium import webdriver
from getpass import getpass

#usr = input("Email or Phone: ")
#psswd = getpass("Password: ")

usr = "Your account user name"
psswd = "Your account password"

driver = webdriver.Chrome(executable_path="chromedriver")
driver.get("https://www.facebook.com/")

username_box = driver.find_element_by_id("email")
username_box.send_keys(usr)

password_box = driver.find_element_by_id("pass")
password_box.send_keys(psswd)

btn = driver.find_element_by_id("u_0_4")
btn.submit()