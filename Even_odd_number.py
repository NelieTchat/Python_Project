# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

number = int(input("Enter any number between 1-100: "))
if number % 2 == 0:
    print(f'your number {number} is even.')
else:
    print(f'your number {number} is odd.')
