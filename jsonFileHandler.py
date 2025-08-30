# Functions, Modules dan Libraries

"""
    - Functions = Sebuah code yang digunakan untuk menyelesaikan permasalah kecil yang berulang
    - Modules = Memiliki scope yang lebih luas dari sebuah functions, dan biasanya isi dari modules
        adalah gabungan dari beberapa functions
    - Libraries = Gabungan / Kumpulan dari beberapa modules
"""

# Library Standard Python

"""
    - Library Standar Python adalah kumpulan modul (file berisi fungsi/kelas) yang sudah disediakan Python. 
    Dengan ini, kita tidak perlu menulis ulang perintah/fitur yang umum dipakai.
    - Modul Python tidak selalu ditulis dengan Python saja—banyak yang ditulis dengan bahasa C agar kinerjanya cepat, lalu bisa dipakai dari Python.
    - Inti analogi “tidak menciptakan roda lagi”: 
        saat membuat sesuatu yang baru, kita memakai komponen yang sudah ada dari library. 
        Seperti membuat mobil dengan “roda” yang sudah jadi, bukan bikin roda dari nol.
        
    Contoh mini:
    
        import math
        print(math.sqrt(9))  # pakai modul math dari library standar

    Kesimpulan: Gunakan library standar/modul yang sudah tersedia agar pekerjaan lebih cepat, mudah, dan andal.
"""


# Navigating the Python Standard Library

"""
    - Python Standard Library = kumpulan modul bawaan Python. 
        Fungsinya untuk mempermudah pemrograman agar tidak perlu menulis ulang fitur yang umum.
    - Di dalamnya ada banyak modul siap pakai, misalnya:
        1. 'time' untuk kerjaan waktu/jam,
        2. 'sys' untuk info dan pengaturan terkait interpreter/system,
        3. os untuk berinteraksi dengan sistem operasi,
        4. dan banyak lagi.
    - Kenapa dipakai? Karena membuat kode lebih ringkas, mudah dirawat, dan mudah dipindahkan ke platform lain (Windows, Linux, macOS) —  modul standar tersedia di semua instalasi Python.
    - Contoh cepat:
    
        import time, os, sys
        
        print(time.strftime("%Y-%m-%d %H:%M:%S"))  # fitur waktu
        print(os.getcwd())                          # direktori kerja saat ini
        print(sys.version)                          # versi Python
    
    Jadi, kalau bisa pakai library standar, pakailah—hemat waktu dan lebih rapi.
"""

# Pentingnya menggunakan modules

"""
    - Mengulang pakai kode (reusability) → Pakai fungsi yang sudah teruji, sehingga lebih kecil kemungkinan muncul bug.
    - Ada dokumentasi resmi → Saat mengimpor modul, kamu bisa mengacu ke dokumentasinya untuk tahu cara pakai yang benar.
    - Belajar sekali, pakai berkali-kali → Modul yang umum bisa dipelajari sekali lalu dipakai di banyak proyek.
    - Kode lebih mudah dipahami tim lain → Jika kamu memakai modul yang umum dipakai, developer lain lebih cepat mengerti alur kodenya.
    
    Singkatnya: impor modul = hemat waktu, lebih aman, konsisten, dan mudah dirawat.
"""

# Tipe - Tipe modules (Sumber Modules)

"""
    1. Dibuat sendiri (created by you)
        Kamu mengelompokkan fungsi/kelas yang sering dipakai ke dalam satu file .py agar rapi dan bisa dipakai ulang.
        Contoh: my_utils.py lalu dipakai dengan import my_utils.
        
    2. Dari pihak luar (external sources)
        Modul dibuat orang lain dan umumnya di-instal lewat pip.
        Contoh: pip install requests lalu import requests.
    
    3. Bawaan Python (prepackaged / standard library)
        Sudah ikut terpasang saat instal Python, sehingga tidak perlu instal apa pun.
        Contoh: math, time, random.
        
        import math, time, random


    Kesimpulan: Modul bisa kamu tulis sendiri, ambil dari komunitas, atau pakai yang sudah bawaan Python. 
        Tujuannya supaya kode lebih terstruktur, mudah dipakai ulang, dan hemat waktu.
"""


# Importing Modules

"""
    Kamu wajib mengimpor sebelum dipakai, meskipun modul itu bawaan Python. Ada dua cara utama:
    
    1. Impor seluruh modul
        import math
        math.pi        # akses konstanta pi
        math.exp(3)    # fungsi e**3
    
    Kelebihan: nama tetap jelas (math.), kecil risiko bentrok nama.
    
    2. Impor bagian tertentu dari modul
        
        from math import pi, exp
        pi          # langsung pakai tanpa 'math.'
        exp(3)
        
    Kelebihan: lebih singkat; hati-hati potensi bentrok nama.
    
    Tips:
    
    - Bisa pakai alias kalau perlu singkat tapi tetap jelas:
    
        import math as m
        m.sqrt(16)
        
    - Hindari from math import * agar tidak mengacaukan nama-nama di ruang kerja.
    
    Ringkasnya: pakai import untuk mengambil modul; pakai from … import … untuk mengambil fungsi/konstanta tertentu.
"""

# Exception Handling (Penanganan Pengecualian)

