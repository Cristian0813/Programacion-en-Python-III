# LISTA (LIST)

list1 = [1, 2, 3, 4, 5]
print(list1) 
list2 = ['A', 'B', 'C', 'D', 'E']
print(list2) 
list3 = ['Hello', 1, True, 40.22]
print(list3) 
list4 = [1, [2, 3, 4], 5, 6]
print(list4) 

print()
print("--------------------------------")
print()

list1 = [1, 2, 3, 4, 5]
list1.insert(len(list1), 6)
print(list1, sep=" ")

list1 = [1, 2, 3, 4, 5]
list1.append(7)
print(list1, sep=" ")

list1 = [1, 2, 3, 4, 5]
list1.extend([7, 8, 9])
print(list1, sep=" ")

list1 = [1, 2, 3, 4, 5]
list1.pop(4)
print(list1, sep=" ")

list1 = [1, 2, 3, 4, 5]
del list1[2]
print(list1, sep=" ")

list1 = [1, 2, 3, 4, 5]
for x in list1: 
    print('value: ', x)

print()
print("--------------------------------")
# ===============================================================
print()

# TUPLA (TUPLE)

my_tuple = 1, 'strings', 4.5, True
print(type(my_tuple))

my_tuple = 1, 'strings', 4.5, True
print(my_tuple.count('strings'))

my_tuple = 1, 'strings', 4.5, True
print(my_tuple.index(4.5))

my_tuple = 1, 'strings', 4.5, True
my_tuple[0] = 5
for x in my_tuple:
    print(x)


print()
print("--------------------------------")
# ===============================================================
print()

# COJUNTO (SETS)

set_a = {1, 2, 3, 4, 5}
set_a.add(6)
print(set_a)

set_a = {1, 2, 3, 4, 5}
set_a.remove(2)
print(set_a)

set_a = {1, 2, 3, 4, 5}
set_a.discard(2)
print(set_a)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a.union(set_b))

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a | set_b)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a.intersection(set_b))

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a & set_b)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a.difference(set_b))

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a - set_b)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a.symmetric_difference(set_b))

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a ^ set_b)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a[0])

print()
print("--------------------------------")
# ===============================================================
print()

# DICCIONARIOS (DICTIONARIES)

sample_dict = {1:'Coffee', 2:'Tea' , 3:'Juice'}
print(sample_dict[1])

sample_dict = {1:'Coffee', 2:'Tea' , 3:'Juice'}
sample_dict[2] = 'Mint Tea'
print(sample_dict)

sample_dict = {1:'Coffee', 2:'Tea' , 3:'Juice'}
del sample_dict[3]
print(sample_dict)

sample_dict = {1:'Coffee', 2:'Tea' , 3:'Juice'}
for key, value in sample_dict.items():
    print(str(key) + ":" + value)

print()
print("--------------------------------")
# ===============================================================
print()

# ARGUMENTOS CLAVE (ARGS - KWARGS - KEYWORD ARGUMENTS)

def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum
print(sum_of(4, 5, 6, 4, 5, 6))


def sum_of(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return round(sum, 2)

print(sum_of(coffee=2.99, cake=4.55, juice=3.99))
