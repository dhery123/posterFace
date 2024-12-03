from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import facebook as fb 
import sys
import pyautogui

def CargarMensaje():
    

    print("Cargando mensaje")
    # Mensaje
    archivo = open("mensaje.txt", 'r', encoding='utf-8' )

    msj = archivo.read()

    archivo.close()
    return msj
def CargarImagen():
    print("Cargando imagen")
    # Mensaje
    archivo = open("img.txt", 'r')
    img = archivo.read()
    archivo.close()
    return img
def CargarGrupos():
    print("Cargando listado de grupos")
    # Lista de grupos
    archivo = open("grupos.txt", 'r')
    lg = []
    for grupo in archivo.readlines():
        lg.append(grupo)
    archivo.close()
    return lg

def CargarLogin():
    # Datos previos
    print("Carga datos del Login")
    # Cargamos el archivo
    archivo = open("datos.txt", "r")
    lineas = []
    for linea in archivo.readlines():
        lineas.append(linea)
    archivo.close()
    # Fin de uso del archivo

    return lineas
#Funcion Logear
def LogearFacebook(u,c):
    #Elementos de facebook
    try:
        time.sleep(5)
        login = driver.find_element_by_name("email")
        p = driver.find_element_by_name("pass")
        a = driver.find_element_by_xpath("//*[@value='1']")

        # Llenado de datos
        
        p.send_keys(c)
        time.sleep(5)
        login.send_keys(u)
        a.click()
         


        return True
    except:
        return False

#!pip install facebook-sdk
mensaje = CargarMensaje()
imagen = CargarImagen()

access_token = "Token"

groupfb = fb.GraphAPI(access_token)

groupfb.put_photo(open(imagen,"rb"), message = mensaje)
