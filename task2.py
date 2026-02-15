size = int(input())

list1 = []
list2 = []

for i in range(size):
    list1.append(int(input()))

for i in range(size):
    list2.append(int(input()))

print(list1)
print(list2)

list3 = list1 + list2
print(list3)

no_repeat = []
for i in list3:
    count = 0
    for j in no_repeat:
        if i == j:
            count += 1
    if count == 0:
        no_repeat.append(i)
print(no_repeat)

common = []
for i in list1:
    for j in list2:
        if i == j:
            count = 0
            for k in common:
                if k == i:
                    count += 1
            if count == 0:
                common.append(i)
print(common)

unique = []
for i in list1:
    count = 0
    for j in list2:
        if i == j:
            count += 1
    if count == 0:
        unique.append(i)

for i in list2:
    count = 0
    for j in list1:
        if i == j:
            count += 1
    if count == 0:
        unique.append(i)

print(unique)

min1 = list1[0]
max1 = list1[0]
for i in list1:
    if i < min1:
        min1 = i
    if i > max1:
        max1 = i

min2 = list2[0]
max2 = list2[0]
for i in list2:
    if i < min2:
        min2 = i
    if i > max2:
        max2 = i

print([min1, max1, min2, max2])
