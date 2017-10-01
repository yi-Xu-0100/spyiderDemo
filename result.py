# -*- coding:utf-8 -*- 


__author__ = 'yi_Xu'


import os
import sys, time


def getName(p):
    return sorted(
    [
        (x, os.path.getctime(os.path.join(p,x))) #生成一个列表，列表的每个元素是一个元组（文件，文件创建时间）
        for x in os.listdir(p) if os.path.isfile(os.path.join(p,x)) #p是文件夹路径，对p下的所有内容，只将文件的信息加入列表
    ],
    key=lambda i: i[1])[0][0]#对列表进行排序，排序的依据是每一个元组元素的第二个元素，排序后取最后一个元素


if __name__ == '__main__':
    p = os.path.join('.', 'result')
    fileName = '《希灵帝国》.txt'
    with open(os.path.join(p, fileName), mode='w', encoding='utf-8') as f:
        f.write('《希灵帝国》\n\n')
    while getName(p) != fileName:
        with open(os.path.join(p, fileName), mode='a', encoding='utf-8') as f_w:
            f_w.write('\n\n')
            with open(os.path.join(p, getName(p)), mode='r', encoding='utf-8') as f_r:
                for line in f_r:
                    f_w.write(line)
            f_w.write('\n\n')
            os.remove(os.path.join(p, getName(p)))

