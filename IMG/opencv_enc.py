# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 13:31:06 2021

@author: FADIL
"""

import cv2
import numpy as np

demo = cv2.imread("E:/KULIAH/TUGAS KULIAH/SEMESTER 3/Sistem Keamanan Data (Prak)/UAS/IMG/image.jpg", 0) # Memanggil file image
r, c = demo.shape
key = np.random.randint(0, 256, size=(r, c), dtype=np.uint8)  # Membuat random key image
cv2.imwrite("E:/KULIAH/TUGAS KULIAH/SEMESTER 3/Sistem Keamanan Data (Prak)/UAS/IMG/key.jpg", key)   # Menyimpan key image

cv2.imshow("demo", demo)  # Menampilkan image asli
cv2.imshow("key", key)  # Menampilkan key image

encryption = cv2.bitwise_xor(demo, key)  # Fungsi enkripsi
cv2.imwrite("E:/KULIAH/TUGAS KULIAH/SEMESTER 3/Sistem Keamanan Data (Prak)/UAS/IMG/hasil/image_enkripsi.jpg", encryption)  
   # Simpan hasil enkripsi image
decryption = cv2.bitwise_xor(encryption, key)  # Fungsi dekripsi
cv2.imwrite("E:/KULIAH/TUGAS KULIAH/SEMESTER 3/Sistem Keamanan Data (Prak)/UAS/IMG/hasil/image_dekripsi.jpg", decryption) # Save the decrypted image

cv2.imshow("encryption", encryption)  # Menampilkan enkripsi image
cv2.imshow("decryption", decryption)  # Menampilkan dekripsi image

cv2.waitKey(-1)
cv2.destroyAllWindows()