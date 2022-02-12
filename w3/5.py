def auth(login, password):
    if login == "l1" and password == "p1":
        print("ok")
    else:
        print("denied")

auth(password="p1", login="l1")
auth(login="l1", password="p1")