#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- Author:zcg -*-
# -*- Time:2024-10-05 22:27:05
# -*- Describe:

'''
    类中方法的处理
'''


def handleMethod(temp):
    
    method_dict = {}
    method_dict['name'] = temp['name']
    method_dict['modifiers'] = ' '.join(temp['modifiers'])
    method_dict['funcs'], method_dict['methods'] = handleMethodNodes(temp['nodes'])
    method_dict['params'] = []
    for i in temp['params']:
        method_dict['params'].append(i[1]['name'])
    return method_dict




def handleMethodNodes():
    pass