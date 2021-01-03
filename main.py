import time
import os
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.chrome.options import Options


PATH = r'E:\python 2020\chromedriver.exe'
driver = webdriver.Chrome(PATH)

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

    drp = Select(driver.find_element_by_id('form'))
    drp.select_by_value('/icpplustiem/citar?p=28&locale=es')

    btn = driver.find_element_by_id('btnAceptar')
    btn.click()

    tramites = Select(driver.find_element_by_id('tramiteGrupo[0]'))
    tramites.select_by_value('4010')

    wait.until(EC.element_to_be_clickable((By.ID, 'btnAceptar'))).click()

    wait.until(EC.element_to_be_clickable((By.ID, 'btnEntrar'))).click()

    driver.find_element_by_id('txtIdCitado').send_keys('Y7041009X')
    driver.find_element_by_id('txtDesCitado').send_keys('MOHAMMED YEASIN')
    Select(driver.find_element_by_id('txtPaisNac')).select_by_value('432')
    wait.until(EC.element_to_be_clickable((By.ID, 'btnEnviar'))).click()

    try:
        try:
            solicitar = WebDriverWait(driver, 10).until(
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
            sede11 = "CNP-Comisaría de Rivas-Vaciamadrid, José Hierro, 82"
            sede12 = "CNP-Comisaría de Alcorcón, Alfredo Nobel, 10"

            selection = (sede, sede3, sede6, sede1, sede2, sede5, sede7, sede8, sede9 )
            CNP = ""
            for s in selection:
                try:
                    oficina.select_by_visible_text(s)
                    CNP = s
                    break
                except:
                    print('Not found: '+ s)

            if CNP:
                print('Serching for: ' + CNP)
                time.sleep(2)
                oficina.select_by_visible_text(CNP)
                driver.find_element_by_id('btnSiguiente').click()

                driver.find_element_by_id('txtTelefonoCitado').send_keys('604397369')
                driver.find_element_by_id('emailUNO').send_keys('citapreviabd26@gmail.com')
                driver.find_element_by_id('emailDOS').send_keys('citapreviabd26@gmail.com')
                driver.find_element_by_id('btnSiguiente').click()

                try:
                    noCita = driver.find_element_by_xpath('//*[@id="mensajeInfo"]/p[1]/span/b')
                    if noCita:
                        print('There is no Cita available. Try again later.')
                        time.sleep(2)
                        driver.find_element_by_id('btnSubmit').click()
                except:
                    print('Please select time.....')
                    repeat = False
            else:
                print("Información: En este momento no hay oficinas disponibles")
                driver.find_element_by_id('btnSubmit').click()
        except:
            print("Searched for " + CNP +', But try again')
            driver.find_element_by_id('btnSalir').click()
    except:
        driver.find_element_by_id('btnSalir').click()
        print("There no oficinas disponible")