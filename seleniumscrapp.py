from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def obtener_datos_copias():
    # Configura el controlador del navegador
    driver = webdriver.Chrome()

    url = "http://192.168.0.199:8000/"
    driver.get(url)

    # Esperar a que se cargue la página y se genere el contenido dinámico de JS
    driver.implicitly_wait(10)

    #Hacemos click en el primer enlace
    driver.find_element(By.LINK_TEXT, 'Monitor estado/Cancelar').click()

    #Buscamos formas de identificar los siguientes enlaces para navegar en la pagina y hacemos click en ellos
    try:
        element = WebDriverWait(driver,15).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'Comprobación de contadores'))
        )
        element.click()

        element = WebDriverWait(driver,15).until(
            EC.presence_of_element_located((By.ID, 'contentHeadingTools'))
        )

        #con esta linea comenzamos a aplicar el html parser :)
        contenidohtml = driver.page_source
       # driver.find_element(By.ID, 'tmpUpdate')
       # tmpUpdate
        
    #cerramos el driver del navegador
    finally:
        driver.quit()


    # Utilizamos BeautifulSoup para analizar el contenido HTML
    soup = BeautifulSoup(contenidohtml, 'html.parser')

    # Ahora puedes buscar el tbody y las filas dentro del contenido generado dinámicamente
    div0 = soup.find('div', id='mainCounterInformationModule').find('tbody').find_all('tr')
    #   print(div[0].find_all('td')[0].get_text()) asi se visualiza el contendio de la tabla de elemxeleme

    total2 = []
    total1 = []
    for file in div0:
        total2.append(file.find_all('td')[0].get_text())
        total1.append(file.find_all('td')[1].get_text())
        """
        celdas = file.find_all('td')
        for celda in celdas:
            print(celda.get_text())
        """
    # Convertir las listas a cadenas y unir los elementos con el método join()
   # total1_str = '\n'.join(total1)
   # total2_str = '\n'.join(total2)

    #print('El total 1 es:\n' + total1_str)
    #print('El total 2 es:\n' + total2_str)

    df1 = pd.DataFrame({"Tipo":total2,
                       "Num. de copias":total1,
                      })

    #df.to_csv('papel.csv')
    



    date = soup.find('div', id='tmpUpdate').get_text()
    div = soup.find('div', id='sendCounterInformationModule').find('tbody').find_all('tr')
    #   print(div[0].find_all('td')[0].get_text()) asi se visualiza el contendio de la tabla de elemxeleme
    tipo =[]
    numcopias = []
    for file in div:
        """
        celdas = file.find_all('td')
        for celda in celdas:
            print(celda.get_text())
        """

        tipo.append(file.find_all('td')[0].get_text())
        numcopias.append(file.find_all('td')[1].get_text())
    df2 = pd.DataFrame({
        "Tipo": tipo,
        "Numcopias":numcopias
    })

    df_final = pd.concat([df1, df2], ignore_index=True)
    #df_final.to_csv('papel.csv', index=False)
    with pd.ExcelWriter('data.xlsx', engine='xlsxwriter') as writer:
        df_final.to_excel(writer, sheet_name='Sheet1', index=False)
        #Obtener el objeto Workbook y la hoja Sheet1
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']
        #Agregar la variable date como una celda en la hoja Excel
        worksheet.write('D1', 'Fecha:')
        worksheet.write('E1', date)
   
obtener_datos_copias()







