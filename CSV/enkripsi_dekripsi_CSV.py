# Import modul
from cryptography.fernet import Fernet


# Membuat key
key = Fernet.generate_key()
 
# Menyimpan key
with open('CSV/filekunci.key', 'wb') as filekey:
   filekey.write(key)


# Pakai kunci
fernet = Fernet(key)
 
# Membuka file csv
with open('E:/KULIAH/TUGAS KULIAH/SEMESTER 3/Sistem Keamanan Data (Prak)/UAS/CSV/file_csv.csv', 'rb') as file:
    original = file.read()
     
# Enkripsi csv
encrypted = fernet.encrypt(original)
 
# Simpan file enkripsi
with open('E:/KULIAH/TUGAS KULIAH/SEMESTER 3/Sistem Keamanan Data (Prak)/UAS/CSV/hasil/enkrip.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)


#DEKRIPSI
    
# Pakai kunci
fernet = Fernet(key)

# Buka file hasil enkrpisi
with open('E:/KULIAH/TUGAS KULIAH/SEMESTER 3/Sistem Keamanan Data (Prak)/UAS/CSV/hasil/enkrip.csv', 'rb') as enc_file:
	encrypted = enc_file.read()

# Dekripsi csv
decrypted = fernet.decrypt(encrypted)

# Simpan file dekripsi
with open('E:/KULIAH/TUGAS KULIAH/SEMESTER 3/Sistem Keamanan Data (Prak)/UAS/CSV/hasil/deskrip.csv', 'wb') as dec_file:
	dec_file.write(decrypted)
