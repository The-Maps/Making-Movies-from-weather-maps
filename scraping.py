"""
参考文献
https://note.nkmk.me/python-download-web-images/
"""

import os
import pprint
import time
import urllib.error
import urllib.request

def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)
    
url = 'http://agora.ex.nii.ac.jp/digital-typhoon/weather-chart/thumb/as/1280x960/188303/18830301_2.jpg'
dst_path = 'data/0.jpg'
download_file(url, dst_path)