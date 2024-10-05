#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- Author:zcg -*-
# -*- Describe: 
'''
作用：
PHP代码转化为json数据，并存储在input1.json文件中
调用方法：
from PHPJson import phpjson
phpjson(filename)#
 
'''



from phply.phplex import lexer  # 导入phply库的lexer模块，用于PHP代码的词法分析
from phply.phpparse import make_parser  # 导入phply库的phpparse模块，用于PHP代码的语法分析
import json  # 导入json模块，用于序列化JSON数据

with_lines = True
def export(items):
    result = []  # 初始化一个空列表，用于存储转换后的PHP代码元素
    if items:  # 如果items列表不为空
        for item in items:  # 遍历items列表中的每个元素
            if hasattr(item, 'generic'):  # 检查元素是否有一个名为generic的方法
                item = item.generic(with_lineno=with_lines)  # 如果存在，调用generic方法并传入with_lineno参数
            result.append(item) # 将转换后的元素添加到result列表中
    # print(result) 
    return result  # 返回转换后的PHP代码元素列表

def phpjson(filename):
    # 创建一个解析器
    parse = make_parser()
    # 打开文件
    with open(filename,'r') as inf:
        # 打开输出文件
        with open('input1.json','w') as out:
            temp1 = inf.read() # 读取数据
            temp2 = parse.parse(temp1,lexer=lexer,tracking=with_lines) # 通过phply.phpprase 分析代码 形成ast树存储
            json.dump(export(temp2),out,indent=2)# json序列化存储到json文件中
    out.close()
    inf.close()

phpjson('demo.php')