'''
steps:
2. yaml
    1. how to write a yaml with python
    2. how to transform yaml to md
    3. data -> yaml -> md
    4. generalize

TODO:
1. a mapper
2. a template
'''
import ruamel
from ruamel.yaml import YAML
from config import *
import numpy as np
import shutil, os
import re
from data import *
import requests

##### write functions #####
def write_title(yaml_dict, record):
    placeholder = ""
    if record[MAPPER["title"]] not in NONES:
        placeholder = record[MAPPER["title"]]
    yaml_dict["title"] = placeholder

def write_superuser(yaml_dict, record):
    yaml_dict["superuser"] = False

def write_role(yaml_dict, record):
    yaml_dict["role"] = "Member"

def write_organizations(yaml_dict, record):
    placeholder = []
    if record[MAPPER["organizations"]] not in NONES:
        pass # TODO
    if record[MAPPER["session"]] not in NONES:
        institution = ""
        for s in record[MAPPER["session"]]:
            if s.isalpha(): institution += s
        institution = institutionize(institution)

        if institution == "thu": 
            placeholder.append({
                "name": "Tsinghua University",
                "url": "https://www.tsinghua.edu.cn"
            })
        if institution == 'pku': 
            placeholder.append({
                "name": "Peking University",
                "url": "https://www.pku.edu.cn/"
            })

    yaml_dict["organizations"] = placeholder

def write_bio(yaml_dict, record):
    placeholder = ""
    if record[MAPPER["bio"]] not in NONES:
        placeholder = record[MAPPER["bio"]]
    yaml_dict["bio"] = placeholder
    
def write_interests(yaml_dict, record):
    placeholder = []
    if record[MAPPER["interests"]] not in NONES:
        results = record[MAPPER["interests"]]
        symbols = "[" + SPLITTERS + "]"
        results = re.split(symbols, results)
        results = [result for result in results if result]
        for result in results:
            placeholder.append(result)
    yaml_dict["interests"] = placeholder

def write_education(yaml_dict, record):
    placeholder = {}
    placeholder["courses"] = []
    if record[MAPPER["organizations"]] not in NONES:
        pass # TODO
    if record[MAPPER["session"]] not in NONES:
        institution = ""
        year = ""
        for s in record[MAPPER["session"]]:
            if s.isalpha(): institution += s
            if s.isdigit(): year += s
        institution = institutionize(institution)

        year = int(year) + 2000
        year = "{}-{}".format(year, year + 4)

        if institution == "thu": 
            placeholder["courses"].append({
                "course": "B.E. in Automation and Artificial Intelligence",
                "institution": "Tsinghua University",
                "year": year
            })
        if institution == 'pku': 
            placeholder["courses"].append({
                "course": "B.E. in Artificial Intelligence",
                "institution": "Peking University",
                "year": year
            })

    yaml_dict["education"] = placeholder

def write_social(yaml_dict, record):
    placeholder = []
    if record[MAPPER["email"]] not in NONES:
        placeholder.append({
            "icon": "envelope",
            "icon_pack": "fa",
            "link": "mailto:" + record[MAPPER["email"]],
        })
    if record[MAPPER["homepage"]] not in NONES:
        placeholder.append({
            "icon": "house",
            "icon_pack": "fa",
            "link": record[MAPPER["homepage"]],
        })
    if record[MAPPER["google-scholar"]] not in NONES:
        placeholder.append({
            "icon": "google-scholar",
            "icon_pack": "ai",
            "link": record[MAPPER["google-scholar"]],
        })
    if record[MAPPER["github"]] not in NONES:
        placeholder.append({
            "icon": "github",
            "icon_pack": "fab",
            "link": "https://github.com/" + record[MAPPER["github"]],
        })
    if record[MAPPER["cv"]] not in NONES:
        placeholder.append({
            "icon": "cv",
            "icon_pack": "ai",
            "link": record[MAPPER["cv"]],
        })
    if record[MAPPER["twitter"]] not in NONES:
        placeholder.append({
            "icon": "twitter",
            "icon_pack": "fab",
            "link": "https://twitter.com/" + record[MAPPER["twitter"]],
        })
    if record[MAPPER["linkedin"]] not in NONES:
        placeholder.append({
            "icon": "linkedin",
            "icon_pack": "fab",
            "link": "https://www.linkedin.cn/incareer/in/" + record[MAPPER["linkedin"]],
        })
    yaml_dict["social"] = placeholder

