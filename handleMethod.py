#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- Author:zcg -*-
# -*- Describe:
'''
'''


def handleMethod(temp):
    # 处理类中方法，部分赋值相关内容还没有处理好
    method_dict = {}
    method_dict['name'] = temp['name']
    method_dict['modifiers'] = ' '.join(temp['modifiers'])
    method_dict['funcs'], method_dict['methods'] = parse_method_nodes(temp['nodes'])
    method_dict['params'] = []
    for i in temp['params']:
        method_dict['params'].append(i[1]['name'])
    return method_dict




def handleMethodNodes():
    pass