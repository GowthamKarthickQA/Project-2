import time

from selenium import webdriver
import pytest
from PageObjects.Forgot_password import Forgot_password
from Utilities.customlogger import LogGen
from Utilities.ReadProperties import ReadConfig


class Test_reset_password:
    
    baseURL = ReadConfig.getApplicationURL() # get baseURL from readproperties.py
    username = ReadConfig.getUsername() # get username from readproperties.py
    password = ReadConfig.getPassword() # get password from readproperties.py
    invalid_username_2 = ReadConfig.getInvalidUsername2() # get invalid_username_2 from readproperties.py

    logger = LogGen.loggen()  # Logger Code

    def test_resetpwd(self,setup):
        self.logger.info("*********************** POSITIVE TESTCASES *************************************")
        self.logger.info("*********************** Test_reset_password *************************************")
        self.logger.info("*********************** Entering Valid Username *************************************")
        self.driver = setup    # initialize the chrome driver
        self.driver.get(self.baseURL)  # get URL
        self.driver.implicitly_wait(5)
        self.driver.maximize_window() # maximize window
        self.lp = Forgot_password(self.driver)
        self.lp.clickForgotPassword() # Click Forgot password button
        time.sleep(5)
        self.lp.setUserName(self.username) # Clear username text if exist and enter valid username
        time.sleep(5)
        self.lp.clickResetPassword() # Click Reset password button
        time.sleep(5)
        self.lp.getSuccessMessage() # get password successfully message
        self.logger.info("*********************** Password Reset Successfully **********************************")
        self.driver.close()

    def test_resetpwd_1(self, setup):
        self.logger.info("*********************** NEGATIVE TESTCASES *************************************")
        self.logger.info("*********************** Test_reset_password_1 *************************************")
        self.logger.info("*********************** Entering Invalid Username *************************************")
        self.driver = setup # initialize the chrome driver
        self.driver.get(self.baseURL) # get URL
        self.driver.implicitly_wait(5)
        self.driver.maximize_window() # maximize window
        self.lp = Forgot_password(self.driver)
        self.lp.clickForgotPassword() # Click Forgot password button
        time.sleep(5)
        self.lp.setInvalidUserName(self.invalid_username_2) # Clear username text if exist and enter invalid username
        time.sleep(5)
        self.lp.clickResetPassword() # Click Reset password button
        time.sleep(5)
        self.lp.getSuccessMessage() # get password successfully message
        self.logger.info("*********************** Invalid Username Executed Successfully **********************************")
        self.driver.close()

