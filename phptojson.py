#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- Author:zcg -*-

from phply.phplex import lexer  # 导入phply库的lexer模块，用于PHP代码的词法分析
from phply.phpparse import make_parser  # 导入phply库的phpparse模块，用于PHP代码的语法分析
import json  # 导入json模块，用于序列化和反序列化JSON数据

with_lines = True

def change():
    parse = make_parser()
    with open("demo.php","r") as inf:
        data = inf.read()
    a = parse.parse(data,lexer=lexer,tracking=with_lines)
    print(type(a))
    print(a)
    # for i in a:
        # print(i)

change()