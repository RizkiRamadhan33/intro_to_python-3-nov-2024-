import random
def makeDist_generete(banyak_data):
    list_data = []
    for i in range(banyak_data):
        nilai_acak = random.randint(1,100)
        list_data.append(nilai_acak)
    return list_data

def bubble_short(data):
    n = len(data) #len itu function untuk mengukur banyak data dalam list

    for i in range(n):
        for j in range(0,n-i-1):
            if data[j] > data [j + 1]:
                data[j],data[j+1] = data[j+1],data[j]
                # temp

value = int(input("banyak data yang akan di looping :"))
list_data = makeDist_generete(value)
print("list data sebelum diurutkan")
print(list_data)
print("Data setelah diurutkan :")
bubble_short(list_data)
print(list_data)