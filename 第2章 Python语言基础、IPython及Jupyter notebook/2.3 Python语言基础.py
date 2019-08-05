#!/usr/bin/env python
# coding: utf-8
# 2.3.1 语言定义
# 2.3.1.5变量和参数传递


def append_element(some_list, element):
    some_list.append(element)


data = [1, 2, 3]
append_element(data, 4)
print(data)

# 2.3.1.6 动态引用、强类型
a = 4.5
b =2
# 字符串格式化，用于后面访问
print('a is {0}, b is {1}'.format(type(a), type(b)))
print(a / b)

# 2.3.2 标量类型
# 字符串
c = """
This is a longer string that
spans multiple lines
"""
c.count('\n')



