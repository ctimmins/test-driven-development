from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        #go to homepage and retrieve contents
        self.browser.get('http://localhost:8000')
        
        self.assertIn('To-Do', self.browser.title)
        self.fail('finished the test')
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')
    