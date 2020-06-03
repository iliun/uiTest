#coding=utf-8
import os,time
os.system('pytest ../test_case/test_self_leiji.py --alluredir=../reports --clean-alluredir')
time.sleep(5)
os.system('allure serve ../reports')