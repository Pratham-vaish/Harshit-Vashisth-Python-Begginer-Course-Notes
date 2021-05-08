#  and, or operator are used to check two condition in one line
# AND
print("your password should be 8 characters long")
Password = input("enter your new password.... ")
if len(Password) >= 8:
    pass
else:
    print("your password is shorter renter it")
    Password = input("renter.... ")
print("   ")
print("confirm password")
confirm_password = input("enter password again... ")
if Password == confirm_password and len(Password) >= 8:
    pass
else:
    print("wrong again")
    confirm_Password = input("renter.... ")
if Password == confirm_password:
    print("your new password "+ str(Password) )
print("   ")
input("PRESS ANY KEY TO CLOSE")
 