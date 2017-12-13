def rectangle(w,h): #dynamic typing
    # code block
    area = w*h
    return area

def triangle(w,h):
    area = .5 * w*h
    return area
#main
#test
'''
print("1. rectangle ")
print("2. triangle ")
n = input("select option ")
w = int(input("width = "))
h = int(input('height = '))

if n == "1":
    print(rectangle(w,h))
else:
    print(triangle(w,h))
'''
#test
# print(triangle(w,h)) ERROR



######### none return and void
def celsius_to_fah(celsius):
    return (celsius * 9/5)+32

def temperature_table():
    for c in range(0,101,5):
        f = celsius_to_fah(c)
        print("{}c = {}F".format(c,f))
    #return None
#test
#return_of_temperature_table = temperature_table()
#print(return_of_temperature_table)

def price_with_vat(amount):
    vat = amount*7 /107
    price = amount - vat
    return price,vat

#test
print(price_with_vat(107))
a = price_with_vat(200)
print(a,a[0],a[1],type(a))
a,b = price_with_vat(107)
print("a = ",a,"\nb = ",b)