a=int(input("enter the ages"))
b=int(input("enter the ages"))
c=int(input("enter the ages"))
if a>b and b>c:
    print("a is the oldest")
elif b>a and b>c:
    print("b is the oldest")
elif c>a and c>b:
    print("c is the oldest")
if a<b and b<c:
    print("a is the youngset")
elif b<a and b<c:
    print("b is the youngest")
elif c<a and c<b:
    print("c is the youngest")
else:
    print("same ages")