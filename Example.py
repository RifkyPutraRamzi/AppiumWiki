from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

options = UiAutomator2Options()

options.udid = '127.0.0.1:62001'
options.platform_name = 'Android'
options.app_package = 'org.wikipedia'
options.app_activity = '.main.MainActivity'

driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

# driver.find_element(AppiumBy.ID,)

sleep(3)