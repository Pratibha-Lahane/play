from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException as Ec


class LoginPage:
    text_Username_XPATH = (By.XPATH, "//input[@name='username']")
    text_Password_XPATH = (By.XPATH, "//input[@placeholder='Password']")
    click_Login_Button_XPATH = (By.XPATH, "//button[normalize-space()= 'Login']")
    click_Menu_Button_XPATH = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
    click_Logout_Button_XPATH = (By.XPATH, "//a[normalize-space()= 'Logout']")

    def __init__(self, driver):
        self.driver = driver

    def Enter_Username(self, username):
        self.driver.find_element(*LoginPage.text_Username_XPATH).send_keys(username)

    def Enter_Password(self, password):
        self.driver.find_element(*LoginPage.text_Password_XPATH).send_keys(password)

    def Click_Login_Button(self):
        self.driver.find_element(*LoginPage.click_Login_Button_XPATH).click()

    def Click_Menu_Button(self):
        self.driver.find_element(*LoginPage.click_Menu_Button_XPATH).click()

    def Click_Logout_Button(self):
        self.driver.find_element(*LoginPage.click_Logout_Button_XPATH).click()

    def Login_Status(self):
        # self.driver.implicitly_wailt(10)
        try:
            self.driver.find_element(*LoginPage.click_Menu_Button_XPATH)
            return True
        except Ec:
            return False

