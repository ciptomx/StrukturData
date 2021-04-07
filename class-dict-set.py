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
class mobil:
  warna = 'Hitam'
  transmisi = 'MT'
  gigi = 'N'

def __init__(self, transmisi):
  self.transmisi = transmisi
  print('Mobil Siap !')

def supir(self):
  self.gigi = 'D'
  print('Jalankan')

def mundur(self):
  self.gigi = 'N'
  print('Mundur.. Perhatikan bagian belakang mobil')

def gantigigi(self, gigi = 'N'):
  self.gigi = gigi
  print('Posisi Gigi : ' + self.gigi)

def ambilgigi(self):
  return self.gigi

  mobil1 = mobil('MT')
  mobil1.gantigigi('D')

  mobil2 = mobil('AT')
  gigi = mobil2.ambilgigi()
  print(gigi) 
