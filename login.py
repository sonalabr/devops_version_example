









def login(user):
    if user == "admin":
        print("Welcome, admin!")
    else:
        print(f"Welcome, {user}!")

if __name__ == "__main__":
    login("guest")
