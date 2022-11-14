# Program that translates French to English and French to Bulgarian.

french_english = {"rouge" : "red" ,
         "vert" : "green",
         "bleu" : "blue",
         "prune" : "plum",
         "jaune" : "yellow"}

french_bulgarian = {"prune": "слива",
          "cerise": "череша",
          "mangue": "манго",
          "pomme": "ябълка",
          "ananas" : "ананас"}

print('case1')
my_dic = input("choose bulgarian or english dic :  ")
my_dic = my_dic.lower()
query = input("which word would you like to translate? : ")
query = query.lower()

if my_dic == 'bulgarian':
    if query in french_bulgarian:
        print(french_bulgarian.get(query), '\n')
    else:
        print(f'{query} will be added later on. \n')
elif my_dic == 'english':
    if query in french_english:
        print(french_english .get(query), '\n')
    else:
        print(f'{query} will be added later on.\n')
        print()


print('case2')
my_dic = input("choose bulgarian or english dic :  ")
my_dic = my_dic.lower()
query = input("which word would you like to translate? : ")
query = query.lower()

if my_dic == 'bulgarian':
    if query in french_bulgarian:
        print(french_bulgarian.get(query), '\n')
    else:
        print(f'{query} will be added later on.\n')
elif my_dic == 'english':
    if query in french_english:
        print(french_english .get(query), '\n')
    else:
        print(f'{query} will be added later on.\n')