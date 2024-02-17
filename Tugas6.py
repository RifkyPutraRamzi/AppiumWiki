from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
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

# def test_search_keyword():
#     driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
#     driver.implicitly_wait(10)
#     driver.find_element(AppiumBy.ID,'org.wikipedia:id/fragment_onboarding_skip_button').click()
#     driver.find_element(AppiumBy.ID,'org.wikipedia:id/search_container').click()
#     driver.find_element(AppiumBy.ID,'org.wikipedia:id/search_src_text').send_keys('Automation')
#     text = driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="org.wikipedia:id/language_label" and @text="ENGLISH"]').click()
#     text = driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="org.wikipedia:id/page_list_item_title" and @text="Automation"]').text

#     assert text == 'Automation'
#     driver.quit()

    
# def test_more_bottom_sheet():
#     driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
#     driver.implicitly_wait(10)
#     driver.find_element(AppiumBy.ID,'org.wikipedia:id/fragment_onboarding_skip_button').click() 
#     driver.find_element(AppiumBy.ID,'org.wikipedia:id/menu_icon').click() 
#     try:
#         WebDriverWait(driver,10).until(EC.presence_of_element_located((AppiumBy.ID,'org.wikipedia:id/main_drawer_login_button')))
#         login_button_text = driver.find_element(AppiumBy.ID,'org.wikipedia:id/main_drawer_login_button').text    
#     except TimeoutException:
#         print('element gak muncul')
        
#     assert login_button_text == 'Masuk log / gabung ke Wikipedia'
#     driver.quit()

def test_login():
    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    driver.implicitly_wait(10)
    driver.find_element(AppiumBy.ID,'org.wikipedia:id/fragment_onboarding_skip_button').click()
    driver.find_element(AppiumBy.ID,'org.wikipedia:id/menu_icon').click() 
    driver.find_element(AppiumBy.ID,'org.wikipedia:id/main_drawer_login_button').click()
    driver.find_element(AppiumBy.ID,'org.wikipedia:id/create_account_login_button').click()
    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@text="Nama pengguna"]').send_keys('Mzeees')
    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@text="Kata sandi"]').send_keys('Testing123')
    driver.find_element(AppiumBy.ID,'org.wikipedia:id/login_button').click()
    driver.find_element(AppiumBy.ID,'org.wikipedia:id/menu_icon').click()
    try:
        WebDriverWait(driver,10).until(EC.presence_of_element_located((AppiumBy.ID,'org.wikipedia:id/main_drawer_account_name')))
        username_text = driver.find_element(AppiumBy.ID,'org.wikipedia:id/main_drawer_account_name').text    
    except TimeoutException:
        print('element gak muncul')

    assert username_text == 'Mzeees'

def test_logout():
    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    driver.implicitly_wait(10)
    driver.find_element(AppiumBy.ID,'org.wikipedia:id/fragment_onboarding_skip_button').click()
    driver.find_element(AppiumBy.ID,'org.wikipedia:id/menu_icon').click() 
    driver.find_element(AppiumBy.ID,'org.wikipedia:id/main_drawer_settings_container').click()
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(572, 1481)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(587, 55)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    driver.find_element(AppiumBy.ID,'org.wikipedia:id/logoutButton').click()
    driver.find_element(AppiumBy.ID,'android:id/button1').click()
    driver.find_element(AppiumBy.ID,'org.wikipedia:id/menu_icon').click()
    try:
        WebDriverWait(driver,10).until(EC.presence_of_element_located((AppiumBy.ID,'org.wikipedia:id/main_drawer_login_button')))
        login_button_text = driver.find_element(AppiumBy.ID,'org.wikipedia:id/main_drawer_login_button').text    
    except TimeoutException:
        print('element gak muncul')
        
    assert login_button_text == 'Masuk log / gabung ke Wikipedia'
    driver.quit()


    
    
    






    




