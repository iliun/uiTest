#coding=utf-8
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from common.com_func import Common
from common.desired_caps import appium_desired
from selenium.webdriver.support.ui import WebDriverWait
from businessView.self_zidongtou import SelfZidongtouView
import pytest


class Test_zidongtou():
    driver = appium_desired()
    obj = SelfZidongtouView(driver)
    com = Common(driver)

    @pytest.fixture()
    def my_fixture(self):
        WebDriverWait(self.driver,10).until(lambda x: x.find_element(*self.com.gesture))
        self.com.shoushi()
        self.driver.implicitly_wait(3)
        self.com.click_self_center()
        self.obj.click_zidongtou()

    def test_topBanner(self,my_fixture):
        assert self.obj.click_top_banner() == True,'点击topBanner失败'

    def test_topBanner_jump(self):
        assert self.obj.check_banner_jump()  == True,'topBanner_jump失败'

    def test_commonProblem(self):
        assert self.obj.click_common_problem() == True,'点击常见问题icon失败'

    def test_commonProble_jump(self):
        assert self.obj.check_common_problem_jump() == True,'常见问题跳转失败'

    def test_open_auto(self):
        assert self.obj.click_open_auto() == True,'点击开启自动投icon失败'

    def test_check_openAuto_jump(self):
        assert self.obj.check_openAuto_jump()==True,'开启自动投跳转失败'






