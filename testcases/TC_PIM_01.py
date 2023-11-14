import time

from selenium import webdriver
import pytest
from PageObjects.Forgot_password import Forgot_password
from Utilities.customlogger import LogGen
from Utilities.ReadProperties import ReadConfig


class Test_reset_password:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()  # Logger Code

    def test_resetpwd(self,setup):
        self.logger.info("*********************** Test_reset_password *************************************")
        self.logger.info("*********************** Verifying Login Page *************************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.lp = Forgot_password(self.driver)
        self.lp.clickForgotPassword()
        time.sleep(5)
        self.lp.setUserName(self.username)
        time.sleep(5)
        self.lp.clickResetPassword()
        time.sleep(5)
        self.lp.getSuccessMessage()
        self.logger.info("*********************** Password Reset Successfully **********************************")
        self.driver.close()
