testList = [3,4,2,6,'AKU',3,5,3,2]
print (testList)
print (testList[0])
teks = testList[4] 
print (teks)
#mengganti isi list sesuai index
testList[4] = 'SAYA'
#mengisi var dengan list
teks = testList[4]
print (teks)
print (testList)
#Menambahkan data di list
testList.append('KAMU')
print (testList)
print(len(testList))
testList.insert(0,'PERTAMA')
print (testList)
#mengganti isi data list
testList[10]='ANDA'
print (testList)
#menghapus list
#dengan fungsi del()
del testList[5:10]
print ('ini')
print (testList)
del testList[5]
print (testList)

for i in testList:
  #if i % 2 == 0:
    testList.remove(i)

print(testList)
print(len(testList))

testList.pop(1)
print(testList)

testList.append('AKHIR')
print(testList)

nilai_akhir = testList.pop()
print(testList)
print(nilai_akhir)
