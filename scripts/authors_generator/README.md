# 自动填写content/authors
## log
2022.11.20: naive version
## 大体流程
idea很简单
1. 利用pandas读取信息收集表格excel，存为dict
2. 为yaml的每一项写一个函数write_xxx
3. 利用函数将收集的数据写成特定的dict格式
4. 将所有数据写回_index.md

注: 目前该脚本只能写学生的信息，老师的信息需要手动敲
## 食用说明
### 0. requirements.txt
安装需要的包
```bash
pip install -r requirements.txt
```
### 1. _index.md说明
需要了解一下markdown的front matter和yaml
其实就是markdown中的---之间放的是yaml的数据，而yaml的数据读进来就是dict的形式。
---之后的部分是个人简介，注意和bio的区别。这次问卷没有收集，就还没处理这部分的写入。
可以尝试一下运行writer.py

参考: 
[Python 读写 yaml 文件](https://www.cnblogs.com/auguse/articles/16007684.html)
[How do I read/write markdown yaml frontmatter with ruamel.yaml?](https://stackoverflow.com/questions/67964331/how-do-i-read-write-markdown-yaml-frontmatter-with-ruamel-yaml)

### 2. scripts/data.py说明
Record
> 就是一个字典
> 初始化的时候要根据scripts/config.py中的MAPPER初始化所有可能的值，这样后面在读取值的时候，不会因为没有对应的key而报错
> 比较大小好像就不用了，因为网站自动根据英文名来排序

People
> 把信息收集表格excel全部读取，并且整理成一个一个的Record
> 路径，可以给绝对路径，也可以给当前目录下文件名

### 3. 修改scripts/config.py
根据问卷每一栏的标题，修改MAPPER的value。
> 考虑到问卷的题目不一定会固定，所以我们把yaml的每一项和问卷中的每一问进行了映射。
> 如果需要新增/修改写入内容，也需要在MAPPER中新增/修改对应的映射，然后去新增/修改scripts/writer.py中的函数

注（config.py中一些有用的设定）:
Userful Path
> 这里主要是设定root, scripts, assets, data的路径，不用担心运行脚本时各种路径上的问题。
> 同时还可以放一些固定文件的路径，如默认头像DEFAULT_AVATAR的路径，这样修改的时候就不用跑到函数里面去一个一个修改了。

Userful Alias
> 考虑到一些alias的设定，问卷那边就不用太限定输入了（MAPPER也是）。
> institutionize函数用来统一返回institution，便于统一判定。目前支持thu, pku, bigai。
> NONES用来指定 空 ，用这个来识别信息收集表格中未填入的部分（通常为np.NaN），这样统一设定就不会出奇奇怪怪的bug。
> TRUES和FALSES用来指定问卷中肯定和否定的回答。

Useful Variable
> 一些其他可能会用上的变量。
> SPLITTERS用来分割填入的信息，如科研兴趣，大家可能用 , 或者 / 或者 & 分开，配合正则表达式re就可以把字符串分开了。（目前还不支持空格的分开，因为"AI Music" is not "AI" "Music"）

### 4. 修改scripts/writer.py
参考assets的template，最外面的一项都是需要单独写一个函数来维护的（如：title, superuser等）

write_xxx
> 如果要新增/修改填入的数据格式，请写一个write_xxx(yaml_dict, record)

write_record
> 将所有的write_xxx函数都加入到write_record中的write_funcs，这样可以统一循环调用。

handle_avatar
> 理想策略是：如果问卷里面有上传头像，就用问卷的头像；如果没有，就用本地搜集的头像。需要将两部分头像在本地合并。
> 目前策略师：如果问卷里面有上传头像，就下载问卷的头像（腾讯文档收集的头像有一个url）；如果没有，就用本地默认头像DEFAULT_AVATAR

write
> 给数据存储的根路径和record
> 如果不想展示，就直接跳过
> 根据record来生成目录，如THU20_YuyangLi（所以需要检查问卷的英文名和届别）
> 调用handel_avatar来存储avatar.jpy
> 调用write_record来获得yaml_dict
> 将yaml_dict写成_index.md（---后的写入需要简单修改一下，就是文件的读写而已）
### 4. 运行scripts/main.py
目录结构
> assets: 默认头像和template参考
> data: 收集的excel表格和生成的数据
> scripts: 所有的代码 

python main.py
> 修改form，填入excel的名字
> 运行
> 在data生成希望被展示的所有数据

替换网站的content/authors
> 策略：新增，旧的不改（后续可以考虑合并）
> 备份网站的content/authors的所有学生
> 删除网站的content/authors的所有学生
> 将data中所有的学生copy到content/authors
> 将备份网站的content/authors覆盖掉这次问卷重复收集的

## 特例说明
1. 年份。统一考虑4年，即THU20的年份是2020-2024。
2. 问卷格式。届别，如THU 20级，只能收集为 config.py/institutionize中的thu_alias中的某个 + 空格（可选） + 20，如THU 20或者清华20等
3. 问卷格式。科研兴趣等需要分点的，一律考虑 config.py/SPLITTERS 的分点，不要用空格分点！

## TODO
1. 头像处理
2. bio和_index.md最后的个人简介的处理