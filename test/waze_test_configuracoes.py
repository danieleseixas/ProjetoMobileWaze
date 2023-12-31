import unittest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import time

class TestWazePerfil(unittest.TestCase):
    def setUp(self) -> None:
        options = AppiumOptions()
        options.load_capabilities({
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:appPackage": "com.waze",
        "appium:appActivity": ".FreeMapAppActivity",
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True
        })
        self.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        self.wait = WebDriverWait(self.driver, 5)

        #Primeiros passos

        self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text=\"Continuar\"]")))
        el1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text=\"Continuar\"]")
        el1.click()
        self.wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")))
        el2 = self.driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        el2.click()
        self.wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.waze:id/authWelcomeTopButtonText")))
        el3 = self.driver.find_element(AppiumBy.ID, value="com.waze:id/authWelcomeTopButtonText")
        el3.click()
        self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@resource-id=\"com.waze:id/dialog_item_text\" and @text=\"Continuar como convidado\"]")))
        el4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id=\"com.waze:id/dialog_item_text\" and @text=\"Continuar como convidado\"]")
        el4.click()
        self.wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.waze:id/mainQuickSettings")))
        el5 = self.driver.find_element(AppiumBy.ID, "com.waze:id/mainQuickSettings")
        el5.click()
        self.wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.waze:id/hamburgerButton")))
        el6 = self.driver.find_element(AppiumBy.ID, "com.waze:id/hamburgerButton")
        el6.click()
        self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@content-desc=\"ACTION_CELL_TEXT\" and @text=\"Configurações\"]")))
        el7 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@content-desc=\"ACTION_CELL_TEXT\" and @text=\"Configurações\"]")
        el7.click()
        self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@resource-id=\"com.waze:id/settingsViewKey\" and @text=\"Postos de combustível\"]")))
        el8 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id=\"com.waze:id/settingsViewKey\" and @text=\"Postos de combustível\"]")
        el8.click()


    def tearDown(self) -> None:
        self.driver.quit()

    def test_combustivel_preferido_etanol(self):
        self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@resource-id=\"com.waze:id/settingsViewKey\" and @text=\"Combustível preferido\"]")))
        el9 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id=\"com.waze:id/settingsViewKey\" and @text=\"Combustível preferido\"]")
        el9.click()
        self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@resource-id=\"com.waze:id/title\" and @text=\"Etanol\"]")))
        el10 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id=\"com.waze:id/title\" and @text=\"Etanol\"]")
        el10.click()
        self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@resource-id=\"com.waze:id/settingsViewValue\" and @text=\"Etanol\"]")))
        result = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id=\"com.waze:id/settingsViewValue\" and @text=\"Etanol\"]")
        assert result.text=="Etanol"

    def test_posto_ordenado_preco(self):       
        self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@resource-id=\"com.waze:id/settingsViewKey\" and @text=\"Ordenar postos por\"]")))
        el9 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id=\"com.waze:id/settingsViewKey\" and @text=\"Ordenar postos por\"]")
        el9.click()
        self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@resource-id=\"com.waze:id/settingsViewKey\" and @text=\"Preço\"]")))
        el10 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id=\"com.waze:id/settingsViewKey\" and @text=\"Preço\"]")
        el10.click()
        self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@resource-id=\"com.waze:id/settingsViewValue\" and @text=\"Preço\"]")))
        result = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id=\"com.waze:id/settingsViewValue\" and @text=\"Preço\"]")
        assert result.text=="Preço"

if __name__ == '__main__':
    unittest.main()