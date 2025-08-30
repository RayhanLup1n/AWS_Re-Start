# List

"""
    List Merupakan sebuah tempat atau wadah untuk menyimpan lebih dari 1 
    values pada sebuah variabel.
    
    List ditandai dengan menggunakan tanda kurung siku ([])
"""

myFruitsList = ['banana', 'apple', 'grape', 'muscat']
print(myFruitsList)


"""
    Kita dapat mengakses / mengambil variable tertentu yang tersimpan dalam
    sebuah list dengan menggunakan indexing. Hal ini karena salah satu sifat
    dari list adalah berurutan (Ordered).
    Setiap index dimulai dari angka 0, berarti jika ada 5 values yang tersimpan
    dalam 1 list, maka index nya dari 0-4
"""

print(f'Buah urutan kedua adalah {myFruitsList[1]}')
print(f'Buah urutan ketiga adalah {myFruitsList[2]}')

myFruitsList[3] = 'Cherry'
print(myFruitsList)
print(type(myFruitsList))

# Tuple

"""
    Secara fungsi tuple memiliki fungsi yang sama seperti list yaitu
    untuk menyimpan 1 atau lebih values dalam sebuah variabel.
    
    Yang menjadi perbedaan yang paling terlihat adalah tuple menggunakan tanda
    kurung () sendangkan list menggunakan kurung siku ([]).

    Selain itu tuple bersifat uneditable, yang artinya values yang sudah tersimpan
    dalam sebuah tuple tidak dapat diedit kecuali kita membuat tuple baru dengan
    menyimpan values baru.
"""

myTuple = ('Agus', 'Wawan', 'Alpukat', 'Avocado', 1, 3.14)
print(myTuple)
print(type(myTuple))