# score = 75
# if score > 70:
#     print("good")
# else:
#     print("try harder")
#
## if ... else if .... else
def greeting(lang):
    if lang == "th":
        print("sawadee")
        print("สวัสดี")
    elif lang == "jp":
        print("konichiwa")
    elif lang == "kr":
        print("ann-yeong")
    else:
        print("hello")

## 
def meet_re(eng,interview,math = 0):
    if eng > 70 and interview > 80 and math > 50 :
        return True
    else:
        return False

greeting("th")

print(meet_re(80,90))

##################################################################
def ticket2(age,is_local):
    if (age <= 5 or age >= 60) and is_local:
        return 0
    else:
        return 100

def ticket_ternary(age,is_local):
    return 0 if (age <=5 or age >= 60)and is_local else 100

print(ticket2(90,False))

###############################################################
def demo(a):
    if a <= 10 and a <= 20:
        print("OK")
    else:
        print("not OK")

def demo2(a):
    if 10 <= a <= 20:
        print("OK")
    else:
        print("not OK")
