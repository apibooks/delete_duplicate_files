# -*- coding:utf-8 -*-
import os


# 扩展名
def get_file_extension(path):
    return os.path.splitext(path)[1]


# 提取所有的目录
def get_all_file(path):
    all_file_list = []

    # Allowed extension
    alllow_filee_xtension = ['.txt', '.mp3']

    # recursive extraction of all paths of a file
    for root, dirs, files in os.walk(path):
        for name in files:
            filePath = os.path.join(root, name)
            if (get_file_extension(filePath) in alllow_filee_xtension):
                all_file_list.append(filePath)

    return all_file_list


# 去除空格
def remove_blank(content):
    return content.strip().replace(' ', '')


# main
if __name__ == '__main__':
    # 提取路径
    path = 'E:\\python\\res2'.decode('gbk')

    # 提取所有文件
    all_file = get_all_file(path)

    # 循环删除重复的文件
    keepList = []

    for item in all_file:
        file = remove_blank(item)
        if file not in keepList:
            keepList.append(file)
        else:
            os.remove(item)
            print(u'删除文件 %s' % item)

    print('完毕');
