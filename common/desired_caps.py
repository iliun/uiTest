#coding=utf-8
from appium import webdriver
import os
import yaml
import logging
import logging.config

CON_LOG='../config/log.conf'
CON_LOG_PATH = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')),'config/log.conf')
logging.config.fileConfig(CON_LOG_PATH)
logging=logging.getLogger()

def appium_desired():
    with open("../config/caps.yaml",'r',encoding='utf-8') as file:
        data = yaml.load(file,Loader=yaml.FullLoader)
    desired_caps = {}
    desired_caps['platformName']=data['platformName']
    desired_caps['platformVersion']=str(data['platformVersion'])
    desired_caps['deviceName']=data['deviceName']
    desired_caps['udid']=data['udid']
    dir_name = os.path.dirname(os.path.dirname(__file__))
    app_path = os.path.join(dir_name,'app',data['app'])
    desired_caps['app']= app_path
    desired_caps['appActivity']=data['appActivity']
    desired_caps['appPackage']=data['appPackage']
    desired_caps['noReset']=data['noReset']
    desired_caps['unicodeKeyboard']=data['unicodeKeyboard']
    desired_caps['resetKeyboard']=data['resetKeyboard']
    desired_caps['ip']=data['ip']
    desired_caps['port']=data['port']
    logging.info("启动app")
    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
    return driver


if __name__ == '__main__':
    appium_desired()