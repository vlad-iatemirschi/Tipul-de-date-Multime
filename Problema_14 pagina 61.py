A=set(input("Dati sirul de caractere:"))
B=set(input("Dati sirul de caractere:"))
print("Caracterele care se intalnesc cel putin un sir :",A.union(B))
print("Caracterele care apar in ambele siruri",A.intersection(B))
print("Caracterele care apar in primul nu apar in sirul doi",A.difference(B))