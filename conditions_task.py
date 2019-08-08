first_number = input("Enter the first number:   ")
second_number = input("Enter the second number:   ")
operation = input("Choose the operation(+,-,/,*):   ")
if first_number != int(first_number):
    print("number is invalid)
if second_number != int(second_number):
    print("number is invalid)
if operation == +:
    print("the answer is "+ (first_number + second_number))
elif operation == -:
    print("the answer is "+ (first_number - second_number))
elif operation == /:
    print("the answer is "+ (first_number/second_number))
elif operation == *:
    print("the answer is "+ (first_number*second_number))
else:
    print("Operation is invalid")
