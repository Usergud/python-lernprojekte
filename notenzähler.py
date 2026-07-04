
n=0
w=0
t=7
while True:
    eingabe=input()
    if eingabe=="ende" or eingabe=="end" or eingabe=="Ende":
        break
    x=int(eingabe)
    w=w+x
    n=n+1
    if x<t:
        t=x
print(w/n)
print(t)
