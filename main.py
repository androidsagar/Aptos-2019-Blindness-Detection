import shutil
from constants import *
import os
import re
import pandas as pd

# files = os.listdir(train_images_final)
# files = [i for i in files if 'orig' not in i]
#
# for file in files:
#     if 'orig' in file:
#         continue
#     cls = re.search(r'_(.*)_', file).group(1)
#
#     if not os.path.exists(train_images_keras + cls):
#         os.makedirs(train_images_keras + cls)
#     shutil.move(train_images_512 + file, train_images_keras + cls + '/')
#
# for file in files:
#     shutil.move(train_images_512 + file, train_images_final)
#
# csv = pd.read_csv(train_csv)
# csv['id_code'] = csv['id_code'] + '.png'
# csv['diagnosis'] = csv['diagnosis'].astype(str)
#
# df = pd.DataFrame(columns=['name', 'code'])
# # df['id'] = files[0]
# # df['code'] = re.search(r'_(.*)_', files[0]).group(1)
# df = df.append([{'name': files[0],'code':re.search(r'_(.*)_', files[0]).group(1)}])
# df = df.append([{'name': files[0],'code':re.search(r'_(.*)_', files[0]).group(1)}])
#
# print(df)


def get_data_frame():
    files = os.listdir(train_images_final)
    files = [i for i in files if 'orig' not in i]
    df = pd.DataFrame(columns=['name', 'code'])
    for file in files:
        df = df.append([{'name': file, 'code': re.search(r'_(.*)_', file).group(1)}])
    return df
