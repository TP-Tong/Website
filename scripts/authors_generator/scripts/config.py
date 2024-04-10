import os
from pathlib import Path
import numpy as np

##### Userful Path #####
ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = os.path.join(ROOT, "scripts")
ASSETS = os.path.join(ROOT, "assets")
DATA = os.path.join(ROOT, "data")
DEFAULT_AVATAR = os.path.join(ASSETS, "default.jpg")
##### #####


##### Userful Alias #####
''' map yaml key to excel key, NEED to change map_dict according to your form.
'''
MAPPER = {
    "DONT_CHANGE": "TO_CHANGE",
    ##### name #####
    "title": "姓名（英文，如 Guangyuan Jiang）（必填）",
    "chineseName": "姓名（中文，如 姜广源）",
    ##### photo #####
    "photo": "个人照片",
    ##### role #####
    ##### organizations #####
    "organizations": "组织",
    ##### bio #####
    "bio": "个人简介",
    ##### interests #####
    "interests": "研究兴趣（必填）",
    ##### education #####
    "session": "届别",
    ##### social #####
    "email": "邮箱（用于学术联络）（必填）",
    "homepage": "个人主页链接（如有）",
    "google-scholar": "Google Scholar 链接（如有）",
    "github": "GitHub 用户名（如有）",
    "twitter": "Twitter 用户名（如有）",
    "linkedin": "LinkedIn 用户名（如有）",
    "orcid": "ORCID",
    "cv": "个人简历链接",
    ##### email #####
    ##### display #####
    "display": "您是否同意自己被列入网站的 People 页？（必填）",
    ##### submit #####
    "submit": "提交者（自动）", # the unique account used to submit the form
}

def institutionize(excel_item):
    thu_alias = ["清华", "清华大学", "T大", "THU", "thu"]
    pku_alias = ["北大", "北京大学", "P大", "PKU", "pku"]
    bigai_alias = ["通院", "通用人工智能研究院", "北京市通用人工智能研究院", "BIGAI", "bigai"]
    if excel_item in thu_alias: return "thu"
    if excel_item in pku_alias: return "pku"
    if excel_item in bigai_alias: return "bigai"
    return None



# to identify the blank input
NONES = [None, np.nan, np.NaN, np.NAN, ""]

TRUES = ["是", "行", "可", "可以", "确认", "确定", "YES", "Yes", "yes", "TRUE", "True", True]
FALSES = ["否", "不是", "不行", "不", "不可以", "否认", "否定", "NO", "No", "no", "FALSE", "False", False, None, np.nan, np.NaN, np.NAN]
##### #####

##### Useful Variable #####
# NEVER split with space! eg. "AI Music" is not "AI" "Music"
SPLITTERS = "/&,，、\n"
##### ##### 