class person():
    def __init__(self, nama):       # mendefinisikan constructor
        print("construct class person", nama)
        self.nama =  nama
        self.__umur = 0             # private atribut

    @property
    def umur(self):
        return self.__umur

    @umur.setter
    def umur(self, value):
        self.__umur = self.__cek(value)             # mengakses private method __cek()
        
    def cetak(self):
        print(self.nama, self.__umur, sep=" , ")

    def __cek(self, x):
        if x in range(20, 31, 1):
            return x


class mahasiswa(person):
    def __init__(self, nama, nim=False):            # overriding constructor
        print("construct class Mahasiswa", nama)
        self.nim = nim
        person.__init__(self, nama)                 # memanggil parent constructor

    def cetak(self):                # overriding fungsi cetak()
        print(self.nim, end=", ")
        person.cetak(self)
    
ob1 = person("Dika")                # membuat instance class / objek
ob1.umur = 31                       # mengubah nilai property umur
ob1.cetak()                         # mengakses fungsi / method

ob2 = mahasiswa("Riko", 1234)       # membuat instance class / objek
ob2.nama = "Riko Londong"           # mengubah nilai atribut nama
print(ob2.umur)                     # mengakses nilai property umur
ob2.cetak()

print(type(ob1))
print(type(ob2))
