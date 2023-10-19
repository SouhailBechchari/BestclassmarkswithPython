n = int(input("Tapez le nombre des etudiatns "))
T = []
for i in range(n):
    note = float(input("tapez la note de l'étudiant" ,i+1))
    T.append(note)
S = 0
for note in T:
    S = S + note
M = S / n
print("Les notes supérieures à la moyenne sont :")
for note in T:
    if note > M:
        print(note)

