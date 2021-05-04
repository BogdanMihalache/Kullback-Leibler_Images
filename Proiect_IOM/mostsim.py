import os
from iom_functions import read_files, create_hists, kl, show_image


def find_images(file_path):
    file = file_path.split('\\')[-1]
    path = file_path[:(len(file_path) - len(file) - 1)]

    jpgfiles = read_files(path)
    hist_matr = create_hists(jpgfiles, path)
    img_index = jpgfiles.index(file)

    KL = kl(hist_matr, img_index)

    return os.path.join(path, jpgfiles[KL['Q1']]), os.path.join(path, jpgfiles[KL['Q2']])

    # print(KL['KL'], jpgfiles[KL['P']], jpgfiles[KL['Q1']], jpgfiles[KL['Q2']])
    # show_image(jpgfiles[KL['P']], path)
    # show_image(jpgfiles[KL['Q1']], path)
    # show_image(jpgfiles[KL['Q2']], path)
