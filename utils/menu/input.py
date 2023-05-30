# Mendapat input dari User
def getInput(message="Please input your value!"):
    user_input = "_"
    while user_input == "_":
        user_input = input(message)
        if user_input == "":
            print("[!] please input your string")
            user_input = "_"
        else:
            break
    return user_input

def getInputInt(message="Please input your value!"):
    user_choice = -1
    while user_choice == -1:
        # ! kenapa pake try except ?? biar dpt erronya klo if else ga bisa
        try:
            # Block mungkin terjadi error
            user_choice = int(getInput(message))
        except:
            # Jika error lakukan hal berikut
            print("[!] Please input integer value!")
            user_choice = -1
    return user_choice