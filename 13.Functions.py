# Functions

# Pengenalan Functions

"""
    Functions adalah sebuah kumpulan statements yang dicomplie / dirangkum
    ke dalam 1 kode secara utuh. Tujuan dari function adalah untuk mengorganisir
    sebuah kode dengan membaginya ke dalam beberapa potongan kecil yang sesuai
    dengan solusi untuk sebuah masalah
    
    Ada beberapa ketentuan dalam membuat function:
        1. Define the function (Mendefinisikan fungsi tersebut)
            Untuk mendefinisikan sebuah function, kita menggunakan keywords
            yang sudah ditentukan yaitu 'def'
        
        2. Name it and put placeholders arguments
            Setelah mendefinisikan sebuah function, kita harus memberikan nama
            untuk funtion tersbut dan tidak lupa untuk menambahkan argumen setelah
            nama functionnya
            Contoh: def Penjumlahan(Argumen):
            
        3. Indents lines of code inside of function like code in loops
            Setelah mendefinisikan nama functionnya, kita harus berikan indentasi 
            (1 tab) untuk menandakan bahwa itu adalah hal yang harus dilakukan oleh
            function tersebut, sama sepert looping.
            
        Maka secara umum untuk membuat function syntax nya adalah sebagai berikut:
            def <functionName>(Arguments):
                <thingsToDo>
"""

# Tujuan Function

"""
    Salah satu tujuan utama dari pembuatan function adalah reusability (penggunaan
    secara berulang). Dengan mendeklarasikan sebuah custom function, kita dapat
    menggunakan function tersebut dengan sekadar memanggil function tersebut.
    
    Salah satu contoh function bawaan yang sudah dibuatkan oleh python adalah
    'print()'
    
    Selain 'print()' beberapa function yang sudah disediakan oleh python diantaranya:
        1. print()
        2. open()
        3. sum()
        4. dict()
        5. and others.
        
    dengan menggunakan functions, kita hanya tinggal memasukkan perintahnya 
    / argumennya saja
"""

# Tipe-tipe functions

"""
    Argumen = value yang dimasukkan di dalam kurung
    
    Tipe-tipe functions adalah sebagai berikut:
        1. No Arguments Return, no Return Given (Non Fruitful)
            Function jenis ini tidak menerima masukkan argumen dan juga
            tidak memberikan return (values balik)
            
        2. Take argument or argumen, no return given (Non Fruitful)
            Function jenis ini menerima masukan / argumen, tetapi tidak mengembalikan
            argumen tersebut
            
        3. No Argumen Taken, Return sometihng (fruitful)
            Function jenis ini tidak menerima argumen, tetapi akan mengembalikan
            sebuah nilai (return)
            
        4. take argument or arguments, retunr sometihng (fruitful)
            Function jenis ini menerima masukkan / argumen, dan juga mengembalikan
            sebuah nilai (return)
"""


# Contoh dari sebuah function

def demo(x):
    y = x + 3
    print(y)

print('Ini contoh penggunaan function demo: ')    
demo(10)
print("======================================")


# Mengorganisir pekerjaan menggunakan function (Organizing code with functions)

"""
    Melakukan organisasi code dengan bantuan function akan memudahkan hidup kita
    sebagai seorang programmer. Dengan hal tersebut code kita akan semakin mudah
    untuk dibaca dan dipahami. Berikut contoh penerapan untuk menghitung radius
    lingkaran
"""

print('Calculating the radius of circle: ')
# defines the 'phi' value
phi = 3.14159

# calculates the area of circle for a given radius
def calculate_circle_area(radius):
    # pi multiplied by r squrred
    return phi*radius**2
    
r = int(input('Enter the radius of the circle: '))
area = calculate_circle_area(r)
print(area)
print("======================================")


# Supporting Function
def DoublingAlphabet(Alphabet):
    NewAlpha = Alphabet + Alphabet
    return NewAlpha
    
# print(DoublingAlphabet("Sze"))
# print("======================================")

def EncryptMess():
    EncryptedStr = input("Tolong masukkan pesan yang ingin di enkripsi: ")
    return EncryptedStr
    
# print(EncryptMess())
# print("======================================")

def CypherKey():
    NumberAcc = input("Tolong masukkan sebuah angka (Angka valid adalah 1-25): ")
    return NumberAcc
    
# print(CypherKey())


# Fungsi Utama untuk enkripsi
def encryptMessage(message, CypherKey, Alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper() # Buat pesan yang dienkripsi menjadi kapital sehingga bisa dicompare dengan salt
    for currentCharacter in uppercaseMessage: # Loop pada setiap karakter yang ada pada sebuah kalimat yang kita masukkan
        position = Alphabet.find(currentCharacter) # Menemukan indeks setiap karakter pada message
        newPosition = position + int(CypherKey) # Tambahkan indeks dengan CypherKey yang kita tentukan, dan dijadikan final shifting index
        if currentCharacter in Alphabet: # Jika sebuah karakter ditemukan dalam list Alphabet, maka:
            encryptedMessage = encryptedMessage + Alphabet[newPosition] # Simpan dalam sebuah variable 'encryptedMessage'
        else: # Jika karakter tidak ditemukan, semisal spasi, angka, spesial karakter maka:
            encryptedMessage = encryptedMessage + currentCharacter # Simpan value asli dalam 'encryptedMessage'
    return encryptedMessage # Hasil Akhir dari function adalah pesan yang terenkripsi di dalam encryptedMessage
    
def decryptMessage(message, CypherKey, Alphabet):
    decryptKey = -1 * int(CypherKey) # Geser ke posisi semula (ke kiri) sebanyak (x (ChyperKey) * -1)
    return encryptMessage(message, decryptKey, Alphabet) # Hasil Akhir dari function adalah pesan yang terenkripsi di dalam encryptedMessage
    
    
# Function untuk running function utama (Runner Function)
def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = DoublingAlphabet(myAlphabet) # ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ as Encryptor / Salt
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = EncryptMess() # Terima inputan message dar isuer. Message ini adalah karakter yang akan di enkripsi
    print(myMessage)
    myCipherKey = CypherKey() # Terima inputan berapa banyak shifting cypher dari user
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2) # Eksekusi Enskripsi
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2) # Eksekusi Dekripsi
    print(f'Decypted Message: {myDecryptedMessage}')
    
runCaesarCipherProgram()