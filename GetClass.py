#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- Author:zcg -*-
# -*- Describe:
'''
获取每一个类
待定
'''
# from PHPJson import phpjson

# phpjson("demo.php")

import json

def get_the_classes(outf):
    # 对文件中存在的每个Class进行提取
    Classes = []
    for i in json.load(outf):
        if i[0] == "Class":
            Classes.append(i[1])
    # print(Classes)
    return Classes
def prapreClass(data):
    for tempdata in data:
        print(tempdata)
        print('分割线==================')
        for i in tempdata:
            pass
            # print(i)

with open("input1.json","r") as inf:
    prapreClass(get_the_classes(inf))


