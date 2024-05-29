with open('Modulo-2/test.txt', 'r') as file:
        data = file.readline()
        print(data)
print()


with open('Modulo-2/newfile.txt', 'w') as file:
        file.write("This is a new file created !!!")
print()


with open('Modulo-2/newfile2.txt', 'w') as file:
        file.writelines(["This is a new file created !!!", "\nThis is another line to be added."])
print()


with open('Modulo-2/newfile3.txt', 'a') as file:
        file.writelines(["\nThis is a new file created !!!", "\nThis is another line to be added."])
print()


try:
    with open('sample/newfile3.txt', 'a') as file:
            file.writelines(["\nThis is a new file created !!!", "\nThis is another line to be added."])
except FileNotFoundError as e:
       print("ERROR", e)
print()


with open('Modulo-2/sample.txt', 'r') as file:
       print(file.read())
print()     


with open('Modulo-2/sample.txt', 'r') as file:
       print(file.read(44))
print()     


with open('Modulo-2/sample.txt', 'r') as file:
       print(file.readline())
print()     

with open('Modulo-2/sample.txt', 'r') as file:
       data = file.readlines()
       for x in data:
              print(x)
print()     


