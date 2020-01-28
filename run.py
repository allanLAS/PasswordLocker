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


#credentials
##creating a new credential
def create_credential(appname, accountname, passwordname):
    return new_credential

# saving the credentials
def save_newcredential(credentials):
    credentials.save_newcredential()

##delete a credential
def deletecredential(credentials):
    credentials.deletecredential()

#using appname to find password
def find_credentialbyappname(credentials):
    return Credentials.find_credentialbyappname(credentials)

 #checking if the credential exists
 def credential_exists(appname):
     return Credentials.credential_exists(appname)

#display all credentials
def display_allcredentials():
    return Credentials.display_allcredentials()   

##running
def main():
    print("Wagwan!Welcome to password locker.\n To proceed, use these short codes:\n ca - ")