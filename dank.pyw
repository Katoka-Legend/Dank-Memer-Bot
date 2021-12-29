
import scheduler
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.remote_connection import ChromeRemoteConnection
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver import ChromeOptions
from selenium.common import exceptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.common.by import By
import time
import datetime
import psutil 
import tkinter as tk
import schedule



def get_driver(op):
    print("get_driver()")
    options = Options()
    driver_path = "F:/ADVAITH/CODING/PYTHON/Application Python 3.9.6/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe"
    user_data_dir = "F:\ADVAITH\CODING\PYTHON\Activities\Bots\Dank Chrome User Data 1"
    profile_directory = "Profile 8"
    if op == True:
        options.add_argument("--headless")
    options.add_argument("--user-data-dir={}".format(user_data_dir))
    options.add_argument("--profile-directory={}".format(profile_directory))
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    # options.add_argument("--window-position=-2920,1080")
    driver = webdriver.Chrome(executable_path=driver_path,options=options)
    # driver.set_window_size(1440, 900)
    return driver


def login(driver):
    try:
        # print("here")
        time.sleep(5)
        email_ele = driver.find_element_by_name("email")
        email_ele.click()
        time.sleep(1)
        email_ele.send_keys(Keys.DELETE)
        email_ele.send_keys("advaithm.nair@gmail.com",Keys.ENTER)
        password_ele = driver.find_element_by_name("password")
        password_ele.click()
        time.sleep(2)
        password_ele.send_keys(Keys.DELETE)
        password_ele.send_keys("AdvaitH123",Keys.ENTER)
        # sub_btn = driver.find_elements_by_class_name("marginBottom8-AtZOdT")[1]
        # sub_btn.click()
        time.sleep(5)
    except Exception as error:
        print(f"Failed to login because {error}")



def dig(driver):
        print("Digging")
        textboxel = driver.find_element_by_class_name("textArea-12jD-V")
        textboxel.click()
        time.sleep(2)
        textbox = driver.find_element_by_xpath("//div[@data-slate-object='block']")
        textbox.send_keys("pls dig",Keys.ENTER)

def beg(driver):
        print("Begging")
        textboxel = driver.find_element_by_class_name("textArea-12jD-V")
        textboxel.click()
        time.sleep(2)
        textbox = driver.find_element_by_xpath("//div[@data-slate-object='block']")
        textbox.send_keys("pls beg",Keys.ENTER)
def deposit(driver):
        print("Depositing")
        textboxel = driver.find_element_by_class_name("textArea-12jD-V")
        textboxel.click()
        time.sleep(2)
        textbox = driver.find_element_by_xpath("//div[@data-slate-object='block']")
        textbox.send_keys("pls deposit all",Keys.ENTER)


def sell(driver):
    print("Selling")
    textboxel = driver.find_element_by_class_name("textArea-12jD-V")
    textboxel.click()
    time.sleep(2)
    textbox = driver.find_element_by_xpath("//div[@data-slate-object='block']")
    textbox.send_keys("pls inv",Keys.ENTER)
    time.sleep(5)
    filter_element = driver.find_elements_by_xpath("//div[@class='select-2fjwPw select-z0PgeK lookFilled-22uAsw'][1]")[-1]
    filter_element.click()
    time.sleep(1)
    filter_options =   driver.find_elements_by_xpath("//div[@class='option-3KoAJB selectOption-46tNpR']//div//div//strong")
    findex = 0
    for filter_option in filter_options :
        if filter_option.text == "Sellable":
            break
        findex+=1
    sellable_element = driver.find_elements_by_xpath("//div[@class='option-3KoAJB selectOption-46tNpR']")[findex]
    sellable_element.click()
    time.sleep(1)
    sellable_content = driver.find_elements_by_xpath("(//div[@class='grid-1nZz7S'][1]//div[4])")[-1].text
    # print(sellable_content)   
    sell_data = []
    sell_commands = []
    for sell_content in sellable_content.split("\n"):
        for sellables in sell_content.split("─"):
            if sellables != "" and sellables !=' Sellable':
                sell_data.append(sellables)
    print(sell_data)
    for i in range(0,len(sell_data),3):
        sell_item = sell_data[i+2].split(" ")[1]
        num = sell_data[i+1]
        sell_commands.append(f"pls sell {sell_item} {num}")
    textboxel = driver.find_element_by_class_name("textArea-12jD-V")
    textboxel.click()
    for sell_command in sell_commands:
        textbox = driver.find_element_by_xpath("//div[@data-slate-object='block']")
        textbox.send_keys(sell_command,Keys.ENTER)
        print(sell_command)
        time.sleep(5)

def search(driver):
    print("Searching")
    textboxel = driver.find_element_by_class_name("textArea-12jD-V")
    textboxel.click()
    time.sleep(2)
    textbox = driver.find_element_by_xpath("//div[@data-slate-object='block']")
    textbox.send_keys("pls search",Keys.ENTER)
    time.sleep(2)
    search_options_element = driver.find_elements_by_xpath("//button[@class='component-1IAYeC button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeSmall-2cSMqn grow-q77ONN']")[-1]
    search_options_element.click()    

driver = get_driver(op = True)
try:
    driver.get("https://discord.com/channels/739424193715896350/917061652585799681")
except Exception as error:
    print(f"Error :- \n {error}")


login(driver)

# beg(driver)

schedule.every(40).seconds.do(lambda : beg(driver))
schedule.every(40).seconds.do(lambda : dig(driver))
schedule.every(1).minutes.do(lambda : deposit(driver))
schedule.every(10).minutes.do(lambda : sell(driver))
schedule.every(30).seconds.do(lambda : search(driver))

while True:
    try:
        schedule.run_pending()
        time.sleep(10)
    except Exception as Error:
        print(f"Error :----- \n {Error}")
        driver.quit()
        driver.close()
        driver = get_driver(op = True)
        driver.get("https://discord.com/channels/739424193715896350/917061652585799681")
        login(driver)
        time.sleep(10)
        pass  



