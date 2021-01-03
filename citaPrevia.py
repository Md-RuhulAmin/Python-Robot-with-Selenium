import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://sede.administracionespublicas.gob.es/icpplustiem/index')
driver.find_element_by_id('cookie_action_close_header').click() #Acepting cookies

repeat = True
number = 0
wait = WebDriverWait(driver, 10)
while repeat:
    print('-------------------------------------------------')
    print('Trying number: ' + str(number))
    number += 1
    if number == 100:
        repeat = False