# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestUntitled():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_untitled(self):
    self.driver.get("http://localhost:53922/Login/Index")
    self.driver.set_window_size(1060, 904)
    self.driver.find_element(By.NAME, "correo").click()
    self.driver.find_element(By.NAME, "correo").send_keys("incorrecto@gmail.com")
    self.driver.find_element(By.NAME, "clave").click()
    self.driver.find_element(By.NAME, "clave").send_keys("123")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.NAME, "correo").click()
    self.driver.find_element(By.NAME, "correo").send_keys("joserivas@gmail.com")
    self.driver.find_element(By.NAME, "clave").click()
    self.driver.find_element(By.NAME, "clave").send_keys("jose777")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.LINK_TEXT, "Personas").click()
    self.driver.find_element(By.LINK_TEXT, "Usuarios").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    self.driver.find_element(By.ID, "txtnombre").click()
    self.driver.find_element(By.ID, "txtnombre").send_keys("qwerty")
    self.driver.find_element(By.ID, "txtapellido").click()
    self.driver.find_element(By.ID, "txtapellido").send_keys("qwerty")
    self.driver.find_element(By.ID, "txtcorreo").click()
    self.driver.find_element(By.ID, "txtcorreo").send_keys("qwerty@gmail.com")
    self.driver.find_element(By.ID, "txtclave").click()
    self.driver.find_element(By.ID, "txtclave").send_keys("123")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary:nth-child(2)").click()
    self.driver.find_element(By.LINK_TEXT, "Personas").click()
    self.driver.find_element(By.LINK_TEXT, "Lectores").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    self.driver.find_element(By.ID, "txtnombre").click()
    self.driver.find_element(By.ID, "txtnombre").send_keys("asdf")
    self.driver.find_element(By.ID, "txtapellido").click()
    self.driver.find_element(By.ID, "txtapellido").send_keys("asdf")
    self.driver.find_element(By.ID, "txtcorreo").click()
    self.driver.find_element(By.ID, "txtcorreo").send_keys("asdf@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary:nth-child(2)").click()
    self.driver.find_element(By.LINK_TEXT, "Biblioteca").click()
    self.driver.find_element(By.LINK_TEXT, "Categoria").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    self.driver.find_element(By.ID, "txtdescripcion").click()
    self.driver.find_element(By.ID, "txtdescripcion").send_keys("zxc")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary:nth-child(2)").click()
    self.driver.find_element(By.LINK_TEXT, "Biblioteca").click()
    self.driver.find_element(By.LINK_TEXT, "Editorial").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    self.driver.find_element(By.ID, "txtdescripcion").click()
    self.driver.find_element(By.ID, "txtdescripcion").send_keys("zxccv")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary:nth-child(2)").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.LINK_TEXT, "Biblioteca").click()
    self.driver.find_element(By.LINK_TEXT, "Autores").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    self.driver.find_element(By.ID, "txtdescripcion").click()
    self.driver.find_element(By.ID, "txtdescripcion").send_keys("fghj")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary:nth-child(2)").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.LINK_TEXT, "Biblioteca").click()
    self.driver.find_element(By.LINK_TEXT, "Prestamos").click()
    self.driver.find_element(By.LINK_TEXT, "Consultar").click()
    self.driver.find_element(By.ID, "cboestadoprestamo").click()
    dropdown = self.driver.find_element(By.ID, "cboestadoprestamo")
    dropdown.find_element(By.XPATH, "//option[. = 'Pendiente']").click()
    self.driver.find_element(By.ID, "btnbuscar").click()
    self.driver.find_element(By.ID, "cboestadoprestamo").click()
    dropdown = self.driver.find_element(By.ID, "cboestadoprestamo")
    dropdown.find_element(By.XPATH, "//option[. = 'Devuelto']").click()
    self.driver.find_element(By.ID, "btnbuscar").click()
    element = self.driver.find_element(By.ID, "btnbuscar")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.LINK_TEXT, "Personas").click()
    self.driver.find_element(By.LINK_TEXT, "Usuarios").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(3) span:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".fa-user-shield").click()
    self.driver.find_element(By.LINK_TEXT, "Salir").click()
  