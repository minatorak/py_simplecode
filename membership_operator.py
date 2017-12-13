## check .....  in ..... (yes , no)
flowers = "lily","rose","daisy","tulip"

if "calla" in flowers:
    print("available")
else:
    print("not available")

sentence = "over the rainbow"
if "su" in sentence:
    print("ok")
else:
    print("not ok")

n = [10,8,15,30,60]
if 15.0 in n:
    print("n ok")

####### for .. in
for i in n:
    print(i)

def sum_number(num):# 083123456
    total = 0
    for one_num in num:
        total += int(one_num)
    return total

print("sum of number ",sum_number("0831234567"))