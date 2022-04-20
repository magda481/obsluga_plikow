import os
import sys
import csv
import json
import pickle


lista = []
string = []
wejscie = sys.argv[1]
wyjscie = sys.argv[2]

argumenty = sys.argv
zmiany = argumenty[3:]

if os.path.isdir(wejscie):
    print('Podana ścieżka to katalog a nie plik')
    print(os.listdir(wejscie))
elif os.path.exists(wejscie) == False:
    print('Plik nie istnieje')
else:
    with open(wejscie, 'r') as f:
        reader = csv.reader(f)
        for linia in reader:
            lista.append(linia)

# print("Lista wejściowa: ", lista)
for idx in range(len(zmiany)):
    b = zmiany[idx]
    c = b.split(',')
    string.append(c)

for idx in range(len(string)):
    b = string[idx]
    lista[int(b[0])][int(b[1])] = b[2]

print('Lista po wprowadzonych zmianach:')
print(lista)

sciezka, nazwa = os.path.split(wyjscie)
_, rozszerzenie = os.path.splitext(nazwa)
print(sciezka, nazwa, rozszerzenie)
zapis = (sciezka+'/'+nazwa)

if rozszerzenie == '.csv':
    with open(zapis, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(lista)
elif rozszerzenie == '.json':
    with open(zapis, 'w') as f:
        json.dump(lista, f)
elif rozszerzenie == '.pickle':
    with open(zapis, 'wb') as f:
        pickle.dump(lista, f)
else:
    print('Złe rozszerzenie pliku')
