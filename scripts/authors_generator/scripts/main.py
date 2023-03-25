'''
steps:
1. excel
    1. read the data properly
    2. define a class
    3. read the data with class
2. yaml
    1. how to write a yaml with python
    2. how to transform yaml to md
    3. data -> yaml -> md
    4. generalize
3. automate
    1. python
    2. shell
    3. gui
'''

from config import *
from data import *
from writer import *
from tqdm import tqdm

if __name__ == '__main__':
    form = os.path.join(DATA, "dataset.xlsx") # TODO: change this
    people = People(form)

    print("data writing...")
    for i in tqdm(range(len(people))):
        write(DATA, people[i])

    print("data written!")