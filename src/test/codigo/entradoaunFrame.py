import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import Select
class Test_005(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # espera implicita
        self.driver.implicitly_wait(5)

        self.driver.maximize_window()
        self.driver.get("https://chercher.tech/practice/frames-example-selenium-webdriver")

    def test_frame(self):
        self.main_title = self.driver.find_element(By.XPATH,"//body/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]")
        print(self.main_title.text)





        #frame1
        self.frameUno = self.driver.find_element_by_xpath("//iframe[@id='frame1']")
        self.driver.switch_to_frame(self.frameUno)
        #cojade texto
        self.cajatx = self.driver.find_element_by_xpath("//body/input[1]")
        self.cajatx.send_keys("hola")

        #entrando frame3
        self.frameTres = self.driver.find_element_by_xpath("//iframe[@id='frame3']")
        self.driver.switch_to_frame(self.frameTres)
        self.check = self.driver.find_element_by_xpath("//input[@id='a']")
        self.check.click()

        # saliendo de los frames
        self.driver.switch_to.parent_frame()#saliendo del frame 3
        self.driver.switch_to.parent_frame()#saliendo del frame 1
        time.sleep(3)


        # frame2
        self.frameDos = self.driver.find_element_by_xpath("//iframe[@id='frame2']")
        self.driver.switch_to_frame(self.frameDos)
        self.selectors = Select(self.driver.find_element_by_xpath("//select[@id='animals']"))
        self.selectors.select_by_visible_text("Avatar")
        time.sleep(3)






    def tearDown(self):
     self.driver.quit()


if __name__ == '__main__':
    unittest.main()
