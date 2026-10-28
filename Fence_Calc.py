#Fence calculator of cost to perimeter

def num_check(question):

    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            # ask the user for a number
            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Main Routine Goes Here

keep_going = ""
while keep_going == "":
    width = num_check("Width: ")

    height = num_check("Height: ")

    perimeter = 2 * (height + width)

    print(f"The fences perimeter is {perimeter}")


    cost = num_check("Cost per meter: ")

    total_cost = cost * perimeter
    print(f"The fences total cost is ${total_cost}")
    keep_going = input("Press enter to keep going or any key to quit.")
    print()

print("Thank you for using the fence cost calculator.")
