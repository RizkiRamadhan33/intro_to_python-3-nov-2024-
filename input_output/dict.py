# inisialisasi data

biodata_simple = {
    "nama" : "Rizki Ramadhan",
    "age" : 20,
    "tempat lahir" : "Jakarta"    
}

# cetak nilai
print(biodata_simple)

# mengambil nilai spesifik
# biodata_simple("nama")
print("Hello nama anda siapa : {nama}".format(nama= biodata_simple["nama"]))
# biodata_simple.get("age")
print("{nama} , saya berumur : {age}".format(nama = biodata_simple.get("nama"),
age = biodata_simple.get("age")))

# menambahkan key dan value
biodata_simple["tanggal_lahir"] = "20-sep-2000"
print("Data Setelah Diupdate")
print(biodata_simple)

# mengubah nilai
biodata_simple["tanggal_lahir"] = "20-sep-2000"
print("Setelah di ganti format tanggal lahirnya ")
print(biodata_simple)

# menghapus nilai
del biodata_simple["tanggal_lahir"]
print("Data setelah dihapus")
print(biodata_simple)


# check key yang ada
print("List Key : ")
print(biodata_simple)
print("list Value : ")
print(biodata_simple.values())
