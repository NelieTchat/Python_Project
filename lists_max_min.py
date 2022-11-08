# Returning the largest and the smallest numbers using min and max.

list = [18, 29, 31, 42, 53]
list1 = [-14, -25, -36, -47]
list2 = list + list1

print('case1')
if len(list2) > 0 or len(list2) < 0:
    print(max(list), min(list), '\n')
    print(max(list1), min(list1), '\n')
else:
    print('None')

print('case2')
if len(list2) == 0:
    print(max(list1), min(list1), '\n')
    print(max(list), min(list), '\n')
else:
    print('None')