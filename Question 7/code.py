# Question 7
"""A group of friends wants to split the total bill.
The program asks the user to enter the total bill
amount and the number of people, separated by a comma.
It then calculates how much each person should pay.
The program handles errors like dividing by zero
(if number of people is 0), missing commas, or invalid input.
After successful calculation,
it confirms that everything went well."""

# Source code

try:
    inp_msg = "Enter total bill, no of people (separated): "
    total_bill_str, no_of_people_str = input(inp_msg).split(",")

    total_bill = float(total_bill_str)
    no_of_people = int(no_of_people_str)

    per_person = total_bill / no_of_people
    print(f"Per person bill is {per_person:.2f} PKR")

except ZeroDivisionError:
    print("No of people should not be zero")
except ValueError:
    print("Missing commas or invalid input")
except:
    print("Something went wrong")
else:
    print("Calculation was successful, Everything went well")
finally:
    print("Program execution has ended")