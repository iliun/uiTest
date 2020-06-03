#coding=utf-8
class BaseView(object):
    def __init__(self,driver):
        self.driver = driver
    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self,start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def get_screenshot_as_file(self,fileName):
        return self.driver.get_screenshot_as_file(fileName)

    def find_element_by_android_uiautomator(self):
        return self.deriver.find_element_by_android_uiautomator()