def ucapan_selamat_datang(nama = "Robot"):
    print("Hello, {nama} Selamat datang di program yang saya mau testing !!!".format(nama = nama))

def penjumlahan (n1 , n2):
    return n1 + n2



nama = "Rizki"
n1 = 10
n2 = 20
# memanggil function
print("Function ucapa selamat datang")
ucapan_selamat_datang(nama)
print("Hasil dari penjumlahan {a} + {b} = {hasil}".format(a = n1 , b = n2 , 
hasil = penjumlahan(n1,n2)))