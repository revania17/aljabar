def operasi_matriks(A, B, operator):
    if operator == '+':
        return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    elif operator == '-':
        return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    elif operator == '*':
        return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    else:
        raise ValueError("Operator tidak valid, gunakan '+', '-', atau '*'")

# Memasukkan matriks dari user
A = []
B = []

print("Masukkan elemen matriks A (pisahkan dengan spasi):")
for i in range(2):
    baris = list(map(int, input().split()))
    A.append(baris)

print("Masukkan elemen matriks B (pisahkan dengan spasi):")
for i in range(2):
    baris = list(map(int, input().split()))
    B.append(baris)

# Memilih operasi
operator = input("Masukkan operasi ('+' untuk penjumlahan, '-' untuk pengurangan, '*' untuk perkalian): ")

# Melakukan operasi matriks
hasil = operasi_matriks(A, B, operator)

# Menampilkan hasil
print("Matriks A:")
for baris in A:
    print(baris)

print("Matriks B:")
for baris in B:
    print(baris)

print(f"Hasil matriks A {operator} B:")
for baris in hasil:
    print(baris)
