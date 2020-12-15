import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IntegrationTesting(unittest.TestCase):

	def verifySentences(self, input, output):
		self.driver = webdriver.Firefox()
		self.driver.get("http://localhost:5000")
		time.sleep(2)
		elem = self.driver.find_elements(By.XPATH, '/html/body/form/center/p[2]/textarea')
		elem[0].send_keys(input)
		time.sleep(2)
		elem = self.driver.find_elements(By.XPATH, '/html/body/form/center/p[2]/input')
		elem[0].submit()
		time.sleep(30)
		elem = self.driver.find_elements(By.XPATH, '/html/body/center/span/div')
		self.assertEqual(elem[0].text[:10], output)
		time.sleep(2)
		self.driver.close()


	def test_verifyTemplateLoaded(self):
		self.driver = webdriver.Firefox()
		self.driver.get("http://localhost:5000")
		time.sleep(2)
		elem = self.driver.find_elements(By.XPATH, '/html/body/form/center/h1')
		self.assertEqual(elem[0].text, 'Finding similar tweets')
		self.driver.close()

	def test_verifySentences(self):

		pass
		self.verifySentences("I love Data engineering", '1“Obamacar')


if __name__ == '__main__':
	unittest.main()


# driver = webdriver.Firefox()
# driver.get("http://localhost:5000")
# elem = driver.find_element_by_name("p")
# print(elem)
# self.assertEqual(elem, 'test')