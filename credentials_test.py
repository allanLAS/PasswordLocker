import unittest
from credentials import Credentials

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        method that will run before each test case
        '''

        self.new_credential = Credentials("facebook", "allanLumush", "safepass")
    def tearDown(self):
        '''
        cleans after each test case has been executed
        '''
        Credentials.credential_list = []

    def test_init(self):
        '''
        testing proper initialization of an object
        '''
        self.assertEqual(self.new_credential.app_name,"facebook")
        self.assertEqual(self.new_credential.account_name,"allanLumush")
        self.assertEqual(self.new_credential.account_password,"safepass")

    def test_save_newcredential(self):
        '''
        testing if credential object is saved into credential list
        '''
        self.new_credential.save_newcredential()
        self.assertEqual(len(Credentials.credential_list),1)

    def 
    