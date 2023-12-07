import cv2
import numpy as np
import matplotlib.pyplot  as plt

man = cv2.imread(r'D:\ML\openCV\man.jpg')
jwell = cv2.imread(r'D:\ML\openCV\2k.png')
print(man.shape)
print(jwell.shape)
man=cv2.resize(man,(900,900))
jwell=cv2.resize(jwell,(300,300))
man = cv2.cvtColor(man, cv2.COLOR_BGR2RGB)
jwell = cv2.cvtColor(jwell, cv2.COLOR_BGR2RGB)

x_offset = 300
y_offset = 570
x_end = x_offset + jwell.shape[1]
y_end = y_offset + jwell.shape[0]

man[y_offset:y_end,x_offset:x_end] = jwell
plt.imshow(man)
plt.show()
plt.imshow(man)
plt.show()
plt.imshow(jwell)
plt.show()
plt.imshow(blended)
plt.show()