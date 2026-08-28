#Validate user input exercise
# username is no more 12 characters
# username must no contain digits
# username must no contai spaces 

username = input("Masukkan username anda: ")

if len(username) > 12:
    print("Your username can't be more 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't be contain spaces" )
elif not username.isalpha():
    print("Your username can't be contain digits")
else:
    print(f"welcome {username}!")