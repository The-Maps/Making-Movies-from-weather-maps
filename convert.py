import glob

import cv2

# 画像の読み込みの準備
img_list = []
file_list = sorted(glob.glob("images/195909*.jpg"))

# 画像を読み込んでリストに追加
for filename in file_list:
    img = cv2.imread(filename)
    img = img[:795,:1170,:] #トリミング
    img_list.append(img)

# 書き込みの準備
movie_name = 'isewan.mp4'
fps = 5.0
size = (1170,795)
out = cv2.VideoWriter(
    movie_name, cv2.VideoWriter_fourcc(*'mp4v'),
    fps, size)

# 動画を書き込み
for img in img_list:
    out.write(img)

out.release() # 動画を保存
