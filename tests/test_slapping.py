from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from time import sleep
from Pages.Login import LoginPage
import unittest

driver = webdriver.Chrome(ChromeDriverManager().install())


class Test_bpm(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

###Login

    def test01_login_wrong_phone(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        alert = Alert(driver=self.driver)
        login = LoginPage(driver=self.driver)
        login.enter_login_username("9122367800")
        login.enter_login_btn_submit_next()
        login.enter_login_password("43126")
        login.enter_login_btn_submit()
        sleep(1)
        print(alert.text)
        alert.accept()
        print("با زدن شماره اشتباه و کد صحیح وارد نمی شود.")



    def test02_login_wrong_code(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        alert = Alert(driver=self.driver)
        login = LoginPage(driver=self.driver)
        login.enter_login_username("9122367860")
        login.enter_login_btn_submit_next()
        login.enter_login_password("43136")
        login.enter_login_btn_submit()
        sleep(1)
        print(alert.text)
        alert.accept()
        print("با زدن شماره صحیح و کد اشتباه وارد نشد.")

    def test03_login_not_phone(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        alert = Alert(driver=self.driver)
        login = LoginPage(driver=self.driver)
        login.enter_login_btn_submit_next()
        sleep(1)
        print(alert.text)
        alert.accept()
        print("بدون وارد کردن شماره تلفن وارد نشد.")

    def test04_login(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        sleep(1)
        login.enter_login_username("9122367860")
        login.enter_login_btn_submit_next()
        login.enter_login_password("43126")
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل شد")



    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
