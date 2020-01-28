import string
import secrets
import random

class Credentials:
    '''
    This class genrates a new instance of a user
    '''

    credential_list = []
    def __init__(self,app_name,account_name,account_password):
        '''
        initialises a new instance of a credential
        '''
        self.app_name = app_name
        self.account_name = account_name
        self.account_password = account_password

    def save_newcredential(self):
        Credentials.credential_list.append(self)
    def deletecredential(self):
        '''
        delete a credential from credential list
        '''
        Credentials.credential_list.remove(self)
    @classmethod
    def find_credentialbyappname(cls,name):
        '''
        Method that takes in appname and returns a credential that matches that appname.
        Args:
        appname to search for
        returns :
        credentials of the one that mayches the appname.
        '''
        for credentials in cls.credential_list:
            if credentials.app_name == name:
                return credentials