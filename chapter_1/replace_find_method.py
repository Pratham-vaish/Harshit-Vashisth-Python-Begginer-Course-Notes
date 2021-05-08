password = "1   3   5     2  5    7              5"
#replace method is used to replace any chracter
password_2 = password.replace(" ", "")
print(password_2.replace("5", "6"))
#find method is used to find position of character
print(password_2.find("6", 7))
