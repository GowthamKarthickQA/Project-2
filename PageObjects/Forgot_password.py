from selenium import webdriver
from selenium.webdriver.common.by import By

class Forgot_password:
    # Using locators,finding an element
    link_forgotpassword_xpath = "//*[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']"
    textbox_username_xpath = "//input[@class='oxd-input oxd-input--active']"
    button_resetpassword_xpath = "//button[text()=' Reset Password ']"
    text_getsuccessmsg_xpath = "//h6[@class='oxd-text oxd-text--h6 orangehrm-forgot-password-title']"

    def __init__(self,driver):
        self.driver = driver

    def clickForgotPassword(self):
        self.driver.find_element(By.XPATH,self.link_forgotpassword_xpath).click()  #click forgot password button

    def setUserName(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).clear() # Clear text if any exist
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)  # enter valid username

    def setInvalidUserName(self,invalid_username_2):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).clear() # Clear text if any exist
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(invalid_username_2) # enter valid username

    def clickResetPassword(self):
        self.driver.find_element(By.XPATH,self.button_resetpassword_xpath).click() # Click reset password button

    def getSuccessMessage(self):
       success_msg = self.driver.find_element(By.XPATH,self.text_getsuccessmsg_xpath) # getting successful message
       print(success_msg.text)
