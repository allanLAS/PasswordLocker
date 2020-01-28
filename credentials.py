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
        