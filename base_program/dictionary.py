#!/usr/bin/python3

# 字典 是无序的，且key不能重复

d1 = {}  # 空字典
print(d1)
d1['name'] = 'tom'
d1['age'] = 11
print(d1)

d2 = {'name': 'jdx', 'age': 22}
print(d2)   # {'name': 'jdx', 'age': 22}
print(d2['name'])   # 'jdx'
print(d2.keys())    # dict_keys(['name', 'age'])
print(d2.values())  # dict_values(['jdx', 22])


# 构造函数 dict() 可以直接从键值对序列中构建字典如下：
d3 = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
print(d3)   # {'Runoob': 1, 'Google': 2, 'Taobao': 3}

