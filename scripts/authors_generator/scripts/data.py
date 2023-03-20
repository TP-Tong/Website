'''
steps:
1. excel
    1. read the data properly
    2. define a class
    3. read the data with class

TODO:
1. sort
2. ch/en?
'''

from copy import deepcopy
import os, sys
from pathlib import Path
import numpy as np
import pandas as pd
from tqdm import tqdm
from config import *

class Record(dict):
    def __init__(self, keys, values, comparison=None):
        # use dict to store a single record, easy to index
        # IMPORTANT to init for all possible values in MAPPER
        for key in MAPPER:
            self[MAPPER[key]] = np.NaN

        for idx, key in enumerate(keys):
            self[str(key)] = values[idx]
        # if comparison is None, then no sort
        self.comparison = comparison

    def __lt__(self, other):
        if self.comparison is None:
            return id(self) < id(other)
        
        # TODO: sort name
        return self[self.comparison] < other[self.comparison]


class People(object):
    def __init__(self, filename, comparison=None):
        self.root = Path(__file__).resolve().parents[0] # path to this file
        self.path = os.path.join(self.root, filename) # path to excel
        self.comparison = comparison # use to sort

        self.load()

    def load(self):
        print("data loading...")
        people_df = pd.read_excel(self.path, keep_default_na=False)
        people_df_col = people_df.columns.values
        people_mat = people_df.values
        self.data = []

        for i in tqdm(range(people_mat.shape[0])):
            self.data.append(Record(people_df_col, people_mat[i], self.comparison))

        if self.comparison is not None:
            print("sorting...")
            print("sorted!")

        print("data loaded!")
        
    def __getitem__(self, index):
        return self.data[index]
    
    def __len__(self):
        return len(self.data)

    def delete_empty_row(self, df, id_loc):
        row, col = df.shape
        to_delete = np.array([], dtype=np.int32)
        for i in range(row):
            if df.iloc[i,id_loc] is np.NaN:
                to_delete = np.append(to_delete, i)
                continue
            if not df.iloc[i,id_loc].isdigit():
                to_delete = np.append(to_delete, i)
                continue
        df.drop(labels=to_delete, inplace=True)
        print("delete {} empty lines".format(len(to_delete)))
        
    def preview(self, line=5):
        length = min(line, len(self.data))
        for i in range(length):
            print(self.data[i])
        

if __name__ == '__main__':
    # keys = ["a", "vb"]
    # values = [1,2]
    # record = Record(keys, values)
    # print(record)
    people = People(os.path.join(DATA, "通班网站信息收集（收集结果）.xlsx"))
    people.preview()