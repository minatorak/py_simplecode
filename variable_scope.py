x = "Shala"

def fn():
    x= "s1"
    print(x)
def fn0():
    x = "M "+x
    print("fn0 ",x)

def fn2():

    global x
    x = "M "+ x
    print("fn2",x)

print(x)
fn()
fn2()
print(x)