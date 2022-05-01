import os
import sys
import csv
import json
import pickle

wejscie = "folder1/folder2/folder3/in.csv"
wyjscie = "katalog/katalog2/out.csv"
argumenty = sys.argv
zmiany = argumenty[1:]

lista = []



def sprawdz():

    if os.path.isdir(wejscie):
        print('Podana ścieżka to katalog a nie plik')
        print(os.listdir(wejscie))
    elif os.path.exists(wejscie) == False:
        print('Plik nie istnieje')


class CSV:
    def __init__(self):
        self.name = None

    def load(self):
        with open(wejscie, 'r') as f:
            reader = csv.reader(f)
            for linia in reader:
                lista.append(linia)
        return lista

    def zmiany(self):
        string = []
        for idx in range(len(zmiany)):
            b = zmiany[idx]
            c = b.split(',')
            string.append(c)

        for idx in range(len(string)):
            b = string[idx]
            lista[int(b[0])][int(b[1])] = b[2]
        print('Lista po wprowadzonych zmianach:')
        print(lista)

    def save(self):
        with open(zapis, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(lista)


class JSON(CSV):
    def load(self):
        with open(zapis, 'r') as f:
            json.load(lista, f)

    def save(self):
        with open(zapis, 'w') as f:
            json.dump(lista, f)


class PICKLE(CSV):
    def load(self):
        with open(zapis, 'r') as f:
            pickle.load(lista, f)

    def save(self):
        with open(zapis, 'w') as f:
            pickle.dump(lista, f)


sprawdz()

sciezka, nazwa = os.path.split(wyjscie)
_, rozszerzenie = os.path.splitext(nazwa)
os.makedirs(sciezka)
zapis = (sciezka + '/' + nazwa)

obiekt = CSV()
obiekt.load()
obiekt.zmiany()

if rozszerzenie == '.csv':
    obiekt.save()
elif rozszerzenie == '.json':
    obiekt = JSON()
    obiekt.save()
elif rozszerzenie == '.pickle':
    obiekt = PICKLE()
    obiekt.save()
else:
    print('Złe rozszerzenie pliku')
