from common.desired_caps import appium_desired
from common.com_func import Common
from selenium.webdriver.common.by import By
import logging,time
class SelfZidongtouView(Common):
    #自动投
    zidongtou = (By.ID,'com.fengjr.mobile:id/layout_container')
    #自动投页面 顶部banner
    top_banner = (By.ID,'com.fengjr.mobile:id/banner_img')
    #顶部banner内图片
    image = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.widget.Image')
    #常见问题顶部图片
    image1 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.widget.Image')
    #开启自动投页面的确认开启按钮
    status = (By.ID,'com.fengjr.mobile:id/view_status')

    def click_zidongtou(self):
        self.driver.find_elements(*self.zidongtou)[1].click()

    def click_top_banner(self):
        logging.info('————————检测自动投-顶部banner——————————')
        try:
            element = self.driver.find_element(*self.top_banner)
        except:
            logging.info('-------没有找到自动投-顶部banner入口——————————')
            self.driver.get_screenshot_as_file('../screenshots/点击自动投-topBanner.png')
            return False
        else:
            element.click()
            return True

    def check_banner_jump(self):
        logging.info('————————check_banner_jump-----------')
        try :
            self.driver.find_element(*self.image)
        except:
            logging.info('--------跳转失败——————————')
            self.driver.get_screenshot_as_file('../screenshots/自动投-topBanner跳转.png')
            return False
        else:
            logging.info('——--————跳转成功，返回到上一级页面——————————')
            self.driver.keyevent(4)
            return True

    def click_common_problem(self):
        logging.info('——————————检测自动投-常见问题--------------')
        try:
            element = self.driver.find_element_by_android_uiautomator('new UiSelector().text("常见问题")')
        except:
            logging.info('——————————没有找到自动投-常见问题icon——————————')
            self.driver.get_screenshot_as_file('../screenshots/点击自动投-常见问题.png')
            return False
        else:
            element.click()
            return True

    def check_common_problem_jump(self):
        logging.info('——————————check_common_problem——————————')
        try:
            self.driver.find_element(*self.image1)
        except:
            logging.info('———————————常见问题跳转失败—------------')
            self.driver.get_screenshot_as_file('自动投-常见问题跳转.png')
            return False
        else:
            logging.info('---------跳转成功，返回到上一级页面-----------')
            self.driver.keyevent(4)
            return True

    def click_open_auto(self):
        logging.info('—————————点击去开启自动投———————————')
        try:
            element = self.driver.find_element(*self.status)
        except:
            logging.info('——————————没有找到开启按钮————————————')
            self.driver.get_screenshot_as_file('../screenshots/开启自动投.png')
            return False
        else:
            element.click()
            return True

    def check_openAuto_jump(self):
        logging.info('-----------check_openAuto_jump——————————————')
        try:
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("确认开启")')
        except:
            logging.info('————————————开去自动投的按钮跳转失败——————————————')
            self.driver.get_screenshot_as_file('../screenshots/zidongtou.png')
            return False
        else:
            logging.info('————————————————跳转成功,返回上级页面——————————————————')
            self.driver.keyevent(4)
            return True


if __name__ == '__main__':
    driver = appium_desired()
    obj = SelfZidongtouView(driver)
    com = Common(driver)
    time.sleep(5)
    com.shoushi()
    com.click_self_center()
    obj.click_zidongtou()
    obj.click_top_banner()
