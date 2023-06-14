from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

'''def load_key():
    file - open("key.key", "rb")
    key = file.read()
    file.close()
    return key'''

master_pwd = input("What is the master password? ")
'''key = load_key() + master_pwd.bytes
fer = Fernet(key)'''


def view():
    with open("Password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "\npassword:", passw)

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("Password.txt", "a") as f:
        f.write(name + "|" +pwd +"\n")
        

while True:
    mode = input("Would you like to add a new passwrod or view existing ones?(view/add) ")
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
