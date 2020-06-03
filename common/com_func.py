import csv
import logging,time,os,sys
from common import desired_caps
from selenium.webdriver.common.by import By
from baseView.baseView_func import BaseView
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
class Common(BaseView):
    #启动图的跳过按钮
    skipButton = (By.ID,'com.fengjr.mobile:id/skip')
    #隐私协议的同意按钮
    agreeButton = (By.ID,'com.fengjr.mobile:id/agree')
    #权限请求的允许按钮
    allowButton = (By.ID,'com.android.packageinstaller:id/permission_allow_button')
    #手势密码
    gesture = (By.ID,'com.fengjr.mobile:id/gesture')
    self_button = (By.ID,'com.fengjr.mobile:id/center')
    #处理隐私协议页面
    def agree_button(self):
        logging.info("————————点击隐私协议同意弹窗————————————")
        try:
            agreeButton = self.driver.find_element(*self.agreeButton)
        except NoSuchElementException:
            logging.info('——————没有隐私协议同意按钮——————')
        else:
            agreeButton.click()
    #处理权限请求弹窗
    def allow_button(self):
        logging.info("————————点击权限请求的允许按钮——————————")
        try:
            allowButton = self.driver.find_element(*self.allowButton)
        except NoSuchElementException:
            logging.info('————————没有权限请求的允许按钮——————————')
        else:
            allowButton.click()
    #处理启动图页面
    def skip_button(self):
        logging.info('——————点击启动图的跳过按钮——————')
        try:
            skip = self.driver.find_element(*self.skipButton)
        except NoSuchElementException:
            logging.info("-------没有启动图的跳过按钮------")
            pass
        else:
            skip.click()
            logging.info('-----点击成功------------')

    #处理手势密码
    def shoushi(self):
        logging.info('---------手势密码-------------')
        TouchAction(self.driver).press(x=550,y=850).wait(200)\
            .move_to(x=850,y=850).wait(200).\
            move_to(x=850,y=1100).wait(200).\
            move_to(x=850,y=1330).release().perform()
        time.sleep(3)

    #获取页面大小
    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x,y

    #左滑
    def swipe_left(self):
        logging.info('——————————左滑————————')
        l = self.get_size()
        x1 = int(l[0] * 0.75)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.driver.swipe(x1,y1,x2,y1,2000)

    #下滑
    def swipe_down(self):
        logging.info('——————————下滑————————')
        l = self.get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.8)
        y2 = int(l[0] * 0.5)
        self.driver.swipe(x1,y1,x1,y2,2000)

    #获取当前时间
    def get_time(self):
        now = time.strftime('%Y-%m-%d %H%M%S')
        return now

    #截图
    def get_screenshot(self,module):
        time = self.get_time()
        image_file = os.path.dirname(os.path.abspath(__file__))+'/screenshots/%s_%s.png' %(module,time)
        logging.info('——————获取 %s 的截图————————' %module)
        self.driver.get_screenshot_as_file(image_file)
        logging.info('-------截图成功-------')

    #立即启动/蒙层，点击任意区域
    def click_random(self):
        l = self.get_size()
        x = int(l[0]*0.5)
        y = int(l[1]*0.9)
        self.driver.tap(x,y)
    #未登录首页弹窗关闭方法：
    # def close_home(self):
    #     logging.info('————————关闭未登录时首页弹窗——————————')
    #     try:
    #
    #     except NoSuchElementException:
    #         logging.info('————————没有未登录时首页弹窗——————————')
    #     else:

    #获取csv文件指定行的数据
    def get_csv(self,csvFile,line):
        csv_file = csv.reader(open(csvFile,'r',encoding='utf-8-sig'))
        for i,row in enumerate(csv_file):
            if i==line:
                return row

    def click_self_center(self):
        logging.info('-------点击个人中心按钮————————————')
        self.driver.find_element(*self.self_button).click()
        self.driver.implicitly_wait(3)



if __name__ == '__main__':
    driver = desired_caps.appium_desired()
    obj = Common(driver)
    time.sleep(7)
    obj.shoushi()
    time.sleep(2)
    obj.swipe_left()





