kelas_A = {"Struktur Data", "Basis Data", "AI",
"Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI",
"Cloud Computing"}

matkulGabungan = kelas_A.intersection(kelas_B) #1
print(matkulGabungan)

matkulUnikA = kelas_A.difference(kelas_B) #2
print(matkulUnikA)

matkulUnikB = kelas_B.difference(kelas_A) #3

matkulUnikGabungan = matkulUnikA.union(matkulUnikB)
print(matkulUnikGabungan)

