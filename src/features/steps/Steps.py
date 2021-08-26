# -*- coding: utf-8 -*-
import pytest
import unittest
from behave import *
from selenium.webdriver.common.keys import Keys
from functions.Functions import Functions as Selenium
from functions.inicializar import Inicializar
use_step_matcher("re")

class StepsDefinitions():
    @given("open brower")
    def step_impl(self):
        Selenium.abrir_navegador(self)

    @step("DOM (.*)")
    def abrir_dom(self,jsons):
        Selenium.get_json_file(self,jsons)


    @step("escribir email (.*) texto: (.*)")
    def escribir (self,elemento,texto):
        Selenium.send_key_text(self,elemento,texto)


    @step("captura de pantalla (.*)")
    def step_impl(self,captura):
        Selenium.captura_pantalla(self,captura)


    @step("selecinar mes por texto elemento : (.*) mes (.*)")
    def step_impl(self,elemento,texto):
        Selenium.selector_text(self,elemento,texto)


    @step("select value (.*) y (.*)")
    def step_impl(self,elemetos,value):
        Selenium.espera_el_elemento(self,elemetos)
        Selenium.get_select_element(self,elemetos).select_by_value(value)


    @step("guardar ventana : (.*)")
    def step_impl(selt,name):
        Selenium.switch_to_windows_name(selt,name)


    @step("ir a otra ventana url : (.*)")
    def step_impl(self,url):
        Selenium.new_window(self,url)
