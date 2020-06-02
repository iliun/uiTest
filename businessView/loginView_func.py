import logging,time
from common.desired_caps import appium_desired
from common.com_func import Common
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

class LoginView(Common):
    #我的按钮
    self_button = (By.ID,'com.fengjr.mobile:id/center')
    #定位密码登录
    passwordLogin = (By.ID,'com.fengjr.mobile:id/login_with_pwd')
    #手机号输入框
    phone_input = (By.ID,'com.fengjr.mobile:id/phone_input')
    #密码输入框
    pwd_input = (By.ID,'com.fengjr.mobile:id/pwd_input')
    #登录按钮
    login_button = (By.ID,'com.fengjr.mobile:id/tvLogin')
    #登录账号
    login_name = (By.ID,'com.fengjr.mobile:id/tv_left_subtitle')
    #设置
    settings = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[5]/android.support.v7.widget.RecyclerView/android.view.ViewGroup[4]/android.widget.TextView')
    #安全退出
    logout_button = (By.ID,'com.fengjr.mobile:id/quit')
    #确认退出弹窗
    confirm_exit = (By.ID,'com.fengjr.mobile:id/positiveButton')
    #手机号输入框的清除按钮
    clear_button = (By.ID,'com.fengjr.mobile:id/image_cancel_phone_num')

    #判断是否需要清除手机号输入框内容
    def check_clear_status(self):
        logging.info('————————————判断是否需要清除输入框内容—————————————')
        try:
            self.driver.find_element(*self.clear_button)
        except NoSuchElementException:
            logging.info('——————————————不需要清除手机号输入框内容————————————')
        else:
            logging.info('————————————需要清除手机号输入框内容—————————————')
            self.driver.find_element(*self.clear_button).click()


    #密码登录流程
    def login_action(self,username,password):
        # self.agree_button()
        # self.allow_button()
        WebDriverWait(self.driver,7).until(lambda x:x.find_element(*self.self_button))
        logging.info('-----------执行登录操作-----------')
        self.driver.find_element(*self.self_button).click()
        WebDriverWait(self.driver,3).until(lambda x:x.find_element(*self.passwordLogin))
        self.driver.find_element(*self.passwordLogin).click()
        self.check_clear_status()
        logging.info('——————————输入用户名:%s-----------' %username)
        self.driver.implicitly_wait(2)
        self.driver.find_element(*self.phone_input).send_keys(username)
        logging.info('——————————输入密码:%s————————————' %password)
        self.driver.implicitly_wait(2)
        self.driver.find_element(*self.pwd_input).send_keys(password)
        logging.info('-----------点击登录按钮-----------')
        self.driver.find_element(*self.login_button).click()
        WebDriverWait(self.driver,5).until(lambda x:x.find_element(*self.login_name))
        #self.click_random()
    #首次登录处理3个蒙层
    # def check_mengceng(self):
    #检测是否登录成功
    def check_login_success(self):
        logging.info('——————检测登录是否成功————————————')
        try:
            self.driver.find_element(*self.login_name)
        except NoSuchElementException:
            logging.error('--------登录失败————————')
            self.get_screenshot('../screenshots/登录模块')
            return False
        else:
            logging.info('————————登录成功——————————')
            return True
    #退出登录流程
    def logout_action(self):
        logging.info('————————退出登录——————————')
        self.swipe_down()
        logging.info('-------设置按钮——————————')
        self.driver.find_element(*self.settings).click()
        self.driver.implicitly_wait(2)
        self.swipe_down()
        self.driver.find_element(*self.logout_button).click()
        self.driver.find_element(*self.confirm_exit).click()

    def check_logout_success(self):
        self.driver.find_element(*self.self_button).click()
        try:
            self.driver.find_element(*self.passwordLogin)
        except :
            logging.error('——————————退出登录失败——————————')
            self.get_screenshot('../screenshots/退出登录模块')
            return False
        else:
            logging.info('——————————退出登录成功————————————')
            return True


if __name__ == '__main__':
    driver = appium_desired()
    obj = LoginView(driver)
    obj.login_action('18632843357','1234qwer')
    obj.check_login_success()
    obj.skip_button()
    obj.logout_action()
    obj.check_logout_success()






