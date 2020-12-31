#!/usr/bin/python3

# 字符串使用 ' 和 " 没有区别
str = 'hello python3'
str2 = "hello python3"
print(str, str2)

# 索引值以 0 为开始值，-1 为从末尾的开始位置。
# 字符串截取 str[开始下标:结束下标:步长] 步长表示每个几个字符取一次
print(str[0:-1])  # hello python
print(str[0:])  # hello python3
print(str[0::2])  # hlopto3 每隔两个字符取一次
print(str[0])  # 输出指定下标的字符
print(str * 2)  # hello python3hello python3 连续输出两次字符
print(str + ' coming')  # hello python3 coming 拼接字符串

print(str[-1::-1])   # 从末尾开始截取且步长为-1 用于反转字符串 3nohtyp olleh

# python 的字符串不能修改
# str[0] = 'm' 将报错

# 转义
str3 = 'hello \neo'
print(str3)
'''
hello
eo
'''
# 取消转义 字符串前加 r 注意r与字符串之间不能有空格
str4 = r'hello \neo'
print(str4)  # hello \neo
