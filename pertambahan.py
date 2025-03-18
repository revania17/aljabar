def tambah_matriks(A, B):
    hasil = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    return hasil

# Memasukkan matriks dari user
A = []
B = []

print("Masukkan elemen matriks A:")
for i in range(2):
    baris = list(map(int, input().split()))
    A.append(baris)

print("Masukkan elemen matriks B:")
for i in range(2):
    baris = list(map(int, input().split()))
    B.append(baris)

# Menjumlahkan matriks
hasil = tambah_matriks(A, B)

# Menampilkan hasil
print("Hasil penjumlahan matriks:")
for baris in hasil:
    print(baris)
