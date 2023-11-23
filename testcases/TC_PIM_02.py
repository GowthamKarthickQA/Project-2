import time
from selenium import webdriver
import pytest
from PageObjects.Header_Validation import Header_Validation
from Utilities.customlogger import LogGen
from Utilities.ReadProperties import ReadConfig


class Test_Header_Validation:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    valid_username = ReadConfig.getValidUsername()
    invalid_password = ReadConfig.getInvalidPassword()
    invalid_username_2 = ReadConfig.getInvalidUsername2()
    valid_password_2 = ReadConfig.getValidPassword2()
    invalid_username_3 = ReadConfig.getInvalidUsername3()
    invalid_password_3 = ReadConfig.getInvalidPassword3()

    logger = LogGen.loggen()  # Logger Code


    ###################################### NEGATIVE TESTCASES  ##############################################
    def test_login1(self, setup):
        self.logger.info("*********************** NEGATIVE TESTCASES - 1 *************************************")
        self.logger.info("*********************** Verifying Invalid Login Page *************************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.lp = Header_Validation(self.driver)
        self.lp.setValidUsername(self.valid_username)
        time.sleep(5)
        self.lp.setInvalidPassword(self.invalid_password)
        time.sleep(5)
        self.lp.clickLogin()
        time.sleep(5)
        self.logger.info("*********************** Negative cases executed Sucessfully *************************************")
        self.driver.close()

    def test_login2(self, setup):
        self.logger.info("*********************** NEGATIVE TESTCASES - 2 *************************************")
        self.logger.info("*********************** Verifying Invalid Login Page *************************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.lp = Header_Validation(self.driver)
        self.lp.setInvalidUsername2(self.invalid_username_2)
        time.sleep(5)
        self.lp.setValidPassword2(self.valid_password_2)
        time.sleep(5)
        self.lp.clickLogin()
        time.sleep(5)
        self.logger.info("*********************** Negative cases executed Sucessfully *************************************")
        self.driver.close()

    def test_login3(self, setup):
        self.logger.info("*********************** NEGATIVE TESTCASES - 3 *************************************")
        self.logger.info("*********************** Verifying Invalid Login Page *************************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.lp = Header_Validation(self.driver)
        self.lp.setInvalidUsername3(self.invalid_username_3)
        time.sleep(5)
        self.lp.setInvalidPassword3(self.invalid_password_3)
        time.sleep(5)
        self.lp.clickLogin()
        time.sleep(5)
        self.logger.info("*********************** Negative cases executed Sucessfully *************************************")
        self.driver.close()

    ##################################### POSITIVE TESTCASE ###############################################
    def test_login(self,setup):
        self.logger.info("*********************** POSITIVE TESTCASES *************************************")
        self.logger.info("*********************** Verifying Login Page *************************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.lp = Header_Validation(self.driver)
        self.lp.setUsername(self.username)
        time.sleep(5)
        self.lp.setPassword(self.password)
        time.sleep(5)
        self.lp.clickLogin()
        time.sleep(5)
        print("Title of the page: ",self.driver.title)
        self.lp.clickAdmin()
        time.sleep(5)
        self.lp.getAdminHeader()
        self.logger.info("*********************** Login Sucessfully *************************************")
        self.driver.close()

