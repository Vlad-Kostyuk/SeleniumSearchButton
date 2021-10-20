import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class SearchButton(unittest.TestCase):
    page_url = "https://stackoverflow.com/"
    button_xpath = '//a[@href="https://stackoverflow.com/teams/create/free"]'

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_button(self):
        driver = self.driver
        driver.get(SearchButton.page_url)
        elem = driver.find_element(By.XPATH, SearchButton.button_xpath)
        elem.click()
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
