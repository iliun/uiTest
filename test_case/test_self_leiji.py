#coding=utf-8
import pytest,os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from businessView.self_leiji import SelfLeijiView
from common.desired_caps import appium_desired
from common.com_func import Common
from selenium.webdriver.support.ui import WebDriverWait
class Test_self_leiji():

    driver = appium_desired()
    com = Common(driver)

    @pytest.fixture()
    def my_fixture(self):
        WebDriverWait(self.driver,10).until(lambda x:x.find_element(*self.com.gesture))
        self.com.shoushi()
        self.driver.implicitly_wait(3)
        self.driver.find_element(*self.com.self_button).click()

    
    def test_totalAsset(self,my_fixture):
        total_Asset = SelfLeijiView(self.driver).get_totalAsset()
        assert total_Asset != False,'没有获取到总资产'
        assert total_Asset != '','总资产显示处为空'

    def test_totalIncome(self):
        totalIncome = SelfLeijiView(self.driver).get_todoIncome()
        assert totalIncome != False,'没有获取到总收益'
        assert totalIncome != '','累计收益处显示为空'

    def test_todoIncome(self):
        todoIncome = SelfLeijiView(self.driver).get_todoIncome()
        assert todoIncome != False,'没有获取到待收收益'
        assert todoIncome != '','待收收益处显示为空'


if __name__ == '__main__':
    obj = Test_self_leiji()
    obj.test_totalAsset()