"""
    - Tujuan: Mengatur alur program saat terjadi error runtime supaya program tidak langsung berhenti/crash.
    - Caranya: Pakai blok try / except.
        1. Kode yang “rawan error” taruh di try.
        2. Jika muncul error tertentu, Python loncat ke except untuk ditangani.
    
    Contoh pada slide

        def divide_five_by(number):
            try:
                value = 5 / number
            except ZeroDivisionError:
                print('Divide by zero error')
                value = 1          # nilai pengganti/default
            return value
        
        print(divide_five_by(2))  # -> 2.5 (berhasil)
        print(divide_five_by(0))  # cetak pesan error, lalu -> 1
        
    Saat number = 2, pembagian berhasil → mengembalikan 2.5.
    Saat number = 0, terjadi ZeroDivisionError → ditangkap di except, cetak pesan, lalu kembalikan 1 sebagai nilai aman.
    
    Tips bagus:
    
    1. Tangkap jenis error yang spesifik (mis. ZeroDivisionError), jangan except: kosong.
    2. Bisa tambahkan else (jalan jika tidak ada error) dan finally (selalu jalan, untuk bersih-bersih).
"""

def divided_number(num):
    try:
        value = 5 / num
    except ZeroDivisionError:
        print('Divided by Zero Error')
        value=1
    return value
    
"""
print(divided_number(3))
print(divided_number(0))
"""

# JSON (JavaScript Object Notation)

"""
    1. Apa itu JSON?
    => Format data standar berbentuk teks (string) untuk menukar/mengirim data. JSON tidak tergantung bahasa—bisa dipakai di JavaScript, Python, Java, dll.
    
    2. Fungsinya:
    => Untuk serialize objek—mengubah data (mis. dictionary/objek) menjadi string agar mudah dikirim lewat jaringan atau disimpan; dan sebaliknya bisa deserialize kembali ke objek.

    3. Contoh di gambar:
    
    Sebuah objek JSON berisi:
        - kunci users dengan array daftar orang (name, age),
        - kunci lain seperti dataTitle dan swiftVersion.
        
    Ciri JSON: kunci dan string pakai tanda kutip ganda "...", angka tanpa kutip, pakai { } untuk objek dan [ ] untuk array.
    
    4. Kenapa populer?
    => Ringkas, mudah dibaca manusia/mesin, dan didukung hampir semua bahasa pemrograman (termasuk Python).
    
    Contoh singkat di Python:

        import json
        
        # string JSON -> objek Python (deserialize)
        s = '{"users":[{"name":"John","age":25}], "dataTitle":"JSON Tutorial"}'
        data = json.loads(s)
        print(data["users"][0]["name"])  # John
        
        # objek Python -> string JSON (serialize)
        out = json.dumps(data, indent=2, ensure_ascii=False)
        print(out)
        
    Intinya: JSON adalah cara standar dan sederhana untuk mewakili dan bertukar data antar aplikasi.
    
    5. dump & dumps → serialize
    => Ubah data Python (dict/list) menjadi JSON.
        - dump → ke file
        - dumps → ke string
            Ingat: huruf s = string.
        - load & loads → deserialize
            Ubah JSON kembali jadi data Python.
        - load → dari file
        - loads → dari string
        
    Contoh cepat:
        
        import json
        
        data = {"name": "Ana", "age": 21}
        
        # ---> ke JSON
        s = json.dumps(data, indent=2, ensure_ascii=False)   # string
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False) # file
        
        # <--- dari JSON
        py1 = json.loads(s)                                  # dari string
        with open("data.json", "r", encoding="utf-8") as f:
            py2 = json.load(f)                               # dari file
    
    Ringkas: dump/load = file, dumps/loads = string.
"""

# pip

"""
    1. pip = package manager (manajer paket) untuk Python, mirip apt di Linux.
    2. Dipakai untuk menginstal paket pihak ketiga (sebuah paket berisi satu atau lebih modul/fitur Python yang bisa kamu import di kode).
    3. Biasanya terpasang bersamaan dengan Python.
    4. Dijalankan dari command line/terminal, bukan dari dalam interpreter Python.
    
    Contoh dasar:
        
        # instal paket
        pip install requests
        
        # jika punya beberapa versi Python
        python -m pip install requests     # cara aman
        # atau: pip3 install requests
        
        # upgrade pip
        python -m pip install --upgrade pip
        
        # lihat paket terinstal
        pip list
        
        # hapus paket
        pip uninstall requests
        
    Best practice:
        
        # buat virtual environment (direkomendasikan)
        python -m venv .venv
        # aktifkan
        # macOS/Linux
        source .venv/bin/activate
        # Windows
        .\.venv\Scripts\activate
        
        # simpan/instal dari requirements
        pip freeze > requirements.txt
        pip install -r requirements.txt
        
    Intinya: pip memudahkan pasang/kelola library yang tidak termasuk library standar Python.
"""


# Praktik (Lab)

import json

"""def jsonReader(fileName):
    data = ""
    with open('files/insulin.json') as json_file:
        data = json.load(json_file)
    return data
    
# jsonReader('insulin')
"""

def readJsonFile(fileName):
    data = ""
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    
    return data

# print(readJsonFile('insulin.json')['molecularWeightInsulinActual'])