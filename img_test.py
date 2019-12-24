import cv2

origin = cv2.imread(r'imgs/1.jpg')

print(origin.shape)
print(len(origin[:][:]))
print(origin)

cv2.imshow("1", origin)
cv2.waitKey(0)