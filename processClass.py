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

from handleMethod import handleMethod

def processEndClass(temp):
    
  Class = {}
  Class['name'] = temp['name']
  Class['methods'] = []
  Class['variables'] = []

  for i in temp['nodes']:
    if i[0] == 'Method':
      tempdata = handleMethod(i[0])


  return temp


