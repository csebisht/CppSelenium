from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

# from allure_commons.types import AttachmentType

#from pyramid import testing

import unittest

#import pytest

#import os

#import time


#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# current_directory = os.getcwd()

# wait = WebDriverWait(webdriver,10)
# wait.until(EC.presence_of_all_elements_located('ng-valid'))


class Mytest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        options.add_argument('--disable-gpu')
        options.add_argument('--headless')
        self.driver = webdriver.Chrome('C://Users/pradeep/Documents/chromedriver_win32/chromedriver.exe', options= options)

        #options = Options()
        #options.headless = True
        #self.driver = webdriver.Chrome('C://Users/pradeep/Documents/chromedriver_win32/chromedriver.exe', options= options)
        #self.driver = webdriver.Chrome('C://Users/pradeep/Documents/chromedriver_win32/chromedriver.exe')


    def test_cpp_login(self):
        driver = self.driver
        self.driver.implicitly_wait(30)
        self.driver.get('http://cpp-sprint.s3-website-us-east-1.amazonaws.com/')
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/form/div[1]/input").send_keys('9599665541')
        self.driver.find_element_by_xpath('//*[@id="l_box"]/form/div[2]/input').click()
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div[3]/input[1]').send_keys('1')
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div[3]/input[2]').send_keys('2')
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div[3]/input[3]').send_keys('3')
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div[3]/input[4]').send_keys('4')
        # Login button after enter passcode
        self.driver.find_element_by_xpath('//*[@id="l_box"]/div[4]/button').click()
    def test_register_card(self):
        driver = self.driver
        self.driver.find_element_by_xpath("/html/body/div/div[4]/div/div[2]/div[2]/div/div/div[4]/a/input").click()
        # Add New Card Button
        self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/form/div/div/div/div/div/div/div/div[2]/input").click()
        # self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div[2]/div[2]/div/div/div[4]/a/input').click()
        # self.driver.find_element_by_xpath("").click()
        self.driver.find_element_by_name('card_number1').send_keys('6')
        self.driver.find_element_by_name('card_number2').send_keys('7')
        self.driver.find_element_by_name('card_number3').send_keys('6')
        self.driver.find_element_by_name('card_number4').send_keys('7')
        self.driver.find_element_by_name('card_number5').send_keys('8')
        self.driver.find_element_by_name('card_number6').send_keys('5')
        self.driver.find_element_by_name('card_issuer').click()
        self.driver.find_element_by_xpath('//*[@id="root"]/form/div/div/div[1]/div[2]/div[2]/div/div[1]/div/select/option[2]').click()
        self.driver.find_element_by_name('card_type').click()
        self.driver.find_element_by_name("card_nick_name")
        self.driver.find_element_by_xpath('/html/body/div/form/div/div/div[1]/div[2]/div[2]/div/div[2]/div/select/option[3]').click()
        self.driver.find_element_by_name("last_four_digit1").send_keys('4')
        self.driver.find_element_by_name("last_four_digit2").send_keys('6')
        self.driver.find_element_by_name("last_four_digit3").send_keys('6')
        self.driver.find_element_by_name("last_four_digit4").send_keys('4')
        # self.driver.find_element_by_name('card_nick_name').click()
        s1 = Select(self.driver.find_element_by_name('card_nick_name'))
        s1.select_by_visible_text('Cardio')
        # Selected an option for Card nick name
        # self.driver.find_element_by_xpath("/html/body/div/form/div/div/div[1]/div[2]/div[3]/div[1]/div[5]/div/select/option[3]").click()

        # Submit button at Register New Card
        self.driver.find_element_by_xpath("//input[@value='Save Card' and @type='submit']").click()
        # self.driver.find_element_by_xpath('/html/body/div/form/div/div/div[1]/div[2]/div[3]/div[2]/div[2]/div/div/input').click()

        # self.driver.find_element_by_xpath("//input[@value='Block' or @class='btn-brd mr15']").click()

        # Back to my Dashboard Button at my card page
        self.driver.find_element_by_partial_link_text('Back to My Dashboard').click()

    def test_my_document(self):
        if self.driver:
            driver = self.driver
            print('test_register_card if')
            self.driver.find_element_by_xpath("/html/body/div/div[4]/div/div[2]/div[3]/div/div/div[1]/div/a/h3").click()
            # Fonesafe classic welocome Doc Download
            self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div[5]/div/div/div/ul/li[1]/div/a/div/img").click()
            # Back to my Dashbaord at My document button
            self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div[1]/a").click()
        else:
            print('test_register_card else')


    def test_my_product(self):
        driver = self.driver
        # My Product Page
        self.driver.find_element_by_xpath("/html/body/div/div[4]/div/div[2]/div[3]/div/div/div[2]/div/a/h3").click()

        # My Product
        s2 = Select(self.driver.find_element_by_name("pro_name"))

        s2.select_by_visible_text("Fonesafe Classic")

        # self.driver.find_element_by_name("pro_name").click()

        # Fonesafe Classic Dropdwon arrow
        self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/div[4]/div/div/div/div/div[1]/div/div[3]/img").click()

        # Eros now Dropdown arrow
        # self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div[4]/div/div/div/ul/li[3]/div/div[1]/div[3]/div/span/img").click()

        # Message title
        # s3 =Select(self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div[4]/div/div/div/ul/li[3]/div/div[3]/div/div[3]/div[2]/div/select"))

        # s3.select_by_visible_text("I'd like to request a unique code")

        # s4 = Select(self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div[4]/div/div/div/ul/li[3]/div/div[3]/div/div[3]/div[3]/div/select"))

        # Contact methode
        # s4.select_by_visible_text("Call me back")

        # submit button
        # self.driver.find_element_by_xpath("//input[@value='Send']").click()

        # self.driver.find_element_by_xpath("/html/body/div/div[5]/div/div/div[3]/div/div/button").click()

        self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div[1]/a").click()

    def test_my_card_page(self):
        # My Card  on Dashboard
        self.driver.find_element_by_xpath("/html/body/div/div[4]/div/div[2]/div[3]/div/div/div[3]/div/a/h3").click()

        s5 = Select(self.driver.find_element_by_name("pro_name"))

        s5.select_by_visible_text("Fonesafe Platinum")

        # self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div[5]/div/div/div/ul/li[2]/div/div[1]/div[3]/div/span/img").click()

        # Block all card button
        # self.driver.find_element_by_xpath("//input[@value='Block all cards']").click()
        # back to Dashboard button from Block all card page
        self.driver.find_element_by_xpath(('//a[contains(@href,"/quicklink")]')).click()

        # how can help at footer
        # self.driver.find_element_by_xpath('//a[contains(@href,"/Privacystatement")]').click()

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()
        print('Test Passed')


if __name__ == "__main__":
    unittest.main()
