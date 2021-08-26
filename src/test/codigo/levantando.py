from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from src.functions.Functions import Functions as Selenium
#OJO el driver esta en enviroment/scripts
from src.functions.inicializar import Inicializar

driver = webdriver.Chrome(Inicializar.basedir + "\\drivers\\chromedriver.exe")


#si lo quieres ejecutar sacalo de aqui
driver.get("https://www.udemy.com/course/flask-framework-complete-course-for-beginners/?ranMID=39197&ranEAID=sIt9MIeGnaM&ranSiteID=sIt9MIeGnaM-wUPhqwZGQVf4R4SX7sr2sQ&LSNPUBID=sIt9MIeGnaM&utm_source=aff-campaign&utm_medium=udemyads&couponCode=70F4B5FDFF2D8499E285")

driver.back()
driver.refresh()





assert "Google" in driver.title
elem = driver.find_element_by_xpath('//*[@id="es"]/div[2]/div[3]/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div[1]/span[2]').text
elem.clear()
#elem.send_keys("pycon") = eso lo que hace es escribir en el entry que le pasamos
elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN) = este aun lo tengo muy claro pero creo que hace una enpecie
#de ENTER
elem.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source



