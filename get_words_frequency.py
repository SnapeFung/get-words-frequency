# -*- coding: utf-8 -*-
import re
from get_chinese_meaning import get_chinese

# read the file
# f_name = input('input the essay file name')
f_name = 'Untitled.txt'
with open(f_name, 'r') as f_read:
    essay_content = f_read.read()
filter_essay_list = [i for i in essay_content if i.isalpha() is True or i == ' ']
filter_essay = ''.join(filter_essay_list)
filter_essay = filter_essay.lower()
split_words = filter_essay.split(' ')
split_words = [i for i in split_words if i != '']

# get already know words
with open("already_know.txt", 'r') as already_know:
    already_know = already_know.read()
# sort out the file
already_know = already_know.replace(' ', ',')
already_know = already_know.replace(',', '\n')
already_know = already_know.split('\n')
already_know = list(set(already_know))  # remove duplicate words
already_know = sorted(already_know)

already_know_sort = ''
for i in already_know:
    already_know_sort += i + '\n'
with open("already_know.txt", 'w') as f:  # 刷新已知单词文件
    f.write(already_know_sort)

# filter already know words
filter_words = [i for i in split_words if i not in already_know]

dic = {}
for i in filter_words:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

sort_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)  # sort the dictionary

# for word, frequency in sort_dic:
#     print(word, frequency)
# print(get_chinese(list(dic.keys()), list(dic.values())))
print(get_chinese(list(dic.keys())))
