import random
import os
from PIL import ImageEnhance, Image
from constants import train_images_512
from multiprocessing import Pool


def generate_variety(file_name):
    base_img = Image.open(train_images_512 + file_name)
    square_image = center_square_image(base_img)
    for i in range(10):
        modified_img = randomize_image(square_image)
        new_name = file_name.replace('orig', str(i))
        print(new_name)
        modified_img.save(train_images_512 + new_name)


def randomize_image(img):
    modified = random.randint(3, 7)
    for i in range(modified):
        img = generate_random_images(img)
    return img

#
# def load_data(directory, count):
#     images = list()
#     labels = list()
#     random.seed()
#     for c in range(5):
#         for i in range(count):
#             img = fetch_random_images(directory, c)
#             labels.append(c)
#             images.append(img)
#     return images, labels
#
#
# def load_and_transform_image(directory, count):
#     images = list()
#     labels = list()
#     random.seed()
#     for c in range(5):
#         for i in range(count):
#             img = fetch_random_images(directory, c)
#             img = generate_random_images(img)
#             img = random_square_image(img)
#             labels.append(c)
#             images.append(img)
#     return images, labels


def fetch_random_images(directory, cls):
    files = os.listdir(directory)
    while True:
        file = random.choice(files)
        if 'orig' in file:
            continue
        if '_%s_' % cls in file:
            return Image.open(directory + file)


def generate_random_images(img):
    factor = random.uniform(0.5, 1.5)
    choice = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
    if choice == 1:
        return img.transpose(Image.FLIP_TOP_BOTTOM)
    if choice == 2:
        return img.transpose(Image.FLIP_LEFT_RIGHT)
    if choice == 3:
        return ImageEnhance.Brightness(img).enhance(factor)
    if choice == 4:
        return ImageEnhance.Color(img).enhance(factor)
    if choice == 5:
        return ImageEnhance.Contrast(img).enhance(factor)
    if choice == 6:
        return ImageEnhance.Sharpness(img).enhance(factor)
    if choice == 7:
        return img.transpose(Image.ROTATE_90)
    if choice == 8:
        return img.transpose(Image.ROTATE_180)
    if choice == 9:
        return img.transpose(Image.ROTATE_270)


def random_square_image(img):
    if img.size[0] == img.size[1]:
        return img
    elif img.size[0] < img.size[1]:
        offset = int((img.size[1] - img.size[0]) / 2)
        return img.crop((0, offset, img.size[1], offset + img.size[1]))
    else:
        offset = int((img.size[0] - img.size[1]) / 2)
        return img.crop((offset, 0, offset + img.size[1], img.size[1]))


def center_square_image(img):
    if img.size[0] == img.size[1]:
        return img
    elif img.size[0] < img.size[1]:
        offset = int((img.size[1] - img.size[0]) / 2)
        return img.crop((0, offset, img.size[1], offset + img.size[1]))
    else:
        offset = int((img.size[0] - img.size[1]) / 2)
        return img.crop((offset, 0, offset + img.size[1], img.size[1]))


if __name__ == '__main__':
    files = os.listdir(train_images_512)
    files = [i for i in files if 'orig' in i]
    p = Pool(4)
    p.map(generate_variety, files)
