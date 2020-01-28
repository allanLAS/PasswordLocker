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

    def test_save_multiplecredential(self):
        '''
        testing if we can save multiple credentials to the credential list
        ''' 
        self.new_credential.save_newcredential()
        test_credential = Credentials("testapp","testuser","testpass")
        test_credential.save_newcredential()
        self.assertEqual(len(Credentials.credential_list),2)

    def test_deletecredential(self):
        '''
        to test if we can delete a credential
        from our credential list
        '''
        self.new_credential.save_newcredential()
        test_credential = Credentials("testapp","testuser","testpass")
        test_credential.save_newcredential()
        self.new_credential.deletecredential()
        self.assertEqual(len(Credentials.credential_list),1)

    def test_find_credentialbyappname(self):
        '''
        test to check if we can find a credential by using
        the application name and display information
        '''
        self.new_credential.save_newcredential()
        test_credential = Credentials("newapp","testuser","testpass")
        test_credential.save_newcredential()
        found_credential = Credentials.find_credentialbyappname("newapp")
        self.assertEqual(found_credential.account_name,test_credential.account_name)