def write_email(yaml_dict, record):
    placeholder = ""
    if record[MAPPER["email"]] not in NONES:
        placeholder = record[MAPPER["email"]]
    yaml_dict["email"] = placeholder

def write_highlight_name(yaml_dict, record):
    yaml_dict["highlight_name"] = False

def write_user_groups(yaml_dict, record):
    placeholder = []
    if record[MAPPER["session"]] not in NONES:
        # session = record[MAPPER["session"]].split()
        # institution = institutionize(session[0])
        # year = session[1]
        institution = ""
        year = ""
        for s in record[MAPPER["session"]]:
            if s.isalpha(): institution += s
            if s.isdigit(): year += s
        institution = institutionize(institution)

        if institution == "thu": institution = "清华"
        elif institution == 'pku': institution = "北大"
        else: return

        group = institution + ' ' + year + ' ' + "级"
        placeholder.append(group)

    yaml_dict["user_groups"] = placeholder

##### #####

##### main write function #####
def write_record(record):
    '''register all write functions here
    '''
    yaml_dict = {}
    write_funcs = [
        write_title,
        write_superuser,
        write_role,
        write_organizations,
        write_bio,
        write_interests,
        write_education,
        write_social,
        write_email,
        write_highlight_name,
        write_user_groups,
    ]
    for write_func in write_funcs:
        write_func(yaml_dict, record)
    return yaml_dict

def handle_avatar(path, record):
    # print(os.path.exists(os.path.join(DATA, "student-photos")))
    # print(os.listdir(os.path.join(DATA, "student-photos")))
    # print(record[MAPPER["chineseName"]])
    if record[MAPPER["photo"]] not in NONES:
        avatar = requests.get(record[MAPPER["photo"]], stream=True)
        with open(os.path.join(path, "avatar.jpg"), "wb") as file:
            for chunk in avatar.iter_content(chunk_size=32):
                file.write(chunk)
    elif os.path.exists(os.path.join(DATA, "student-photos"))\
        and record[MAPPER["chineseName"]] in os.listdir(os.path.join(DATA, "student-photos")):
        print("eeee")
        avatarDir = os.path.join("..", "data", "student-photos", record[MAPPER["chineseName"]])
        fileNames = os.listdir(avatarDir)
        avatarName = []
        for i in fileNames :
            avatarName.append(i)
        shutil.copyfile(os.path.join(os.path.join(avatarDir, avatarName[0])), os.path.join(path, "avatar.jpg"))
    else:
        shutil.copyfile(DEFAULT_AVATAR, os.path.join(path, "avatar.jpg"))

def write(path, record):
    # dont want to be displayed on website
    if record[MAPPER["display"]] in FALSES: return
    # missing name or session
    if record[MAPPER["title"]] in NONES or record[MAPPER["session"]] in NONES: return
    
    # get name and session to mkdir
    title = ""
    for s in record[MAPPER["title"]].split():
        title += s
    session = record[MAPPER["session"]].split()
    institution = institutionize(session[0])
    year = session[1]

    if institution == "thu": institution = "THU"
    elif institution == 'pku': institution = "PKU"
    else: return

    directory = institution + year + '_' + title
    path = os.path.join(path, directory)
    if not os.path.exists(path):
        os.mkdir(path)

    # handle avatar
    handle_avatar(path, record)

    # handle index.md
    path = os.path.join(path, "_index.md")
    with open(path, "w", encoding='utf-8') as file:
        yaml_dict = write_record(record)

        yaml = YAML()
        yaml.explicit_start = True
        yaml.dump(yaml_dict, file)

        file.write("---\n")

##### #####

if __name__ == '__main__':
    with open(os.path.join(ASSETS, "template.yml")) as file:
        yml = ruamel.yaml.load(file.read(), Loader=ruamel.yaml.Loader)
        print(yml)

    # people = People(os.path.join(DATA, "通班网站信息收集（收集结果）.xlsx"))
    # people.preview()
    # for i in range(20):
    #     write(DATA, people[i])