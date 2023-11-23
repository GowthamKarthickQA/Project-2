
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Header_Validation:
    # Using locators,finding an element
    textbox_Username_xpath = "//input[@name='username']"
    textbox_Password_name = "password"
    button_Login_xpath = "//button[@type='submit']"
    click_Admin_xpath = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a"
    header_Usermanagement_xpath = "//span[@class='oxd-topbar-body-nav-tab-item']"
    header_Job_xpath = "//li[@class='oxd-topbar-body-nav-tab --parent']/span"
    header_Organisation_xpath ="//li[@class='oxd-topbar-body-nav-tab --parent']/span[text()='Organization ']"
    header_Qualifications_xpath = "//li[@class='oxd-topbar-body-nav-tab --parent']/span[text()='Qualifications ']"
    header_Nationalities_xpath = "//li[@class='oxd-topbar-body-nav-tab']/a[text()='Nationalities']"
    header_Corporatebranding_xpath = "//li[@class='oxd-topbar-body-nav-tab']/a[text()='Corporate Branding']"
    header_Configuration_xpath = "//li[@class='oxd-topbar-body-nav-tab --parent']/span[text()='Configuration ']"

    def __init__(self,driver):
        self.driver = driver

    def setUsername(self,username):
        self.driver.find_element(By.XPATH,self.textbox_Username_xpath).clear() # Clear username if any exist
        self.driver.find_element(By.XPATH,self.textbox_Username_xpath).send_keys(username) # Enter valid username

    def setPassword(self,password):
        self.driver.find_element(By.NAME,self.textbox_Password_name).clear() # Clear password if any exist
        self.driver.find_element(By.NAME,self.textbox_Password_name).send_keys(password) # Enter valid password

    ################################# NEGATIVE CASES - LOGIN CREDENTIALS ############################################
    def setValidUsername(self,valid_username):
        self.driver.find_element(By.XPATH,self.textbox_Username_xpath).clear() # Clear username if any exist
        self.driver.find_element(By.XPATH,self.textbox_Username_xpath).send_keys(valid_username) # Enter valid username

    def setInvalidPassword(self,invalid_password):
        self.driver.find_element(By.NAME,self.textbox_Password_name).clear()  # Clear invalid password if any exist
        self.driver.find_element(By.NAME,self.textbox_Password_name).send_keys(invalid_password) # Enter invalid password

    def setInvalidUsername2(self,invalid_username_2):
        self.driver.find_element(By.XPATH,self.textbox_Username_xpath).clear() # Clear invalid username if any exist
        self.driver.find_element(By.XPATH,self.textbox_Username_xpath).send_keys(invalid_username_2) # Enter invalid username

    def setValidPassword2(self,valid_password_2):
        self.driver.find_element(By.NAME,self.textbox_Password_name).clear() # Clear valid password if any exist
        self.driver.find_element(By.NAME,self.textbox_Password_name).send_keys(valid_password_2) # Enter valid password

    def setInvalidUsername3(self,invalid_username_3):
        self.driver.find_element(By.XPATH,self.textbox_Username_xpath).clear() # Clear username if any exist
        self.driver.find_element(By.XPATH,self.textbox_Username_xpath).send_keys(invalid_username_3) # Enter invalid username

    def setInvalidPassword3(self,invalid_password_3):
        self.driver.find_element(By.NAME,self.textbox_Password_name).clear()
        self.driver.find_element(By.NAME,self.textbox_Password_name).send_keys(invalid_password_3) # Enter invalid password

  #############################################################################################################

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_Login_xpath).click()

    def clickAdmin(self):
        self.driver.find_element(By.XPATH, self.click_Admin_xpath).click()

    def getAdminHeader(self):
        user_management = self.driver.find_element(By.XPATH,self.header_Usermanagement_xpath)
        print("Is User Management displayed : ",user_management.is_displayed())

        job_header = self.driver.find_element(By.XPATH,self.header_Job_xpath)
        print("Is Job displayed : ",job_header.is_displayed())

        organisation_header = self.driver.find_element(By.XPATH,self.header_Organisation_xpath)
        print("Is Organization displayed : ",organisation_header.is_displayed())

        Qualifications_header = self.driver.find_element(By.XPATH,self.header_Qualifications_xpath)
        print("Is Qualifications displayed : ",Qualifications_header.is_displayed())

        Nationalities_header = self.driver.find_element(By.XPATH,self.header_Nationalities_xpath)
        print("Is Nationalities displayed : ",Nationalities_header.is_displayed())

        Corporatebranding_header = self.driver.find_element(By.XPATH,self.header_Corporatebranding_xpath)
        print("Is Corporate Branding displayed : ",Corporatebranding_header.is_displayed())

        Configuration_header = self.driver.find_element(By.XPATH,self.header_Configuration_xpath)
        print("Is Configuration displayed : ",Configuration_header.is_displayed())






















