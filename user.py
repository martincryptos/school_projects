def login(database, username, password):
    if (username in database) and (database[username] == password):
        print("Welcome!", username, password[:-4])
        return username
    elif (username in database) and (database[username] != password):
        print("username does not match password")
        return ""
    elif username not in database:
        print("User not found. Please register.")
    else:
        pass


def register(database, username):
    if username in database:
        print("Username already exists!")
        return ""
    else:
        print(f"Username {username} registered")
        return username
