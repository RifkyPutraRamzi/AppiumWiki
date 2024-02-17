from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pytest
from time import sleep

options = UiAutomator2Options()

options.udid = '127.0.0.1:62001'
options.platform_name = 'Android'
options.app_package = 'org.wikipedia'
options.app_activity = '.main.MainActivity'
options.no_reset = False

def test_search_keyword():
    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    driver.implicitly_wait(10)
    driver.find_element(AppiumBy.ID,'org.wikipedia:id/fragment_onboarding_skip_button').click()
    driver.find_element(AppiumBy.ID,'org.wikipedia:id/search_container').click()
    driver.find_element(AppiumBy.ID,'org.wikipedia:id/search_src_text').send_keys('Automation')
    text = driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="org.wikipedia:id/language_label" and @text="ENGLISH"]').click()
    text = driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="org.wikipedia:id/page_list_item_title" and @text="Automation"]').text

    assert text == 'Automation'
    driver.quit()

    
def test_more_bottom_sheet():
    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    driver.implicitly_wait(10)
    driver.find_element(AppiumBy.ID,'org.wikipedia:id/fragment_onboarding_skip_button').click() # click skip button
    driver.find_element(AppiumBy.ID,'org.wikipedia:id/menu_icon').click() # click menu/more button
    try:
        WebDriverWait(driver,10).until(EC.presence_of_element_located((AppiumBy.ID,'org.wikipedia:id/main_drawer_login_button')))
        login_button_text = driver.find_element(AppiumBy.ID,'org.wikipedia:id/main_drawer_login_button').text    
    except TimeoutException:
        print('element gak muncul')
        
    assert login_button_text == 'Masuk log / gabung ke Wikipedia'
    driver.quit()
