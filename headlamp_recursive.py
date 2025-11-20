# states

# inputs

# transitions

# starting state

# ending states

# possible states are: black, white, red, in drawer
current_state = "black"

# every time through the loop, we...
# get a new input
# transition to the next state

while current_state != "in drawer":

    # Experience being in the state that we're in
    if current_state == "black":
        print("Light is OFF")
    elif current_state == "white":
        print("White light is ON")
    elif current_state == "red":
        print("Red light is ON")
    else:
        print(f"Error! The state {current_state} does not exist")
        

    # get the input
    current_input = input("You can click press (c), hold press (h), or do nothing (n) or put it away (p). Which one do you want? ")

    # transition to the next state based on the current state and the input
    if current_state == "black":
        # handle each input
        if current_input == "c":
            current_state = "white"
        elif current_input == "h":
            current_state = "red"
        elif current_input == "n":
            current_state = "black"
        elif current_input == "p":
            current_state = "in drawer"
        else:
            print(f"Error! I don't recognize the input {current_input}")
    elif current_state == "white":
        # handle each input
        if current_input == "c":
            current_state = "black"
        elif current_input == "h":
            current_state = "red"
        elif current_input == "n":
            current_state = "white"
        elif current_input == "p":
            current_state = "in_drawer"
        else:
            print(f"Error! I don't recognize the input {current_input}")
    elif current_state == "red":
        # handle each input
        if current_input == "c":
            current_state = "black"
        elif current_input == "h":
            current_state = "white"
        elif current_input == "n":
            current_state = "red"
        elif current_input == "p":
            current_state = "in_drawer"
        else:
            print(f"Error! I don't recognize the input {current_input}")
    elif current_state == "in_drawer":
        break
    else:
        print(f"Error! The state {current_state} does not exist")