from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys


class Avtorise(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="..\drivers\chromedriver")
        self.driver.implicitly_wait(10)

    def test1(self):
        driver = self.driver
        site = "http://way2automation.com/way2auto_jquery/index.php"
        driver.get(site)
        time.sleep(10)
        login = "1234"
        passwd = "44444"
        button_avtorise = driver.find_element_by_class_name("fancybox")
        button_avtorise.send_keys(Keys.ENTER)
        login_field = driver.find_element_by_name("username")
        password_field = driver.find_element_by_name("password")
        login_field.send_keys(login)
        password_field.send_keys(passwd)
        button_login = driver.find_element_by_class_name("button")
        button_login.click()
        time.sleep(3)

        alert = driver.find_element_by_id("alert1")
        assert "Invalid username password." in alert


def tearDown(self):
    self.driver.quit()


if __name__ == "__main__":
    unittest.main()
