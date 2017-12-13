def loop1():
    for i in range(11): #for (i = 0;i<11;i++)
        print(i)

def loop2():
    for i in range(1,11,2): #for (i = 0;i<11;i=i+2)
        print(i)

    print("bye")



def loop_string():
    s = "over the rainbow"
    for c in s:
        print(c.upper())



loop_string()