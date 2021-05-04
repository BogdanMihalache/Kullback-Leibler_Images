import os
import numpy as np
from scipy.special import rel_entr
import matplotlib.pyplot as plt
from PIL import Image

def show_image(file_name, path):
    file_path = os.path.join(path, file_name)
    im = Image.open(file_path)
    im.show()

def read_files(path):
    files = os.listdir(path)
    jpgfiles = list()
    for i in files:
        if i.find('.jpg') > 0:
            jpgfiles.append(i)
    return (jpgfiles)


def rgb2gri(img, format):
    img = plt.imread(img)
    s = img.shape
    if len(s) == 3 and s[2] == 3:
        if format == 'png':
            img = (0.299 * img[:, :, 0] + 0.587 * img[:, :, 1] + 0.114 * img[:, :, 2]) * 255
        elif format == 'jpg':
            img = 0.299 * img[:, :, 0] + 0.587 * img[:, :, 1] + 0.114 * img[:, :, 2]
        img = img.astype('uint8')
    return img


def create_hists(jpgfiles, path):
    hists = list()
    for i in range(len(jpgfiles)):
        file_path = os.path.join(path, jpgfiles[i])
        im = rgb2gri(file_path, 'jpg')
        h, _ = np.histogram(im, density=True, bins=range(256))
        hists.append(h)
    return hists


def kl(hists, p):
    # p: index of chosen image
    # h: index of most similar image to chosen image
    most_similar = {'KL': float('inf'),  # initialize KL
                    'P': p,
                    'Q1': 0,
                    'Q2': 0}
    for h in range(len(hists)):
        if h == p:
            continue

        kl_now = sum(rel_entr(hists[p], hists[h]))
        if kl_now < most_similar['KL']:
            most_similar['KL'] = kl_now
            most_similar['Q2'] = most_similar['Q1']
            most_similar['Q1'] = h

    return most_similar
