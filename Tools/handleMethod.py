#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- Author:zcg -*-
# -*- Time:2024-10-05 22:27:05
# -*- Describe:

'''
    类中方法的处理
'''
import json
def handleMethodNodes():
    pass
def handleMethod(temp):
    
    method_dict = {}
    method_dict['name'] = temp['name'] #方法名
    method_dict['modifiers'] = ' '.join(temp['modifiers'])
    method_dict['funcs'], method_dict['methods'] = handleMethodNodes(temp['nodes'])
    method_dict['params'] = [] 
    for i in temp['params']: 
        method_dict['params'].append(i[1]['name'])
    print(method_dict)
    # return method_dict


with open('File/input3.json','r') as f:
    temp = json.load(f)
    # print(temp)

handleMethod(temp)
