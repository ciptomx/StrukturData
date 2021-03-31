#MEMBUAT LIST
num_list = [1, 2, 3, 4, 5, 99, 0, -1]
char_list = ['a', 'b', 'c', 'd', 'ea', 'LT']
drink_list = ['milk', 'coffee', 2021, 0.34]
item = drink_list[1] ntuk mengakses item dari suatu list

drink_list[2] = 'tea' #Jika ingin mengubah isi dari suatu list

#MENGHAPUS LIST
#Untuk menghapus isi suatu list ada tiga cara, masing-masing cara memiliki kegunaan tersendiri. yang pertama menggunakan keyword del
foods = ['chicken', 'potato', 'steak', 'burger', 'sushi']
del foods[0] #hapus dengan index-0

#yang kedua menggunakan function remove()
foods.remove('sushi')

#yang ketiga menggunakan function pop()
last_food = foods.pop()
foods.pop(1)

#MENAMBAHKAN LIST
menu = ['chicken', 'steak']

#gunakan insert(index, item_baru) untuk menambahkan index yg spesifik
menu.insert(1, 'potato') 

#gunakan append() untuk menambahkan item_baru (pada akhir index)
menu.append('soup') 
menu.append(['sushi', 'burger'])

#gunakan extend() untuk menambahkan item_baru (pada akhir index)
menu.extend(['sushi', 'burger']) 

#ingin tahu berapa banyak item yang ada dalam suatu list, gunakan function len():
jum = [23, 11, 41]
nums_length = len(jum)   #hasilnya jumlah list
  
