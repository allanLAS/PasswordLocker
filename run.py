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
    print("Wagwan!!Welcome to password locker.\n To proceed, use these short codes:\n ca - create an account using your own password \n ra - create an account using a randomly generated password \n ex - exit the application")
    short_code = input().lower()
    while True:

        if short_code == 'ca':
            print("Create an account using your own password")
            
            print("First Name")
            first_name = input()

            print("Last Name")
            last_name = input()

            print("User Name")
            user_name = input()

            print("Email")
            email_address = input()

            print("Password")
            pass_word = input()


            #create and save a new account
            save_user(create_user(first_name,last_name,user_name,email_address,pass_word))
            print('\n')
            print(f"Eureka! New Account {user_name} successfully created!")
            print('\n')
            print("Proceed with these short codes: \n lg - login into account \n ex - to exit the application")
            short_codetwo = input().lower()
            if short_codetwo == 'lg':
                print("-"*10)
                print("LogIn")
                print("To log in, input your username and password")

                print("UserName")
                user_namein = input()
                    
                print("Password")
                pass_wordin = input()

                ###verify the username and password
                if user_namein == u_name and pass_wordin == p_word:
                    print("Correct username and password.\n To proceed use the following shortcodes: \n cc - create a new credential \n dc - display credentials \n fc - find a credential by inputing the appname \n rc - to delete a credential \n ex - exit the application")
                    short_codethree = input().lower()
                    if short_codethree == 'cc':
                        print("-"*10)
                        print("To create a new Credential,Input the following.")
                        print("-"*10)

                        print("Application Name")
                        appli_name = input()

                        print("Account Name")
                        acc_name = input()

                        print("Password")
                        pass_name = input()
                            ###create and save a new credential
                        save_newcredential(create_credential(appli_name,acc_name,pass_name))
                        print('\n')
                        print("-"*10)
                        print(f"New Credential for {appli_name} created.")
                        print('\n')
                        print("-"*10)
                        continue
                       
                    
                    elif short_codethree == 'dc':
                        if display_allcredentials():
                            print("Here is a list of all your contacts")
                            print('\n')

                            for credentials in display_allcredentials():
                                print(f"{credentials.appli_name} {credentials.acc_name} {credentials.pass_name}")  
                                print('\n')
                        else:
                            print('\n')
                            print("You do not seem to have any credentials saved yet.")
                            print('\n')
                    elif short_codethree == 'fc':
                        print("Enter the application name for the credential you want to search for.")

                        search_applicationname =input()
                        if credential_exist(search_applicationname):
                            search_credential = find_credentialbyappname(search_applicationname)
                            print(f"{search_applicationname.appli_name} {search_applicationname.acc_name} {search_applicationname.pass_name}")                                             
                        else:
                            print("That credential doesnot exist.")
                else:
                    print("Wrong username or password.Please try again.")
                
            elif short_codetwo == 'ex':
                print("Bye Bye!")
                break
            else:
