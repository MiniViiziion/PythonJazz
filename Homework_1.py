# input below will be for the user to investigate a given number in the multiplication table.
while True:
    user_input = input("Which number would you like to investigate (0 to exit):")
# this statement allows for a print statement to tell user that the value inputted is not an integer.
    try:
        user_input = int(user_input)
        break
    except ValueError:
        print("Invalid input. Please try an integer!!")
# this if statement is simple. If a 0 is placed as an input to investigate it will exit the program.
if user_input == 0:
    run = False
# this else statement below handles the exceptions and conditions for the min and max. The invalid inputs and and the maximum of 10.
else:
    def getInput(prompt="", cast=None, condition=None, errorMessage=None):
        while True:
            try:
                response = (cast or str)(input(prompt))
                assert condition is None or condition(response)
                return response
            except:
                print(errorMessage or "Invalid input. Please try again!")
    minimum = getInput(prompt="Set the minimum:",
                    cast = int,   
                    errorMessage = "Invalid must be an integer!!")
    maximum = getInput(prompt="Set the maximum:",
                    cast = int,
                    condition = lambda i: i <= 10,
                    errorMessage = "Invalid. Must be integer or this exceeds maximum permitted!!")
# this for statement is the range and the calulcation part of the multiplication table.
    for i in range(minimum, maximum + 1):
        print(i,"x",user_input, "=", (i * user_input))
    



    

