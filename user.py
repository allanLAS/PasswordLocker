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
        