import cv2
import numpy as np
import urllib.request
req = urllib.request.urlopen(str(input('url : ')))
image = np.asarray(bytearray(req.read()), dtype=np.uint8)
image = cv2.imdecode(image,cv2.IMREAD_COLOR)
cv2.imshow('displayed image',image)
cv2.waitKey(0)
cv2.imwrite('new_aks.jpeg',image)
cv2.destroyAllWindows()
#اینو url کن