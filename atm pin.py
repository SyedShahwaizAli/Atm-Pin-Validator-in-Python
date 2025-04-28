pin = "1234"
attempts = 3

while attempts > 0:
    user_pin = input("Enter your 4-digit PIN: ")
    if user_pin == pin:
        print("Welcome!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Wrong PIN. " + str(attempts) + " attempts remaining")
        else:
            print("Card Blocked!")