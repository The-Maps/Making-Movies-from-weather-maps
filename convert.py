import glob

import cv2
size = (1170,795)

img_array = []
for filename in sorted(glob.glob("images/195909*.jpg")):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    img = img[:795,:1170,:] #トリミング
    #size = (width, height)
    #print(size)
    img_array.append(img)
#print(len(img_array))

name = 'isewan.mp4'
out = cv2.VideoWriter(name, cv2.VideoWriter_fourcc(*'mp4v'), 5.0, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
