def operasi_matriks(A, B, operator, skalar=None):
    if operator == '+':
        return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    elif operator == '-':
        return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    elif operator == '*':
        return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    elif operator == 's':  # Operasi perkalian dengan skalar
        return [[skalar * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    else:
        raise ValueError("Operator tidak valid, gunakan '+', '-', '*', atau 's' untuk skalar")

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

operator = input("Masukkan operasi ('+' untuk penjumlahan, '-' untuk pengurangan, '*' untuk perkalian, 's' untuk skalar): ")

if operator in ['+', '-', '*']:
    hasil = operasi_matriks(A, B, operator)
elif operator == 's':
    skalar = int(input("Masukkan nilai skalar: "))
    hasil = operasi_matriks(A, None, operator, skalar)
else:
    raise ValueError("Operator tidak valid")

# Menampilkan hasil
print("Matriks A:")
for baris in A:
    print(baris)

if operator in ['+', '-', '*']:
    print("Matriks B:")
    for baris in B:
        print(baris)

print(f"Hasil operasi:")
for baris in hasil:
    print(baris)
