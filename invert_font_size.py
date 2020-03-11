# Author: Ankush Gupta
# Date: 2015
"Script to generate font-models."

import pygame
from pygame import freetype
from text_utils import FontState
import numpy as np 
import matplotlib.pyplot as plt 
#import cPickle as cp
import pickle as cp
import os.path as osp

from config import DATA_DIR, FONT_LIST_FILE, FONT_MODEL_FILE


if __name__ == "__main__":
    pygame.init()

    # ys = np.arange(8,200)
    ys = np.arange(100,200)
    A = np.c_[ys,np.ones_like(ys)]

    xs = []
    models = {} # linear model

    data_dir = osp.join(DATA_DIR, 'data')
    font_list = osp.join(data_dir, 'fonts', FONT_LIST_FILE)
    with open(font_list, 'r') as font_list_file:
        fonts = [osp.join(data_dir, 'fonts', line.strip()) for line in font_list_file]

    #FS = FontState()
    #plt.figure()
    #plt.hold(True)
    #print(FS.fonts)
    #print(fonts)

    for i in xrange(len(fonts)):
        # font = freetype.Font(FS.fonts[i], size=12)
        font = freetype.Font(fonts[i], size=50)
        h = []
        for y in ys:
            h.append(font.get_sized_glyph_height(y))
        h = np.array(h)
        m, _, _, _ = np.linalg.lstsq(A,h)
        models[font.name] = m
        xs.append(h)

    with open(osp.join(DATA_DIR, 'data', 'models', FONT_MODEL_FILE), 'w') as f:
        cp.dump(models, f)

    #plt.plot(xs,ys[i])
    #plt.show()
