import tkinter as tk
from tkinter import messagebox

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
        raise ValueError("Operator tidak valid")

def hitung():
    try:
        A = [[int(entry_A[i][j].get()) for j in range(2)] for i in range(2)]
        if operator_var.get() in ['+', '-', '*']:
            B = [[int(entry_B[i][j].get()) for j in range(2)] for i in range(2)]
            hasil = operasi_matriks(A, B, operator_var.get())
        elif operator_var.get() == 's':
            skalar = int(skalar_entry.get())
            hasil = operasi_matriks(A, None, 's', skalar)
        else:
            messagebox.showerror("Error", "Operator tidak valid")
            return
        
        for i in range(2):
            for j in range(2):
                hasil_labels[i][j].config(text=str(hasil[i][j]))
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid")

root = tk.Tk()
root.title("Operasi Matriks")
root.configure(bg="#2c3e50")
root.geometry("800x600")
root.state('zoomed')

frame = tk.Frame(root, bg="#2c3e50")
frame.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(frame, text="Matriks A", bg="#3498db", fg="white", font=("Arial", 18, "bold")).grid(row=0, column=0, columnspan=2, pady=5)
entry_A = [[tk.Entry(frame, width=15, bg="#ecf0f1", font=("Arial", 16)) for _ in range(2)] for _ in range(2)]
for i in range(2):
    for j in range(2):
        entry_A[i][j].grid(row=i+1, column=j, padx=20, pady=20)

tk.Label(frame, text="Matriks B", bg="#e74c3c", fg="white", font=("Arial", 18, "bold")).grid(row=0, column=3, columnspan=2, pady=5)
entry_B = [[tk.Entry(frame, width=15, bg="#ecf0f1", font=("Arial", 16)) for _ in range(2)] for _ in range(2)]
for i in range(2):
    for j in range(2):
        entry_B[i][j].grid(row=i+1, column=j+3, padx=20, pady=20)

operator_var = tk.StringVar(value='+')
tk.Label(frame, text="Operasi", bg="#2ecc71", fg="white", font=("Arial", 18, "bold")).grid(row=3, column=0, pady=10)
tk.OptionMenu(frame, operator_var, '+', '-', '*', 's').grid(row=3, column=1)

skalar_entry = tk.Entry(frame, width=15, bg="#ecf0f1", font=("Arial", 16))
skalar_entry.grid(row=3, column=3)
tk.Label(frame, text="(Untuk skalar)", bg="#2c3e50", fg="white", font=("Arial", 16)).grid(row=3, column=4)

tk.Button(frame, text="Hitung", command=hitung, bg="#f1c40f", fg="black", font=("Arial", 16, "bold"), width=15).grid(row=4, column=0, columnspan=5, pady=20)

tk.Label(frame, text="Hasil", bg="#9b59b6", fg="white", font=("Arial", 18, "bold")).grid(row=5, column=0, columnspan=2, pady=5)
hasil_labels = [[tk.Label(frame, text="0", width=15, bg="#ecf0f1", font=("Arial", 16, "bold")) for _ in range(2)] for _ in range(2)]
for i in range(2):
    for j in range(2):
        hasil_labels[i][j].grid(row=i+6, column=j, padx=20, pady=20)

root.mainloop()