class Matrix:
    satirSayisi = 0
    sutunSayisi = 0
    matrix = [[0 for x in range(satirSayisi)] for y in range(sutunSayisi)]

    def __init__(self, satir, sutun):
        self.satirSayisi = satir
        self.sutunSayisi = sutun
        self.matrix = [[int(input(f"{x}.satir, {y}. sutun: ")) for x in range(self.satirSayisi)] for y in
                       range(self.sutunSayisi)]
        print(self.matrix)

    def elemanAyarla(self):
        x = int(input("Satir:"))
        y = int(input("Sutun:"))
        self.matrix[x][y] = int(input("Sayi:"))

    def matrisToplami(self, mtx):
        if (mtx.satirSayisi == self.satirSayisi) & (mtx.sutunSayisi == self.sutunSayisi):
            sonuc = [[mtx.matrix[i][j] + self.matrix[i][j] for j in range(mtx.sutunSayisi)] for i in
                     range(mtx.satirSayisi)]
            print(f"Toplam sonucu:{sonuc}")
        else:
            print("Matrisler toplanamaz...")

    def matrisCarpimi(self, mtx):
        if mtx.sutunSayisi == self.satirSayisi:
            result = [[0 for x in range(mtx.satirSayisi)] for y in range(self.sutunSayisi)]
            for i in range(self.satirSayisi):
                for j in range(mtx.sutunSayisi):
                    for k in range(mtx.satirSayisi):
                        result[i][j] += self.matrix[i][k] * mtx.matrix[k][j]
            print(f"Carpım sonucu:{result}")
        else:
            print("Matrisler carpilamaz...")


m1 = Matrix(2,2)
m2 = Matrix(2,2)
m1.matrisCarpimi(m2)
m1.matrisToplami(m2)