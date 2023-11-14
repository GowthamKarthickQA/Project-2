import time
from selenium import webdriver
import pytest
from PageObjects.MainMenu_Validation import Mainmenu_Validation
from Utilities.customlogger import LogGen
from Utilities.ReadProperties import ReadConfig


class Test_Mainmenu_Validation:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()  # Logger Code

    def test_login(self,setup):
        self.logger.info("*********************** Test_001_Login *************************************")
        self.logger.info("*********************** Verifying Login Page *************************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.lp = Mainmenu_Validation(self.driver)
        self.lp.setUsername(self.username)
        time.sleep(5)
        self.lp.setPassword(self.password)
        time.sleep(5)
        self.lp.clickLogin()
        time.sleep(5)
        self.lp.getMainmenu()
        self.logger.info("*********************** Login Sucessfully *************************************")
        self.driver.close()
