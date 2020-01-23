from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import unittest
class cpptest(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome('C://Users/pradeep/Documents/chromedriver_win32/chromedriver.exe', options= options)



    def testcpptest(self):
        driver = self.driver
        self.driver.implicitly_wait(20)
        self.driver.get('http://cpp-sprint.s3-website-us-east-1.amazonaws.com/')
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/form/div[1]/input").send_keys('9599665541')
        self.driver.find_element_by_xpath('//*[@id="l_box"]/form/div[2]/input').click()
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div[3]/input[1]').send_keys('1')
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div[3]/input[2]').send_keys('2')
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div[3]/input[3]').send_keys('3')
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div[3]/input[4]').send_keys('4')
        # Login button after enter passcode
        self.driver.find_element_by_xpath('//*[@id="l_box"]/div[4]/button').click()
        self.driver.find_element_by_xpath("/html/body/div/div[4]/div/div[2]/div[2]/div/div/div[4]/a/input").click()
        # Add New Card Button
        self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/form/div/div/div/div/div/div/div/div[2]/input").click()
        # self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div[2]/div[2]/div/div/div[4]/a/input').click()
        # self.driver.find_element_by_xpath("").click()
        self.driver.find_element_by_name('card_number1').send_keys('7')
        self.driver.find_element_by_name('card_number2').send_keys('5')

        self.driver.find_element_by_name('card_number3').send_keys('6')

        self.driver.find_element_by_name('card_number4').send_keys('6')

        self.driver.find_element_by_name('card_number5').send_keys('8')

        self.driver.find_element_by_name('card_number6').send_keys('5')

        self.driver.find_element_by_name('card_issuer').click()

        self.driver.find_element_by_xpath(
            '//*[@id="root"]/form/div/div/div[1]/div[2]/div[2]/div/div[1]/div/select/option[2]').click()

        self.driver.find_element_by_name('card_type').click()

        self.driver.find_element_by_name("card_nick_name")

        self.driver.find_element_by_xpath(
            '/html/body/div/form/div/div/div[1]/div[2]/div[2]/div/div[2]/div/select/option[3]').click()

        self.driver.find_element_by_name("last_four_digit1").send_keys('4')

        self.driver.find_element_by_name("last_four_digit2").send_keys('6')

        self.driver.find_element_by_name("last_four_digit3").send_keys('4')

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
        self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div[1]/a").click()

        # My Document
        self.driver.find_element_by_xpath("/html/body/div/div[4]/div/div[2]/div[3]/div/div/div[1]/div/a/h3").click()

        # Fonesafe classic welocome Doc Download
        self.driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/div[5]/div/div/div/ul/li[1]/div/a/div/img").click()

        # Back to my Dashbaord at My document button
        self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div[1]/a").click()

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

    def tearDown(self) -> None:
        self.driver.close()

        self.driver.quit()

        print('Test Passed')


if __name__ == "__main__":
    unittest.main()
