"""
Created on Sun Oct 13 10:15:21 2019

@author: Sagar
"""
import os
from multiprocessing import Pool
from PIL import Image
import csv

train_csv = "data/train.csv"
test_csv = "data/test.csv"

base_size = 512

old_dir = "data/test_images/"
new_dir = "data/test_images_512/"


def resize_image(file_name):
    img = Image.open(old_dir + file_name)
    if img.size[0] < img.size[1]:
        pct = base_size / img.size[0]
    else:
        pct = base_size / img.size[1]
    new_w = int(img.size[0] * pct)
    new_h = int(img.size[1] * pct)
    img = img.resize((new_w, new_h), Image.LANCZOS)
    new_file_name = file_name_with_label(file_name)
    print(new_file_name)
    img.save(new_dir + new_file_name)


def find_label(i):
    name = i.replace('.png', '')
    for d in data:
        if d['id_code'] == name:
            return d
    return None


def file_name_with_label(file_name):
    label = find_label(file_name)
    new_name = file_name.replace('.png', '_') + str(label['diagnosis']) + '_orig.png'
    return new_name


if __name__ == "__main__":
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    with open(test_csv, 'r') as infile:
        data = [dict(i) for i in csv.DictReader(infile)]
    files = os.listdir(old_dir)
    p = Pool(4)
    p.map(resize_image, files)
