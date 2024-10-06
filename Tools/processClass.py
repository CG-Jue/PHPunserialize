#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- Author:zcg -*-
# -*- Time:2024-10-05 21:56:50
# -*- Describe:
'''

对每一个类进行模版处理

'''

'''
模版如下
  {
    "name": "类名",
    "methods": [
      {
        "name": "方法名",
        "funcs": [
          {
            "name": "调用的函数名",
            "params": [方法的参数列表]
          }
        ],
        "methods": [该方法调用的其他方法],
        "params": [该方法的参数]
      }
    ],
    "variables": [
      {
        "name": "属性名",
        "modifiers": ["修饰符"],
        "initial": 初始化值，如果没有就是null
      }
    ],
  }
    :param target_class:
    :return:
'''
import json
# from handleMethod import handleMethod
from getClass import get_the_classes
def processEndClass(temp):
  # print(temp[0])
  # print("=============================")
  # print(temp[1])
  
  # exit()
  Class = {}
  allClass = []
  for item in temp:
    json.dump(item,open("File/input2.json",'w'), indent=4)
    # print(item)
    # print("=============================")
    # continue
    Class['name'] = item['name'] 
    Class['methods'] = []
    Class['variables'] = []
    # print(Class)
    # # continue
    # print("=============================")
    # print((type(item['nodes'])))

    for i in item['nodes']:
      # print((i))
      # continue
      if i[0] == 'Method':
        # tempdata = handleMethod(i[0])
        # print(i[1])
        with open("File/input3.json",'w') as f:
          json.dump(i[1],f,indent=4)
        print("=============================")
  # print(Class)
  # return Class

inf = open("File/input1.json","r")

processEndClass(get_the_classes(inf)) 
