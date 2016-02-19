from selenium import webdriver
#import unittest
from django.core.urlresolvers import reverse
#from django.contrib.staticfiles.testing import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

#TestCase class
class NewVisitorTest(StaticLiveServerTestCase):

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

    # First, we define an auxiliar function named get_full_url
    # that takes one argument, the namespace which is an identifier
    # for a url self.live_server_url gives you the local host url. We use this
    # method because the test server uses another url
    # (usually http://127.0.0.1:8021), and this method is more flexible.
    # reverse gives you the relative url of a given namespace, here /
    # The resulting function gives you the absolute url of that namespace
    # (the sum of the previous two), http://127.0.0.1:8021/.
    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    # Test that the home page have in the title the word "NeuroRehabilitation"
    # We create a template for it. So, if that title exist, this mean that template
    # was loaded correctly
    def test_home_title(self):
        self.browser.get(self.get_full_url("home"))
        self.assertIn("NeuroRehabilitation", self.browser.title)

    # Test that h1 be of desired color. The css rule for text color will be a css file,
    # this mean that if the test passed (O.K.) then the static files are loaded correctly
    def test_h1_css(self):
        self.browser.get(self.get_full_url("home"))
        h1 = self.browser.find_element_by_tag_name("h1")
        self.assertEqual(h1.value_of_css_property("color"),
                         "rgba(200, 50, 255, 1)")

    '''
    Testcase. With this method I ask open the broswser  and the
    url http://localhost:8000 and in the assert we says if
    in the html tag title is the text 'Welcome to Django'

    def test_it_worked(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Welcome to Django', self.browser.title)
    '''


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