A=set(input('Introdu litere mari a alfabetului multimii A(prin spatiu) ').split())
a1=True
for x in A:
    if ((ord(x)<65)or(ord(x)>90)):
        a1=False
if a1==True:
    B=set(input('Introdu litere mari a alfabetului multimii B(prin spatiu) ').split())
    a2=True
    for y in B:
        if ((ord(y)<65)or(ord(y)>90)):
            a2=False
    if a2==True:
        print('intersectia multimilor=',A.intersection(B))
        print('reuniunea multimilor=',A.union(B))
        print('diferenta multimilor A-B=',A.difference(B))
        print('diferenta multimilor B-A=',B.difference(A))
    else:
        print("am rugat litere mari")
else:
    print("am rugat litere mari")