# -*- coding: utf8 -*-

import unittest
from time import sleep
import traceback
import sys

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException


class MyAmaysimSettings(unittest.TestCase):

    def setUp(self):
        # make sure the path of chromedriver.exe is in $PATH
        try:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()

            self.driver.get("https://www.amaysim.com.au/my-account/my-amaysim/services/pick?pid=2212604")
            self.driver.find_element_by_id("username").send_keys("0468340754")
            self.driver.find_element_by_id("password").send_keys("theHoff34")
            self.driver.find_element_by_class_name("arrow-next").click()

            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "Settings")))
            self.driver.find_element_by_link_text("Settings").click()
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.LINK_TEXT, "Help & Contact")))
            #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except (NoSuchElementException, TimeoutException, WebDriverException) as e:
            print(traceback.format_exc())
            self.fail("Exception Occurred !!!")

    def tearDown(self):
        self.driver.quit()

    def test_001_Settings_Callforwarding_Yes(self):
        "Set callforwarding to Yes with valid phone number"
        try:
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.ID, "edit_settings_call_forwarding")))

            # set to Yes
            self.driver.find_element_by_id("edit_settings_call_forwarding").click()
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.LINK_TEXT, "Confirm")))
            # "Element is not clickable" error sometimes happens for chromedriver, use javascript solution
            # http://seleniumpythonqa.blogspot.com.au/2015/09/chromedriver-element-is-not-clickable_19.html
            #self.driver.find_element_by_link_text("Confirm").click()
            self.driver.execute_script("document.getElementsByClassName('confirm_popup_confirm button-green-action small-12 columns text-center')[0].click();")
            sleep(5)
            self.driver.find_element_by_xpath("//label/span[text()='Yes']").click()
            self.driver.find_element_by_id("my_amaysim2_setting_call_divert_number").clear()
            self.driver.find_element_by_id("my_amaysim2_setting_call_divert_number").send_keys("0412345678")
            self.driver.execute_script("document.getElementById('settings_call_forwarding').scrollIntoView();")
            #self.driver.find_element_by_name("commit").click()
            self.driver.execute_script("document.getElementsByName('commit')[0].click()")
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='form_info_popup reveal-modal padding-none open']/a[@class='close-reveal-modal']")))
            #self.driver.find_element_by_xpath("//div[@class='form_info_popup reveal-modal padding-none open']/a[@class='close-reveal-modal']").click()
            self.driver.execute_script("document.getElementsByClassName('close-reveal-modal')[0].click()")
            t = self.driver.find_element_by_css_selector("div.small-1.medium-2.large-1.columns.bold.text-right.setting-option-value-text").text
            self.assertEqual("Yes", t)
            t = self.driver.find_element_by_xpath("//div[contains(text(), 'Forward calls to')]").text
            self.assertEqual("Forward calls to 0412345678", t)
        except (NoSuchElementException, TimeoutException, WebDriverException) as e:
            print(traceback.format_exc())
            self.fail("Exception Occurred !!!")

    def test_002_Settings_Callforwarding_Yes_invalid_phonenumber(self):
        "Set callforwarding to Yes with invalid phone number"
        try:
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.ID, "edit_settings_call_forwarding")))

            # set to Yes
            self.driver.find_element_by_id("edit_settings_call_forwarding").click()
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.LINK_TEXT, "Confirm")))
            #self.driver.find_element_by_link_text("Confirm").click()
            self.driver.execute_script("document.getElementsByClassName('confirm_popup_confirm button-green-action small-12 columns text-center')[0].click();")
            sleep(5)
            self.driver.find_element_by_xpath("//label/span[text()='Yes']").click()
            self.driver.find_element_by_id("my_amaysim2_setting_call_divert_number").clear()
            self.driver.find_element_by_id("my_amaysim2_setting_call_divert_number").send_keys("abcd")
            self.driver.execute_script("document.getElementById('settings_call_forwarding').scrollIntoView();")
            #self.driver.find_element_by_name("commit").click()
            self.driver.execute_script("document.getElementsByName('commit')[0].click()")
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.NAME, "commit")))
            els = self.driver.find_elements_by_xpath("//span[text()='Please enter your phone number in the following format: 0412 345 678 or 02 1234 5678']")
            self.assertEqual(1, len(els), "should show error msg for invalid phone number")
        except (NoSuchElementException, TimeoutException, WebDriverException) as e:
            print(traceback.format_exc())
            self.fail("Exception Occurred !!!")

    def test_003_Settings_Callforwarding_No(self):
        "Set callforwarding to No"
        try:
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.ID, "edit_settings_call_forwarding")))

            # set to No
            self.driver.find_element_by_id("edit_settings_call_forwarding").click()
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.LINK_TEXT, "Confirm")))
            #self.driver.find_element_by_link_text("Confirm").click()
            self.driver.execute_script("document.getElementsByClassName('confirm_popup_confirm button-green-action small-12 columns text-center')[0].click()")
            sleep(5)
            self.driver.find_element_by_xpath("//label/span[text()='No']").click()
            #self.driver.find_element_by_name("commit").click()
            self.driver.execute_script("document.getElementsByName('commit')[0].click()")
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='form_info_popup reveal-modal padding-none open']/a[@class='close-reveal-modal']")))
            #self.driver.find_element_by_xpath("//div[@class='form_info_popup reveal-modal padding-none open']/a[@class='close-reveal-modal']").click()
            self.driver.execute_script("document.getElementsByClassName('close-reveal-modal')[0].click()")
            t = self.driver.find_element_by_css_selector("div.small-1.medium-2.large-1.columns.bold.text-right.setting-option-value-text").text
            self.assertEqual("No", t)
        except (NoSuchElementException, TimeoutException, WebDriverException) as e:
            print(traceback.format_exc())
            self.fail("Exception Occurred !!!")

    def test_004_Settings_CallerID_Uncheck(self):
        "Uncheck Caller ID"
        try:
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.ID, "settings_caller_id_out")))

            checked = self.driver.find_element_by_id("my_amaysim2_setting_caller_id_out").is_selected()
            #print(checked, file=sys.stdout, flush=True)
            if checked == False:
                pass
            else:
                self.driver.execute_script("document.getElementById('my_amaysim2_setting_caller_id_out').click()")
                WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='form_info_popup reveal-modal padding-none open']/a[@class='close-reveal-modal']")))
                self.driver.execute_script("document.getElementsByClassName('close-reveal-modal')[0].click()")
                checked = self.driver.find_element_by_id("my_amaysim2_setting_caller_id_out").is_selected()
                #print(checked, file=sys.stdout, flush=True)
                self.assertFalse(checked)
        except (NoSuchElementException, TimeoutException, WebDriverException) as e:
            print(traceback.format_exc())
            self.fail("Exception Occurred !!!")


    def test_005_Settings_CallerID_Check(self):
        "Check Caller ID"
        try:
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.ID, "settings_caller_id_out")))

            checked = self.driver.find_element_by_id("my_amaysim2_setting_caller_id_out").is_selected()
            #print(checked, file=sys.stdout, flush=True)
            if checked == True:
                pass
            else:
                self.driver.execute_script("document.getElementById('my_amaysim2_setting_caller_id_out').click()")
                WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='form_info_popup reveal-modal padding-none open']/a[@class='close-reveal-modal']")))
                self.driver.execute_script("document.getElementsByClassName('close-reveal-modal')[0].click()")
                checked = self.driver.find_element_by_id("my_amaysim2_setting_caller_id_out").is_selected()
                #print(checked, file=sys.stdout, flush=True)
                self.assertTrue(checked)
        except (NoSuchElementException, TimeoutException, WebDriverException) as e:
            print(traceback.format_exc())
            self.fail("Exception Occurred !!!")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(MyAmaysimSettings)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)



