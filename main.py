import shutil
from constants import *
import os
import re

files = os.listdir(train_images_512)
files = [i for i in files if 'orig' not in i]

for file in files:
    if 'orig' in file:
        continue
    cls = re.search(r'_(.*)_', file).group(1)

    if not os.path.exists(train_images_keras + cls):
        os.makedirs(train_images_keras + cls)
    shutil.move(train_images_512 + file, train_images_keras + cls + '/')

