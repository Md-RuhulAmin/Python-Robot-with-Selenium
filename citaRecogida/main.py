import time
import os
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.chrome.options import Options


#PATH = r"C:\Users\ruhul\webDriver\chromedriver.exe"
driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = browser.set_window_position(-3000, 0)

#options = webdriver.ChromeOptions()
#options.add_argument("start-maximized")
#driver = webdriver.Chrome(options=options, executable_path='PATH')

driver.get('https://sede.administracionespublicas.gob.es/icpplustiem/index')
driver.find_element_by_id('cookie_action_close_header').click() #Acepting cookies

repeat = True
number = 0
wait = WebDriverWait(driver, 5)
while repeat:
    print('-------------------------------------------------')
    print('Trying number: ' + str(number))
    number += 1
    if number == 100:
        repeat = False

    drp = Select(driver.find_element_by_id('form'))
    drp.select_by_value('/icpplustiem/citar?p=28&locale=es')
    time.sleep(5)

    btn = driver.find_element_by_id('btnAceptar')
    btn.click()

    tramites = Select(driver.find_element_by_id('tramiteGrupo[0]'))
    tramites.select_by_value('4036')

    wait.until(EC.element_to_be_clickable((By.ID, 'btnAceptar'))).click()

    wait.until(EC.element_to_be_clickable((By.ID, 'btnEntrar'))).click()

    driver.find_element_by_id('txtIdCitado').send_keys('Y3109430M')
    driver.find_element_by_id('txtDesCitado').send_keys('ALAUR RAHMAN')
    wait.until(EC.element_to_be_clickable((By.ID, 'btnEnviar'))).click()

    try:
        solicitar = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "btnEnviar"))
        )
        solicitar.click()
    except:
        driver.quit()
    try:
        oficina = Select(driver.find_element_by_id('idSede'))
        sede = "CNP-Comisaría de Coslada, Guadalquivir, 16"
        sede1 = "CNP-Comisaría de Fuenlabrada, Avda. de los Ángeles, 9"
        sede2 = "CNP-Comisaría de Coslada, Guadalquivir, 16"
        sede3 = 'CNP-AVDA.POBLADOS, Avda. de los Poblados, S/N'
        sede4 = 'CNP-Comisaría de Torrejón de Ardoz, Hilados, 15'
        sede5 = 'CNP-Comisaría de Parla, Avda. Juan Carlos I, 2'
        sede6 = "CNP-Comisaría de Aranjuez, Avda. Príncipe, 40"
        sede8 = "CNP-Comisaría de Móstoles, Granada, 9"
        sede9 = "CNP-Comisaría de Collado Villalba, SAN FERNANDO, 27"
        sede10 = "CNP-Comisaría de Leganés, Avda. de Universidad, 27"
        sede7 = "CNP-Comisaría de Pozuelo de Alarcón, Camino de las Huertas, 36"

        CNP = sede3

        if CNP:
            oficina.select_by_visible_text(CNP)
            driver.find_element_by_id('btnSiguiente').click()

            print('Have found: ' + CNP)
            driver.find_element_by_id('txtTelefonoCitado').send_keys('604397369')
            driver.find_element_by_id('emailUNO').send_keys('citapreviabd26@gmail.com')
            driver.find_element_by_id('emailDOS').send_keys('citapreviabd26@gmail.com')
            driver.find_element_by_id('btnSiguiente').click()
            try:
                noCita = driver.find_element_by_xpath('//*[@id="mensajeInfo"]/p[1]/span/strong')
                info = driver.find_element_by_xpath('//*[@id="mensajeInfo"]/p[1]')
                if noCita:
                    print('There is no Cita available. Trying again.')
                    driver.find_element_by_id('btnSubmit').click()
            except:
                print('Please select time.....')
                repeat = False

    except:
        print("Searched for " + CNP +', But not found')
        driver.find_element_by_id('btnSalir').click()
