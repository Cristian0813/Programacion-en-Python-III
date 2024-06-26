
# Utilice el flujo de control y los bucles para resolver un problema: solución

# Paso 1
num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

for num in num_list:
    print(num)

# Paso 2
num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

for num in num_list:
    if num > 45:
        print(num)

# Paso 3
num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

for num in num_list:
    if num > 45:
        print('Over 45')
    else:
        print('Under 45')

# Paso 4
num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

for x,num in enumerate(num_list):
    if num == 36:
        print('Number found at ', x)

# Paso 5,6,7
num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

count = 0

for x,num in enumerate(num_list):
    count += 1
    if num == 36:
        print('Number found at ', x)

print(count)

# Paso 8
num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

count = 0

for x,num in enumerate(num_list):
    count += 1
    if num == 36:
        print('Number found at ', x)
        break