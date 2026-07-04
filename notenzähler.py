
n=0
w=0
t=7
while True:
    eingabe=input()
    if not eingabe.isdigit() :
        break
    x=int(eingabe)
    w=w+x
    n=n+1
    if x<t:
        t=x
if n>0:
    print("Durchschnitt:",w/n)
    print("Beste Note:", t)
elif n==0:
    print("fehler")




