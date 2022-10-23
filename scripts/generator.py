'''
Author: Aiden Li
Date: 2022-10-23 15:06:00
LastEditors: Aiden Li (i@aidenli.net)
LastEditTime: 2022-10-23 15:21:23
Description: Text generators
'''

def people_generator(
    display_name,
    superuser=False,
    role="Member",
    orgs={"Tsinghua University": "https://www.tsinghua.edu.cn"},
    bio=None,
    interests=[],
    education=[("B.E. in Automation and Artificial Intelligence", "Tsinghua University", "2020-2024")],
    contact={
        "email": "i@johndoe.com", "housepage": "https://johndoe.com", "github": "johndoe", "twitter": "johndoe", "linkedin": "johndoe",
        "gscholar": None, "cv": None
    },
    user_groups=["清华 20 级"],
    intro="John Doe is ..."
):
    pass

def publication(
    title,
    authors=["John Doe", "Jane Doe"],
    date="2022-10-10T00:00:00Z", publishDate="2022-10-10T00:00:00Z",
    publication_type=['1', '3'], publication="International Conference on Robotics and Automation", publication_short="ICRA",
    abstract=None, summary=None, image_caption="teaser", projects=['internal-project'], supplementary_notes=None, bib_text=None,
    links={
        "arxiv": None,
        "pdf": None,
        "code": None,
        "dataset": None,
        "poster": None,
        "project": None,
        "slides": None,
        "source": None,
        "video": None,
    },
):
    pass
