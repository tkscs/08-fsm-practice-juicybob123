# write code to implement a turnstile
x = 0
y = 0
balance = 2
loop = 1
while loop > 0:
    state = int(input("please chose from pushing with 1 or insert a coin with 2, or check your balance with 3. If you wish to go back press 4 or 5 if you want to leave this\n"))
    if state == 2:
        if x == 1:
            print("you already have a coin inserted")
        elif x == 0:
            if balance >= 1:
                x = 1
                print("you have successfully inserted a coin")
                balance = balance  - 1
            else:
                print("you do not have enough money")
    if state == 1:
        if x == 1:
            print("you have succesfully enterd")
            x = 0
            y = 1
        else:
            print("you must enter a coin first.")
    if state == 3:
        print(f"your balance is {balance} coins")
    if state == 4:
        if y == 1:
            print("you have successfully went back to the begining")
            y = 0
        elif y == 0:
            print("you are already at the back")
    if state == 5:
        if y == 0:
            print("you must be after the turnstile")
        elif y == 1:
            print("you have succesfully continued on")
            loop = -1