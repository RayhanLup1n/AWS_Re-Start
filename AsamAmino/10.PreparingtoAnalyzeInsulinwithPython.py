import os
from pathlib import Path

CleanData = 'malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn'

# Hitung Panjang awalnya 
print("Panjang awal variable :",len(CleanData))

# Hapus spasi dan validasi panjangnya (Berdasarkan perintah harusnya 110)
new_data = CleanData.replace(" ", "")
print("Panjang setelah spasi dihapus :",len(new_data))

# Definisikan setiap file dan ukuran panjangnya
files = [
    ('isinsulin', 24),
    ('binsulin', 30),
    ('cinsulin', 35),
    ('ainsulin', 21)
    ]
    
    
# Definisikan path outputnya
outdir = Path("/home/ec2-user/environment/AsamAmino")
print("Folder output:", outdir)


# validasi panjang karakter
total_expected = sum(length for _, length in files)
if len(new_data) != total_expected:
    raise ValueError(f"Panjang data ({len(new_data)}) tidak sama dengan total yang diharapkan ({total_expected}).")
    

# Melakukan looping untuk memasukkan ke dalam masing-masing files
pos = 0
for idx, (name, length) in enumerate(files):
    start, end = pos, pos + length
    segment = new_data[start:end]

    # Validasi panjang segmen
    if len(segment) != length:
        raise ValueError(
            f"Segmen ke-{idx} ({name}) panjangnya {len(segment)}, seharusnya {length} (range {start}:{end})."
        )

    # Simpan ke file
    filepath = outdir / f"{name}-seq-clean.txt"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(segment + "\n")

    print(f"[{idx}] {name}: {segment} (len={len(segment)}, range={start}:{end}) -> {filepath}")
    pos = end
    
# Cek Hasil
print("\nDaftar file hasil:")
for f in os.listdir(outdir):
    if f.endswith("-seq-clean.txt"):
        print(" -", f)