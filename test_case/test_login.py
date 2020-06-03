#coding=utf-8
import logging,time,sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from common.desired_caps import appium_desired
from businessView.loginView_func import LoginView
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class TestLogin():
    csv_file = '../data/numb.csv'
    driver = appium_desired()

    def teardown_method(self):
        obj = LoginView(self.driver)
        obj.logout_action()
        self.driver.keyevent(4)

    def test_01(self):
        logging.info('----通过测试')
        obj = LoginView(self.driver)
        data = obj.get_csv(self.csv_file,0)
        obj.login_action(data[0],data[1])
        assert obj.check_login_success()==True

    def test_02(self):
        logging.info('----密码错误')
        obj = LoginView(self.driver)
        data = obj.get_csv(self.csv_file, 1)
        obj.login_action(data[0], data[1])
        assert obj.check_login_success() == False,'test02 登录未成功'



