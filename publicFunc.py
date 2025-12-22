'''
通用公用函数
'''

import math
from operator import itemgetter
import re
import sqlite3
import pandas as pd
import numpy as np
from collections import OrderedDict
from difflib import get_close_matches


def clearDataBaseTable(table_name):
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {table_name};")
    conn.commit()
    conn.close()

def get_list(str,lists):
    for i in range(0,len(str)-1):
        lists.append(str[i:i+2])

# 从objs列表模糊匹配sourse最相似的字符串
def mostLike(sourse,objs):
    same = 0
    mark = ""
    for obj in objs:
        sourse_lists = []
        len_min = min(len(sourse),len(obj))
        if same < len_min:
            get_list(sourse,sourse_lists)
            tempsame=0
            for sourse_list in sourse_lists:
                if sourse_list in obj:
                    tempsame = tempsame + 1
            if tempsame > same:
                same = tempsame
                mark = obj
    return mark

def fuzzy_match(source, objs):
    """
    从objs列表中找到与source最相似的字符串
    :param source: 要匹配的源字符串
    :param objs: 候选字符串列表
    :return: 匹配度最高的字符串
    """
    if not objs:
        return None
    # 获取最相似的1个结果
    matches = get_close_matches(source, objs, n=1, cutoff=0.6)
    return matches[0] if matches else objs[0]

@np.vectorize
def fixSite(x,y):
    if pd.isnull(x):
        return y
    else:
        return x
    
@np.vectorize
def CompareMin(x,y):
	if x < y:
		return x
	else:
		return y

@np.vectorize
def isDiffer(x,y):
    if x==y:
        return '否'
    else:
        return '是'


def readDataBase(sql):
    conn = sqlite3.connect('data/database.db')
    df = pd.read_sql_query(sql, conn)
    conn.close()
    return df
