import string
import secrets
import random
import pyperclip

class User:
    """
    Class that generates a new instance of a user and creates a new account
    """

    user_list = []
    def __init__(self,first_name,last_name,user_name,email,password):
        """
        Initialize a new credential instance
        """

        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email = email
        self.password = password
    def save_user(self):
        User.user_list.append(self)
    @classmethod
    def display_allusers(cls):
        '''
        this method return a list of all the users
        '''
        return cls.user_list 

     def generate_randompass():
        '''
        this method generates a random password
        '''
        #the password should contain a capital letter, small letter, a digit and punctuation
        characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
        #password length



