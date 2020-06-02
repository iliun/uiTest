from common.com_func import Common
from selenium.webdriver.common.by import By
import logging

class SelfLeijiView(Common):
    #总资产
    totalAsset = (By.ID,'com.fengjr.mobile:id/tv_totalAsset')
    #累计收益
    totalIncome = (By.ID,'com.fengjr.mobile:id/tv_totalIncome')
    #待收收益
    todoIncome = (By.ID,'com.fengjr.mobile:id/tv_todoIncome')

    def get_totalAsset(self):
        logging.info('---------执行get_totalAsset方法--------------')
        try :
            element = self.driver.find_element(*self.totalAsset)
        except:
            logging.info('-------没有获取到总资产元素-----------')
            print('_______截图______')
            self.get_screenshot_as_file('../screenshots/self_leiji.png')
            return False
        else:
            logging.info('————————return总资产数据——————————')
            return element.text

    def get_totalIncome(self):
        logging.info('-------------执行get_totalIncom方法——————————————')
        try:
            element = self.driver.find_element(*self.totalIncome)
        except:
            logging.info('----------没有获取到总收益-----------')
            self.get_screenshot_as_file('../screenshots/self_leiji.png')
            return False
        else:
            return element.text

    def get_todoIncome(self):
        logging.info('-------------获取待收收益——————————————')
        try:
            element = self.driver.find_element(*self.todoIncome)
        except:
            logging.info('---------没有获取到待收收益----------')
            self.get_screenshot_as_file('../screenshots/self_leiji.png')
            return False
        else:
            return element.text

