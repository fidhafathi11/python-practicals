def login_required(func):
    def wrapper():

        print("checkin login status...")
        func()
    return wrapper

@login_required
def open_dashboard():

    print("welcome to your dashboard!")


open_dashboard()