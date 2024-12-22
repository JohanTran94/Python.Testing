'''''
password = ""
while password == "abc":
    password = input("Ange password: ")
    if password == "abc":
        print("Fel password! Försök igen!")
print("Inloggad")
'''

password = ""
while password != "abc":
    password = input("Ange password: ")
    if password != "abc":
        print("Fel password! Försök igen!")
    else:
        print("inloggat")
