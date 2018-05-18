from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time
import unittest
from selenium.webdriver.common.keys import Keys


class Bert(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="..\drivers\chromedriver")
        # driver = webdriver.Opera("..\drivers\operadriver.exe")
        self.driver.implicitly_wait(10)

    def test(self):
        driver = self.driver
        driver.get("http://way2automation.com/way2auto_jquery/registration.php")
        time.sleep(2)
        # driver.find_element_by_xpath("#login").send_keys(Keys.ENTER)
        driver.find_element_by_class_name("fancybox").send_keys(Keys.ENTER)
        # driver.find_element_by_name("fancybox").send_keys(Keys.ENTER)
        login_field = driver.find_element_by_name("username")
        login_field.send_keys("1234")
        password_field = driver.find_element_by_name("password")
        password_field.send_keys("44444")
        button_login = driver.find_element_by_class_name("button")
        button_login.click()
        time.sleep(3)

        alert = driver.find_element_by_id("alert1")
        assert "Invalid username password." in alert
    # driver.set_page_load_timeout(10)
    # driver.get("http://way2automation.com/way2auto_jquery/index.php")
    # driver.set_page_load_timeout(10)
    # time.sleep(5)
    # driver.find_element_by_name("http://way2automation.com/way2auto_jquery/registration.php").send_keys(Keys.ENTER)
    # driver.set_page_load_timeout(5)
    # driver.find_element_by_name("fancybox").send_keys(Keys.ENTER)
    # try:
    #       EC.presence_of_element_located((By.ID, "btn btn-effect btn-info"))
    #   )
    # finally:
    #  driver.find_element_by_name("btn btn-effect btn-info").send_keys(Keys.ENTER)
    #  time.sleep(6)
    # driver.quit()
    # MyDynamicElement = driver.find_element_by_name("name")
    # driver.find_element_by_name("q").send_keys("Login")
    # driver.find_element_by_name("fancybox").send_keys(Keys.ENTER)


def tearDown(self):
    self.driver.quit()


if __name__ == "__main__":
    unittest.main()
