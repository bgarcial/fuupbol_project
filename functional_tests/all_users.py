from selenium import webdriver
import unittest

#TestCase class
class NewVisitorTest(unittest.TestCase):

    """
    setup() is a method which function is initialize the test
    In this case, open the browser and wait for three seconds
    just in case of the page don't load.
    """
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)


    '''
    tearDown() method is executed after of each test

    '''
    def tearDown(self):
        self.browser.quit()

    '''
    Testcase. With this method I ask open the broswser  and the
    url http://localhost:8000 and in the assert we says if
    in the html tag title is the text 'Welcome to Django'
    '''
    def test_it_worked(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Welcome to Django', self.browser.title)


"""
Only if python execute directly the file (not imported)
the unittest.main() function will be executed.
This function launch the Test runner unittest that identify the
differents tests defined through of methods that start with the test prefix
such as test_it_worked()
"""

if __name__ == '__main__':
    unittest.main(warnings='ignore')

"""
The setUp() and tearDown() methods are executed in the beginning and in the end
of each test method, that mean, of each method that have the prefix test such as
test_it_worked()
"""