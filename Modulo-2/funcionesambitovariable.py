# FUNCIONES

def calculate_tax(bill, tax_rate):
    return round(bill * tax_rate) / 100.00

print('Total Tax: ', calculate_tax(175.00, 15))
print('Total Tax: ', calculate_tax(164.33, 22))

#------------------------------------------------------------------------------

# PYTHON SCOPE

#global scope

my_global = 10

def fn1():

    enclosed_v = 8
    
    def fn2():
        local_v = 5
        print("Access to Gobal: ", my_global)
        print("Access to Enclosed: ", enclosed_v)
    