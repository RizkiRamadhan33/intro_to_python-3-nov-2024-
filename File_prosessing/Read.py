# Case
# membaca file_laporan1.txt
# tampilkan
# "r" : Read file
# read 3
# readline
# read
open_file = open("file_laporan1.txt","r")
read_ = open_file.read()
print("Contoh read :")
print(read_)
#readline
open_file.seek(0) # gunanya untuk mengembalikan posisi pointer
read_line = open_file.readline(0)
print("Contoh penggunaan read line : ")
#gunanya untuk karakter
print(open_file.readline(120))
#readlines
open_file.seek(0)
print("Contoh penggunaan readlines : ")
for line in open_file.readlines():
    print(line.strip())