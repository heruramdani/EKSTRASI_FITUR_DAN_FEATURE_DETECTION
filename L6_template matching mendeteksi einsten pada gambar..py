from matplotlib import pyplot as plt
import cv2

# Panggil dan konversi warna agar sesuai dengan Matplotlib
einstein = cv2.imread('aadc2.png')
einstein = cv2.cvtColor(einstein, cv2.COLOR_BGR2RGB)  # Simpan dengan nama yang sama

# Panggil dan konversi warna agar sesuai dengan Matplotlib
solvay = cv2.imread('aadc.jpeg')  # Perbaiki penulisan nama gambar
solvay = cv2.cvtColor(solvay, cv2.COLOR_BGR2RGB)

plt.subplot(121), plt.imshow(einstein), plt.title('Heru Ramdani')
plt.subplot(122), plt.imshow(solvay), plt.title('Selfie')
plt.show()