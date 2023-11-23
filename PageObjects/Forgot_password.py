from selenium import webdriver
from selenium.webdriver.common.by import By

class Forgot_password:
    link_forgotpassword_xpath = "//*[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']"
    textbox_username_xpath = "//input[@class='oxd-input oxd-input--active']"
    button_resetpassword_xpath = "//button[text()=' Reset Password ']"
    text_getsuccessmsg_xpath = "//h6[@class='oxd-text oxd-text--h6 orangehrm-forgot-password-title']"

    def __init__(self,driver):
        self.driver = driver

    def clickForgotPassword(self):
        self.driver.find_element(By.XPATH,self.link_forgotpassword_xpath).click()

    def setUserName(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setInvalidUserName(self,invalid_username_2):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(invalid_username_2)

    def clickResetPassword(self):
        self.driver.find_element(By.XPATH,self.button_resetpassword_xpath).click()

    def getSuccessMessage(self):
       success_msg = self.driver.find_element(By.XPATH,self.text_getsuccessmsg_xpath)
       print(success_msg.text)
