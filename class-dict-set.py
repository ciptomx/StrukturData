#TUPLE
ruangan = (4,6,9,10,7, 'Ruang Rahasia')
#print(ruangan[5])
saturuangan = (2,)
#print(saturuangan[0])
pemain = 23,24,21,'Single'
#print(pemain[1])

k = dict([('Jan', 1),('Feb', 2),('Mar',3)])
#print(k['Jan'])

(x, y, z) = 1, 2, 3
print(y)

nomor = (1, 2, 3)
(a, b, c) = nomor
print(c)

#SET
ikan = {'Cupang', 'Kembung', 'Lele'}
print(ikan)
ikan.add('Bilis')
print(ikan)
ikan.add('Kembung')
ikan.update(['Lele','Lele Dumbo'])
print(ikan)
ikan.discard('Patin')
print(ikan)

#DICT
mahasiswa = {
  'nama' : 'Rivo Budiansyah',
  'umur' : 19,
  'hobi' : {
      'makanan' : 'Indomie',
      'olahraga' : 'Sepak Bola'
  }
}

nama = mahasiswa['nama']
umur = mahasiswa.get('tgllahir')
print(nama)
print(umur)
hobi = mahasiswa['hobi']['olahraga']
print(hobi)

for kunci, nilai in mahasiswa.items():
  print(nilai)

#CLASS
#CLASS
class mobil:
    warna = 'Hitam'
    transmisi = 'Automatic'
    posisi_gigi = 'D'


    def __init__(self, transmisi): #Constructor
        self.transmisi = transmisi
        print('Mobil Siap !')


    def maju(self):
        self.posisi_gigi = 'D'
        print('Jalankan')


    def mundur(self):
        self.posisi_gigi = 'R'
        print('Mundur.. Perhatikan bagian belakang mobil')


    def gantigigi(self, gigi='D'):
        self.posisi_gigi = gigi
        print('Posisi Gigi : ' + self.posisi_gigi)


    def ambil_posisigigi(self):
        return self.posisi_gigi

mobil1 = mobil('Manual')
mobil1.gantigigi('D-1')

mobil2 = mobil('Automatic')
posisi_gigi = mobil2.ambil_posisigigi()
print(posisi_gigi)

Tesla = mobil('Automatic')

#Inheritance
class Tesla(Car):
    pass   # use 'pass' keyword to define class only

tesla = Tesla()
tesla.drive()

#Overriding
class Tesla2(mobil):
  def maju(self):
      super().maju()
      print('Gasss !!')

#Private Attribute/Function
__nomor_seri = '1231234'

def __ambil_nomor_seri(self):
  return self.__nomor_seri

#Polimorphism
class Oto:
  def bbm(self):
      return 'Bensin'

class Honda(Oto):
  pass

class Tesla(Oto):
  def bbm(self):
    return 'Listrik'

def cek_bbm(oto):
  print(oto.bbm())

cek_bbm(Tesla())
cek_bbm(Honda())
