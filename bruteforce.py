'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zipfile import ZipFile

def password_crack(password_list,encrypted):
    ## This function will use the password list to open the file ##
    right_password = ""
    
    with open(password_list,'rb') as pl:
        ## iterate over the passwords ##
        for passwords in pl:
            passwords = passwords.rstrip()
            ### use those passwords to attempt to open the file`
            try:
                encrypted.extractall(pwd=passwords)
            except:
                print("Incorrect Password: " + str(passwords.decode()))
            else:
                right_password = passwords


    print("The right password is " + str(right_password.decode()))

def main():
    password_list = 'rockyou.txt'
    encrypted = ZipFile('enc.zip')
    password_crack(password_list,encrypted)


if __name__=="__main__":
    main()
