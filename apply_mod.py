# print(2016 % 4)
# print(2559 % 4)

def leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False

def leap_year_buddihist(year):
    if year %4 == 3:
        return True
    return False

print(leap_year(2016),2016 %4)
print(leap_year_buddihist(2559),2559 %4)
print(leap_year_buddihist(2558),2558 %4)

def is_even(n):
    return True if n % 2 == 0 else False
    # if n%2 ==0:
    #     return True
    # else:
    #     return False

def is_odd(n):
    # return ~is_even(n)
    return not is_even(n)

print(is_even(20))
print(is_odd(20))

def promotion(come,pay,per_head,pax):
    ''' come 4 ,pay 2 มา4จ่าย2
     มา 5 pay ??
     per_h = 100
     200 + 100 '''
    return (pax // come)*(pay*per_head)+(pax%come) * per_head

print(promotion(4,2,100,4))


