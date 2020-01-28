import unittest
from credentials import Credentials

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        method that will run before each test case
        '''

        self.new_credential = Credentials("facebook", "allanLumush", "mypass")
    def tearDown(self):
        '''
        cleans after each test case has been executed
        '''
        Credentials.credential_list = []

    