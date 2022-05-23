water=int(input("enter the number"))
if water<1:
    print("more water needs to be filled")
elif water>1 and water<10:
    print("no need to fill water")
else:
     print("water overflow")