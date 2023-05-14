from PIL import Image
import os
import sys

music_instruments = [
    "Bonang",
    "Burdah",
    "Kolintang",
    "Rebab",
    "Saluang",
    "Sape",
    "Sasando",
    "Talindo",
    "Tifa",
    "Yi"
]

path = "./download/"
final_size = 150


# RESIZE WITH KEEPING THE SAME RATIO AS THE ORIGINAL FILE
def resize_aspect_fit(item):
    print("starting to resize file")
    if item == '.DS_Store':
        print("failed to resize file")
    elif os.path.isfile(item):
        im = Image.open(item)
        f, e = os.path.splitext(item)
        size = im.size
        ratio = float(final_size) / max(size)
        new_image_size = tuple([int(x*ratio) for x in size])
        im = im.resize(new_image_size, Image.ANTIALIAS)
        new_im = Image.new("RGB", (final_size, final_size))
        new_im.paste(
            im, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
        new_im.save(f + '_resized.jpg', 'JPEG', quality=90)
        print("successfully resize file and saved into " + f + '_resized.jpg')
    else:
        print("unkownn problems")


# for dir in os.listdir(path):
#     for item in os.listdir(path+dir):
#         file = path+dir+"/"+item
#         print(file, os.path.isfile(file))
#         resize_aspect_fit(file)


# RESIZE WITHOUT KEEPING THE SAME RATIO AS THE ORIGINAL FILE
def resize_aspect_not_fit(item):
    print("starting to resize file")
    if item == '.DS_Store':
        print("failed to resize file")
    elif os.path.isfile(item):
        im = Image.open(item)
        f, e = os.path.splitext(item)
        imResize = im.resize((final_size, final_size), Image.ANTIALIAS)
        imResize.save(f + '.jpg', 'JPEG', quality=90)
    else:
        print("unkownn problems")


for dir in os.listdir(path):
    for item in os.listdir(path+dir):
        file = path+dir+"/"+item
        print(file, os.path.isfile(file))
        resize_aspect_not_fit(file)
