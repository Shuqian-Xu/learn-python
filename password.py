password = "a123456"
i = 2
while i >= 0:
    inputPassword = input("Please input your password: ")
    if inputPassword == password:
        print("Login successful!")
        break
    else:
        if i != 0:
            print("Password incorrect! ", i ," times remaining.")
        else:
            print("Login failed!")
        i = i - 1