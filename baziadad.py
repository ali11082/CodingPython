a=0
h=0
r="hichi"
while (r!="ok"):
    print(h,"man hadsam :    ",h, " bood")
    import random
    h=random.randint(0,99)
    print("man hadsam: ",h," ast." )
    r=input("age adadam bozorgtare benevis b va age hadsam koochiktar boodesh benvis k va age dorost goftam benevis ok:   ")
    if r=="ok":
        print("tamam tamam")
    elif r=="k":
        h=random.randint(h,99)
    elif  r=="b":
        h=random.randint(1,h)
    else:
        print("vorodit motabar nis")