if 10 > 9:
    print("It is correct")

x = True
if x:
    print("It's correct")
    print('\n')

if 5 == 2:
    print("It's correct")
else:
    print("It's not correct ")
    print('\n')

# True statement will stop at the first response
# Negative statement like pet = fish will go till the end and print the last condition
pet = "puppet"
if pet == "cat":
    print("you have a cat")
elif pet == "puppet":
    print("You have a puppet")
    print("\n")
elif pet == "fish":
    print("You have a fish")
else:
    print("you have a bizarre pet")
    print("\n")

age = 16
school_grade = 12

if age < 17:
    print("you are a minor")
    if school_grade >= 12:
        print("passed")
    else:
        print("failed")
else:
    print("you are an adult")
