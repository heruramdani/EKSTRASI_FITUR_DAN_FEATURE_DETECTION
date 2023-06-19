# tampilkan kedua gambar
import cv2
from matplotlib import pyplot as plt
# panggil dan konversi warna agar sesuai dengan Matplotlib
sawit = cv2.imread('aadc2.png')
sawit = cv2.cvtColor(sawit, cv2.COLOR_BGR2RGB)
# panggil dan konversi warna agar sesuai dengan Matplotlib
kebun_sawit = cv2.imread('aadc.jpeg')
kebun_sawit = cv2.cvtColor(kebun_sawit, cv2.COLOR_BGR2RGB)
plt.subplot(121),plt.imshow(sawit), plt.title('Heru Ramdani')
plt.subplot(122),plt.imshow(kebun_sawit), plt.title('Foto selfie')
plt.show()