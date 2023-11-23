import time
from selenium import webdriver
import pytest
from PageObjects.MainMenu_Validation import Mainmenu_Validation
from Utilities.customlogger import LogGen
from Utilities.ReadProperties import ReadConfig


class Test_Mainmenu_Validation:

    # Reading login credetials, URl from readproperties.py

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()  # Logger Code

    def test_login(self,setup):
        self.logger.info("*********************** Test_001_Login *************************************")
        self.logger.info("*********************** Verifying Login Page *************************************")
        self.driver = setup # Initialize chrome driver
        self.driver.get(self.baseURL) # get URL
        self.driver.implicitly_wait(5)
        self.driver.maximize_window() # Maximize window
        self.lp = Mainmenu_Validation(self.driver)
        self.lp.setUsername(self.username) # clear and enter valid username
        time.sleep(5)
        self.lp.setPassword(self.password) # clear and enter valid passsword
        time.sleep(5)
        self.lp.clickLogin() # click Login button
        time.sleep(5)
        self.lp.getMainmenu() # validating mainmenu on side pane is displaying or not
        self.logger.info("*********************** Login Sucessfully *************************************")
        self.driver.close()
