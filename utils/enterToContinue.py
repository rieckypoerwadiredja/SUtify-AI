import keyboard

def enter_to_continue(message="Press [enter] to continue..."):
    print(message)
    keyboard.wait("enter")
    print("\n")