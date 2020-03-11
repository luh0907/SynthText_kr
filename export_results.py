"""
Export the generated localization synthetic
data stored in h5 data-bases
"""
from __future__ import division
import os
import os.path as osp
import numpy as np

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt 
import h5py 
from common import *
import itertools
from PIL import Image, ImageDraw
import re
import json

from config import RESULT_DIR, PREFIX, POSTFIX

# initialize index
num = 1

def viz_textbb(text_im, charBB_list, wordBB, index, txt, font, alpha=1.0):
    """
    text_im : image containing text
    charBB_list : list of 2x4xn_i bounding-box matrices
    wordBB : 2x4xm matrix of word coordinates
    """
    img = Image.fromarray(text_im, 'RGB')
    img.save(os.path.join(RESULT_DIR, 'images', '{}_{}_{}.png'.format(PREFIX, index.split('.')[0], POSTFIX)))

    # plot the word-BB:
    for i in xrange(wordBB.shape[-1]):
        bb = wordBB[:,:,i]
        bb = np.c_[bb,bb[:,0]]
        coords(bb[0,:], bb[1,:], index, text_im, txt[i], font[i], i, "word")

    # plot the character-BB:
    for _ in xrange(len(charBB_list)):
        i = 0
        char_cnt = 0
        bbs = charBB_list[i]
        ni = bbs.shape[-1]
        for j in xrange(ni):
            bb = bbs[:,:,j]
            bb = np.c_[bb,bb[:,0]]
            coords(bb[0,:], bb[1,:], index, text_im, txt[i][char_cnt], font[i], i, "char")
            char_cnt += 1
            if char_cnt >= len(txt[i]):
                char_cnt = 0
                i += 1


# generate image files and coordinate files
def coords(x_list, y_list, k, img, txt, font, word_id, typ):
    tmp = []
    
    # remove alpha
    x_list=x_list[:-1]
    y_list=y_list[:-1] 

    # change datatype
    x_list=[int(x) for x in x_list]
    y_list=[int(y) for y in y_list]

    # generate coords list
    tmp=list(zip(x_list, y_list))

    # coords to image file
    k=k.split('.')[0]

    # 8-coords, font_family@style, word_id, label
    with open(os.path.join(RESULT_DIR, typ, '{}_{}_{}.txt'.format(PREFIX, k, POSTFIX)), 'a') as result_file:
        result_file.write("{},{},{},{},{},{},{},{},{},{},{}\n".format(tmp[0][0], tmp[0][1],
                                                                    tmp[1][0], tmp[1][1],
                                                                    tmp[2][0], tmp[2][1],
                                                                    tmp[3][0], tmp[3][1],
                                                                    font, word_id, txt.encode('utf-8')))


def main(db_fname):
    db = h5py.File(db_fname, 'r')
    dsets = sorted(db['data'].keys())
    print "total number of images : ", colorize(Color.RED, len(dsets), highlight=True)
    for k in dsets:
        rgb = db['data'][k][...]
        charBB = db['data'][k].attrs['charBB']
        wordBB = db['data'][k].attrs['wordBB']
        txt = db['data'][k].attrs['txt']
        font = db['data'][k].attrs['font']

        viz_textbb(rgb, [charBB], wordBB, index=k, txt=txt, font=font)
        print "image name        : ", colorize(Color.RED, k, bold=True)
        print "  ** no. of chars : ", colorize(Color.YELLOW, charBB.shape[-1])
        print "  ** no. of words : ", colorize(Color.YELLOW, wordBB.shape[-1])
        print "  ** text         : ", colorize(Color.GREEN, txt)
    
    db.close()

if __name__=='__main__':
    main(os.path.join(RESULT_DIR, 'dset_kr.h5'))
