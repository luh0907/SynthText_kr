DEFAULT = 0
TRAIN = 1
TEST = 2
VAL = 3

NORMAL = 0  # NORMAL/WEIRD: weird for synthetic word dict
WEIRD = 1

SPLIT = TEST    # control through this
MODE = WEIRD
POSTFIX = 0


DATA_DIR = "/hd/SynthText_kr/assets/"

RESULT_DIRS = ["./",
               "train/",
               "test/",
               "val/"]
RESULT_ROOT = "/hd/SynthText_kr/results/"
RESULT_DIR = RESULT_ROOT + RESULT_DIRS[SPLIT]

FONT_LIST_FILES = ["fontlist.txt",
                   "fontlist_train.txt",
                   "fontlist_test.txt",
                   "fontlist_val.txt"]
FONT_LIST_FILE = FONT_LIST_FILES[SPLIT]

FONT_MODEL_FILES = ["font_px2pt.cp",
                    "font_px2pt_train.cp",
                    "font_px2pt_test.cp",
                    "font_px2pt_val.cp"]
FONT_MODEL_FILE = FONT_MODEL_FILES[SPLIT]

DICTIONARY_FILES = [["newsgroup/newsgroup.txt", "newsgroup/newsgroup.txt"],
                    ["dictionary/train.txt", "dictionary/train_weird.txt"],
                    ["dictionary/test.txt", "dictionary/test_weird.txt"],
                    ["dictionary/val.txt", "dictionary/val_weird.txt"]]
DICTIONARY_FILE = DICTIONARY_FILES[SPLIT][MODE] 

PREFIXES = [["default", "default"],
            ["train", "train_weird"],
            ["test", "test_weird"],
            ["val", "val_weird"]]
PREFIX = PREFIXES[SPLIT][MODE]

# train : test : val = 7 : 2 : 1
START_IMG_IDXES = [4400, 0, 5607, 7209]
START_IMG_IDX = START_IMG_IDXES[SPLIT]

NUM_IMGES = [-1, 5607, 1602, 801]
NUM_IMG = NUM_IMGES[SPLIT]   # -1 for all
