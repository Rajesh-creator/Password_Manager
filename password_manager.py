from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key


master_pwd = input("What is the master password? >> ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, encrypted_pass = data.split(" | ")
            try:
                decrypted_pass = fer.decrypt(encrypted_pass.encode()).decode()
            except Exception as e:
                print(f"Error: {e}")
                continue
            print(f"User: {user} | Password: {encrypted_pass}")q


def add():
    name = input("Account name: ")
    password = input("Password: ")
    encrypted_pass = fer.encrypt(password.encode()).decode()

    with open("passwords.txt", "a") as f:
        f.write(f"{name} | {encrypted_pass}\n")


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? >> ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
