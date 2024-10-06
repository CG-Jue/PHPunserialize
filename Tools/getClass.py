#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- Author:zcg -*-
# -*- Time:2024-10-05 21:53:17
# -*- Describe:

'''

获取每一个类

'''


import json

from processClass import processEndClass

finalData=[]

def get_the_classes(outf):
    # 对文件中存在的每个Class的所有属性进行提取
    Classes = []
    for i in json.load(outf):
        if i[0] == "Class":
            Classes.append(i[1])
    print(Classes)
    # return Classes
def prapreClass(data):
    '''
    processEndClass待完善
    '''
    for tempdata in data:
        print(tempdata)
        print('=========分割线=========')
        processEndData = (tempdata)
        # print(processEndData)
        # finalData.append(processEndData)
    # return finalData 
def finalClass():

    with open("input1.json","r") as inf:
       finalData = prapreClass(get_the_classes(inf))
    inf.close()
    # print(finalClass)
    # return finalData

# (finalClass())
get_the_classes(open("input1.json","r"))