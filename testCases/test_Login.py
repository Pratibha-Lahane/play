import time
import pytest
from PageObjects.LoginPage import LoginPage
from Utilities.readproperties import Readconfig
from Utilities.logger import LogGenerator


class Test_Login:
    Url = Readconfig.geturl()
    Username = Readconfig.getusername()
    Password = Readconfig.getpassword()
    log = LogGenerator.loggen()

    def test_Page_Title_001(self, setup):
        self.driver = setup
        self.log.info("test_Page_Title_001 is started--->>")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Go To This Url---->>>"+ self.Url)
        if self.driver.title == "OrangeHRM":
            assert True
            self.log.info("test_Page_Title_001 is Passed..")
            self.log.info("Page Title is-->>" + self.driver.title)
            self.driver.save_screenshot("C:\\Users\\E0492097\\PycharmProjects\\Play\\Screenshots"
                                        "\\test_Page_Title_001-pass.png")
        else:
            self.log.info("test_Page_Title_001 is Failed..")
            self.driver.save_screenshot("C:\\Users\\E0492097\\PycharmProjects\\Play\\Screenshots"
                                        "\\test_Page_Title_001-fail.png")
            assert False

        self.driver.close()
        self.log.info("test_Page_Title_001 is Completed...")

########################################################################################

    def test_Login_002(self, setup):
        self.driver = setup
        self.log.info("test_Login_002 is Started...")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        time.sleep(5)
        self.log.info("Go to this Url-->>" + self.Url)
        self.lp = LoginPage(self.driver)
        self.lp.Enter_Username(self.Username)
        self.log.info("Entering Username-->" + self.Username)
        self.lp.Enter_Password(self.Password)
        self.log.info("Entering Password-->" + self.Password)
        self.lp.Click_Login_Button()
        self.log.info("Click on Login Button")

        if self.lp.Login_Status() == True:
            self.driver.save_screenshot("C:\\Users\\E0492097\\PycharmProjects\\Play\\"
                                        "Screenshots\\test_Login_002-Pass.png")
            self.lp.Click_Menu_Button()
            self.log.info("Click on Menu Button")
            self.lp.Click_Logout_Button()
            self.log.info("Click on LogOut Button")
            self.log.info("test_Login_002 is Passed.")
            assert True

        else:
            self.log.info("test_Login_002 is Failed.")
            self.driver.save_screenshot("C:\\Users\\E0492097\\PycharmProjects\\Play\\"
                                        "Screenshots\\test_Login_002-Fail.png")
            assert False

        self.driver.close()
        self.log.info("test_Login_002 is Completed")














