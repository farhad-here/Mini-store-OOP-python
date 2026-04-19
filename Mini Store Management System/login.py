# for manager to login
def managerLogin() -> bool:
    """
    Handling the manager authentication to see if is accurate or not.
    """
    # username
    username = input("Username: ")
    # password
    __password = input("Password: ")
    # boolean
    return username == "admin" and __password == "1234"

