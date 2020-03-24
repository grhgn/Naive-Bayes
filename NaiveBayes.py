import csv
import numpy

def dataLuar():
    reader = csv.reader(open("TrainsetTugas1ML.csv"), delimiter=",")
    return list(reader)

def dataLuar2():
    reader = csv.reader(open("TestsetTugas1ML.csv"), delimiter=",")
    return list(reader)

def hitungJumlah(nilaiLebih, nilaiKurang, arrayHasil):
    arrayHasil.append('>50K') if nilaiLebih > nilaiKurang else arrayHasil.append('<=50K')
    return arrayHasil

def simpanData(List2):
    with open('TebakanTugas1ML.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerows(List2)

List = dataLuar(); List2 = dataLuar2()
jumlahLebih = sum(x.count('>50K') for x in List)
jumlahKurang = sum(x.count('<=50K') for x in List)
persenLebih = jumlahLebih / ( len(List) - 1 )
persenKurang = jumlahKurang / ( len(List) - 1 )
arraylebih = []; arrayKurang = []; arrayHasil = []
for i in range (1, len(List2)):
    List2[i].remove('')
    sementaraLebih = []; sementaraKurang = []
    for j in range (1, len(List2[i])):
        jumlahDikit = sum(x.count('<=50K') for x in List if List2[i][j] in x) / jumlahKurang
        jumlahBanyak = sum(x.count('>50K') for x in List if List2[i][j] in x) / jumlahLebih
        sementaraLebih.append(jumlahBanyak)
        sementaraKurang.append(jumlahDikit)
    sementaraLebih.append(persenLebih); sementaraKurang.append(persenKurang)
    arraylebih.append(sementaraLebih); arrayKurang.append(sementaraKurang)
    hitungJumlah(numpy.prod(arraylebih[i-1]), numpy.prod(arrayKurang[i-1]), arrayHasil)

for i in range (1, len(List2)):
    List2[i].append(arrayHasil[i - 1])
simpanData(List2)
print('Selesai lihat hasil di TebakanTugas')