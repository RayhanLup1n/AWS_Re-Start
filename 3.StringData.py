string1 = "This is new string"
print(string1)
print(type(string1))


firstString = 'Water'
secondString = 'fall'
completeString = firstString + ' ' + secondString
completeString = firstString + secondString
print(completeString)


# Working with input

"""
    Input adalah sebuah function yang dapat digunakan oleh python untuk berkomunikasi
    dengan pengguna dimana pengguna dapat memasukkan inputan sesuai dengan perintah
"""

nama = input("Silahkan masukkan nama anda : ")
print(nama)
print("Selamat Datang di kelas StringData,",nama)


warna = input("Apa Warna Kesukaan anda ? ")
hewan = input("Apa jenis hewan peliharaan anda ? ")
print("{}, Kamu suka hewan {} yang berwarna {}!".format(nama, hewan, warna))