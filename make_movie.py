
import glob
import cv2
import numpy as np
from tqdm import trange
import os 
import sys

class MovieMaker:
    """
    動画を作るMovieMakerクラス
    """

    def __init__(self, img_dir, movie_size, fps = 1.0):
        self.img_dir = img_dir
        self.movie_size = movie_size
        self.fps = fps

    def write_movie(self, out_dir, movie_name):
        # 準備
        out_path = os.path.join(out_dir, movie_name + ".mp4")
        size = (self.movie_size[0] * 2, self.movie_size[1] * 2)
        out = cv2.VideoWriter(out_path, cv2.VideoWriter_fourcc(*'mp4v'), self.fps, size)
        
        # 画像のパスのリストを取得
        file_list = sorted(glob.glob(os.path.join(self.img_dir, "*.jpg")))
        for i in trange(len(file_list)):
            img = cv2.imread(file_list[i])
            large_img = np.zeros([size[1], size[0], 3], dtype="uint8")
            # 画像のサイズが大きい場合はトリミング
            if img.shape[0] >= self.movie_size[1]:
                img = img[:self.movie_size[1],:,:]
            if img.shape[1] >= self.movie_size[0]:
                img = img[:,:self.movie_size[0],:]
            # resize
            img = cv2.resize(img, (img.shape[1]*2, img.shape[0]*2))
            
            # 画像の方が小さい分は黒色で埋める
            large_img[:img.shape[0], :img.shape[1], :] = img
            out.write(large_img)
        
        out.release() # 動画を保存


if __name__ == "__main__":
    # 入力用の情報と動画の設定
    img_dir = os.path.join(os.path.dirname(__file__), "data") # 実行ファイルと同ディレクトリのdataディレクトリを選択
    movie_size = (1280, 960)
    fps = 30.0
    MM = MovieMaker(img_dir, movie_size, fps)
    
    # 出力用の情報
    out_dir = os.path.dirname(__file__) # 実行ファイルと同ディレクトリに保存
    movie_name = "test"
    MM.write_movie(out_dir, movie_name)
