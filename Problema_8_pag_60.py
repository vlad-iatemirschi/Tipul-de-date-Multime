A = set(map(int, input('Dati numare separatile prin spatiu: ').split()))
B = set(map(int, input('Dati numare separatile prin spatiu: ').split()))
print('Intersectia multimilor este ',A.intersection(B))
print('Reuniunea multimilor este', A.union(B))
print('Diferenta multimilor A-B=', A.difference(B))
print('Diferenta multimilor B-A=', B.difference(A))