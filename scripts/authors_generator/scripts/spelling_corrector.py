from config import *
import pandas as pd
import os

def read_corrections(corrections_path: str) -> list:
    origin_corrections = pd.read_excel(corrections_path, keep_default_na=False)
    keys = origin_corrections.columns.values
    data = origin_corrections.values
    
    corrections = []
    for values in data:
        correction = {}
        for id, key in enumerate(keys):
            correction[key] = values[id]
        if correction['Status'] == 0 and correction['Grade'] != NONES:
            corrections.append(correction)
    return corrections

def correct(outer_folder:str , corrections:list) -> None:
    for correction in corrections:
        old_folder_name = correction['Grade']+'_'+correction['Origin_name'].replace(' ','')
        new_folder_name = correction['Grade']+'_'+correction['Normative_name'].replace(' ','')
        os.rename(os.path.join(outer_folder, old_folder_name), os.path.join(outer_folder, new_folder_name))
        with open(os.path.join(outer_folder, new_folder_name, '_index.md'), 'r+', encoding='utf-8') as f:
            lines = f.readlines()
            lines[1] = 'title: '+correction['Normative_name']+'\n'
            f.seek(0)
            f.writelines(lines)
        print('Succeed: "' + correction['Origin_name'] + '" has changed to "' + correction['Normative_name']+'"')
    

if __name__ == '__main__':
    corrections = read_corrections(os.path.join(ROOT, "错误拼写纠正.xlsx"))
    correct(os.path.join(os.path.dirname(os.path.dirname(ROOT)), 'content', 'authors'),corrections)