from __future__ import absolute_import

import os
import sys
sys.path.append('../')
# sys.path.insert(0,'../')
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.dirname(os.path.abspath(__file__)))
# from src import distortion as dis

import realisticAF
from realisticAF.src import distortion as dis

from PIL import Image
import torch
from torch.utils.data import Dataset

import numpy as np
import cv2

class DemoDataset(Dataset):
    def __init__(self, image_root, image_list_file):
        self.image_root = image_root
        self.image_list = []
        image_list_buf = open(image_list_file)
        line = image_list_buf.readline().strip()
        while line:
            line = line.split(' ')[0]
            self.image_list.append(line)
            line = image_list_buf.readline().strip()
        # self.mean = 127.5
        # self.std = 128.0
        # self.crop_eye = crop_eye

        # self.distort = distort
        # self.distort_param = distort_param
        # self.distortion = Distortion(self.distort, self.distort_param[self.distort])

    def __len__(self):
        return len(self.image_list)


    def __getitem__(self, index):
        short_image_path = self.image_list[index]
        image_path = os.path.join(self.image_root, short_image_path)
        image = cv2.imdecode(np.fromfile(image_path, dtype=np.uint8), cv2.IMREAD_UNCHANGED)

        # transform = dis.Compose([])

        # if self.distort:
        #     image = self.distortion.forward_x(image)
        #image = cv2.resize(image, (112, 112),interpolation=cv2.INTER_CUBIC)


        image = (image.transpose((2, 0, 1)) - self.mean) / self.std
        image = torch.from_numpy(image.astype(np.float32))
        return image, short_image_path


if __name__ == '__main__':
    # transform = dis.Compose([])

    img = Image.open('./img/test.jpg')

    # img = dis.JPEG_Compression(10)(img)
    # img = dis.JPEG_2000()(img)
    # img = dis.Gau_Noise(40)(img)
    # img = dis.Med_Blur(3)(img)
    # img = dis.Sharpness(1.5)(img)
    transform = dis.Compose([dis.JPEG_Compression(10), dis.Gau_Noise(10)])
    img = transform(img)
    img.save('./img/test2.jpg')
    # transformed_img = transform(image=img)

