Maths = int(input("Enter your grades in Maths : "))
Physics = int(input("Enter your grades in Physics: "))
English = int(input("Enter your grades in English: "))
programming= int(input("Enter your grades in Programming: "))
History = int(input("Enter your grades in History: "))
avg = (Maths + Physics + English + English + History)/5

if(avg >= 90):
    print("Grade: A")
elif(avg >= 80 and avg < 90):
    print("Grade: B")
elif(avg >= 70 and avg < 80):
    print("Grade: C")
elif(avg >= 60 and avg <70):
    print("Grade: D")
else:
    print("Grade: Failed")
print('\n')

Science = int(input("Enter your grades in Science : "))
Language_art = int(input("Enter your grades in Language_art: "))
Geography = int(input("Enter your grades in Geography: "))
Social_Studies = int(input("Enter your grades in Social_Studies: "))
Electives = int(input("Enter your grades in History: "))
avg = (Science + Language_art + Geography + Social_Studies + Electives)/5
if(avg >= 90):
    print("Grade: A")
elif(avg >= 80 and avg < 90):
    print("Grade: B")
elif(avg >= 70 and avg < 80):
    print("Grade: C")
elif(avg >= 60 and avg <70):
    print("Grade: D")
else:
    print("Grade: Failed")
print('\n')