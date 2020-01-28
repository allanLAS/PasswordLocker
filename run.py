from user import User
from credentials import Credentials 


###user

# creating a user
def create_user(firstName, lastName, email, password):
    new_user = User(firstName, lastName, username, email, password)
    return new_user

##saving users
def save_user(user):
    user.save_user()

#display all users
def display_allusers():
    return User.display_allusers()

#generate a random password
def generate_randompass():
    return User.generate_randompass()


