from deepface import DeepFace
import time
import matplotlib.pyplot as plt
import cv2 
img1 = cv2.imread("KinFaceW-II\\images\\father-dau\\fd_250_1.jpg")
# img2 = cv2.resize(img1,(128,128))
#cv2.imshow('win',img1)
plt.imshow(img1)
time.sleep(100000)
# print(img2.shape)
# exit()
# img2 = cv2.imread("KinFaceW-II\\images\\mother-dau\\md_250_1.jpg")
# cv2.imshow('win',img1)
#cv2.imshow('wi',img2)
# result = DeepFace.verify(img1_path = "KinFaceW-II\\images\\father-dau\\fd_250_1.jpg", img2_path = "KinFaceW-II\\images\\mother-dau\\md_250_1.jpg",enforce_detection=False)
# print(result)
# time.sleep(1000000)
