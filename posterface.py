
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time


def CargarMensaje():
    print("Cargando mensaje")
    # Mensaje
    archivo = open("mensaje.txt", 'r', encoding="utf8")
    msj = archivo.read()
    archivo.close()
    return msj



def CargarGrupos():
    print("Cargando listado de grupos")
    # Lista de grupos
    archivo = open("grupos.txt", 'r')
    lg = []
    for grupo in archivo.readlines():
        lg.append(grupo)
    archivo.close()
    return lg

#def CargarImagen():
#    usi = int(input('''
#        Ingrese una opcion
#        0. No usar imagen
#        1. Usar imagen
#    '''))
#    while (usi != 1 and usi != 0):
#       print("Opcion incorrecta, vuelva a intentar")
#        usi = int(input('''
#            Ingrese una opcion
#            0. No usar imagen
#            1. Usar imagen
#        '''))
#    return usi

def CargarDireImagen():
    
    print("Cargando direccion de la imagen")
        # Imagen
    imagen = os.path.join(os.getcwd(), "image.png")
   
    return imagen

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

##########
#Navegador
##########

#usar_imagen = CargarImagen()

#Configuracion
PATH= "C:\Program Files (x86)\chromedriver.exe"
options=webdriver.ChromeOptions()

options.add_argument("disable-gpu")
options.add_argument("no-sandbox")

prefs = {  
    'profile.default_content_setting_values' :  {  
        'notifications' : 2  
     }  
}  
options.add_experimental_option('prefs',prefs)


driver = webdriver.Chrome(PATH,chrome_options=options)
driver.get("https://facebook.com/")

driver.maximize_window()


mensaje = CargarMensaje()
print (mensaje)

lista_grupos = CargarGrupos()

imagen = CargarDireImagen()
datos_login = CargarLogin()
print(datos_login)
time.sleep(4)

usuario = datos_login[0]
contra = datos_login[1]

print("la contraseña es:"+contra)




#Logear
#Recorrido de grupos
i = 1
cantidad_lograda = 0
for grupo in lista_grupos:
    driver.get(grupo)
    time.sleep(2)
    try:
        print("Entrando al grupo " + str(i) + ". Link: " + grupo)
        
        LogearFacebook(usuario,contra)
        time.sleep(4)
        print("Realizando posteo")

        
        p = driver.find_element_by_xpath("//*[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7']")
        print("Enviando mensaje")
        p.click()
        time.sleep(4)
        print("Enviando imagen")
        #img = browser.find_element_by_xpath("//input[@class='k4urcfbm bixrwtb6 datstx6m']")
        img = driver.find_element_by_xpath("//input[@class='rpm2j7zs k7i0oixp gvuykj2m ni8dbmo4 du4w35lb q5bimw55 ofs802cu pohlnb88 dkue75c7 mb9wzai9 l56l04vs r57mb794 l9j0dhe7 kh7kg01d eg9m0zos c3g1iek1 j83agx80 cbu4d94t buofh1pr']")

        
        img.send_keys(imagen)
        #
        time.sleep(5)
        #Ubicar la caja de posteo
        p = driver.find_element_by_xpath("//*[@class='notranslate _5rpu']")
        print("Enviando mensaje")
        p.click()
       

        time.sleep(1)
        m = driver.find_element_by_xpath("//*[@class='_1mf _1mj']")
        m.send_keys(mensaje)


      
        time.sleep(5)
        #Ubicar la caja de posteo
        p = driver.find_element_by_xpath("//*[@class='notranslate _5rpu']")
        print("Enviando mensaje")
        p.click()
       
        time.sleep(3)
        m = driver.find_element_by_xpath("//*[@class='notranslate _5rpu']")
        m.send_keys(mensaje)




    except:
        print("Ocurrio un error con el grupo " + str(i) + ". Link: " + grupo)
    i += 1
print("Se logró publicar en " + str(cantidad_lograda) + "/" + str(len(lista_grupos)) + " grupos.")
print("Proceso finalizado")


