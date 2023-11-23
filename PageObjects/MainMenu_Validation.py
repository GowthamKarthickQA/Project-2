
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Mainmenu_Validation:
    # Using locators,finding an element
    textbox_Username_xpath = "//input[@name='username']"
    textbox_Password_name = "password"
    button_Login_xpath = "//button[@type='submit']"
    menu_mainmenu_xpath = "//li[@class='oxd-main-menu-item-wrapper']"
    menu_Admin_xpath = "//li[@class='oxd-main-menu-item-wrapper']/a/span[text()='Admin']"
    menu_PIM_xpath = "//li[@class='oxd-main-menu-item-wrapper']/a/span[text()='PIM']"
    menu_Leave_xpath ="//li[@class='oxd-main-menu-item-wrapper']/a/span[text()='Leave']"
    menu_Time_xpath = "//li[@class='oxd-main-menu-item-wrapper']/a/span[text()='Time']"
    menu_Recruitment_xpath = "//li[@class='oxd-main-menu-item-wrapper']/a/span[text()='Recruitment']"
    menu_MyInfo_xpath = "//li[@class='oxd-main-menu-item-wrapper']/a/span[text()='My Info']"
    menu_Performance_xpath = "//li[@class='oxd-main-menu-item-wrapper']/a/span[text()='Performance']"
    menu_Dashboard_xpath = "//li[@class='oxd-main-menu-item-wrapper']/a/span[text()='Dashboard']"
    menu_Directory_xpath = "//li[@class='oxd-main-menu-item-wrapper']/a/span[text()='Directory']"
    menu_Maintenance_xpath = "//li[@class='oxd-main-menu-item-wrapper']/a/span[text()='Maintenance']"
    menu_Buzz_xpath = "//li[@class='oxd-main-menu-item-wrapper']/a/span[text()='Buzz']"

    def __init__(self,driver):
        self.driver = driver

    def setUsername(self,username):
        self.driver.find_element(By.XPATH,self.textbox_Username_xpath).clear() # clear if any exist
        self.driver.find_element(By.XPATH,self.textbox_Username_xpath).send_keys(username) # enter valid username

    def setPassword(self,password):
        self.driver.find_element(By.NAME,self.textbox_Password_name).clear() # clear if any exist
        self.driver.find_element(By.NAME,self.textbox_Password_name).send_keys(password) # enter valid password

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_Login_xpath).click() # Click login button

    def getMainmenu(self):

 ##################################### CODE - 1 ###############################################

    # Validating main menu on side pane is displaying or not

        Admin_menu = self.driver.find_element(By.XPATH,self.menu_Admin_xpath)
        print("Is Admin displayed : ",Admin_menu.is_displayed())

        PIM_menu = self.driver.find_element(By.XPATH,self.menu_PIM_xpath)
        print("Is PIM displayed : ",PIM_menu.is_displayed())

        Leave_menu = self.driver.find_element(By.XPATH,self.menu_Leave_xpath)
        print("Is Leave displayed : ",Leave_menu.is_displayed())

        Time_menu = self.driver.find_element(By.XPATH,self.menu_Time_xpath)
        print("Is Time displayed : ",Time_menu.is_displayed())

        Recruitment_menu = self.driver.find_element(By.XPATH,self.menu_Recruitment_xpath)
        print("Is Recruitment displayed : ",Recruitment_menu.is_displayed())

        MyInfo_menu = self.driver.find_element(By.XPATH,self.menu_MyInfo_xpath)
        print("Is My INFO displayed : ",MyInfo_menu.is_displayed())

        Performance_menu = self.driver.find_element(By.XPATH,self.menu_Performance_xpath)
        print("Is Performance displayed : ",Performance_menu.is_displayed())

        Dashboard_menu = self.driver.find_element(By.XPATH, self.menu_Dashboard_xpath)
        print("Is Dashboard displayed : ", Dashboard_menu.is_displayed())

        Directory_menu = self.driver.find_element(By.XPATH, self.menu_Directory_xpath)
        print("Is Directory displayed : ", Directory_menu.is_displayed())

        Maintenance_menu = self.driver.find_element(By.XPATH, self.menu_Maintenance_xpath)
        print("Is Maintenance displayed : ", Maintenance_menu.is_displayed())

        Buzz_menu = self.driver.find_element(By.XPATH, self.menu_Buzz_xpath)
        print("Is Buzz displayed : ", Buzz_menu.is_displayed())

##################################### CODE - 2 #################################

        # mainmenu = self.driver.find_elements(By.XPATH, self.menu_mainmenu_xpath)
        # for i in mainmenu:
        #     list = i.text
        #     if list == "Admin":
        #         print("Admin is displayed")
        #     elif list == "PIM":
        #         print("PIM is displayed")
        #     elif list == "Leave":
        #         print("Leave is displayed")
        #     elif list == "Time":
        #         print("Time is displayed")
        #     elif list == "Recruitment":
        #         print("Recruitment is displayed")
        #     elif list == "My Info":
        #         print("My Info is displayed")
        #     elif list == "Performance":
        #         print("Performance is displayed")
        #     elif list == "Dashboard":
        #         print("Dashboard is displayed")
        #     elif list == "Directory":
        #         print("Directory is displayed")
        #     elif list == "Maintenance":
        #         print("Maintenance is displayed")
        #     elif list == "Buzz":
        #         print("Buzz is displayed")
        #     else:
        #         print("Check Your Code Once!!!!")
























