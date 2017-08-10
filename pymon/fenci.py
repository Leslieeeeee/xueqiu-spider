import sys
import jieba
import json
import pymongo
import jieba.analyse
from pymongo import MongoClient
from optparse import OptionParser


#连接数据库
client = MongoClient()
db = client.Spider
col1 = db.xqcom
i = 350878
#读取数据
while i < 350888:
    msg = col1.find({'name':1}).limit(1).skip(i)
    text = json.dump(msg)
    com = text["command"]
    i = i + 1
    #分词
    seg_list = jieba.cut(com)  # 默认是精确模式
    print(", ".join(seg_list))

    #关键词提取

    """
    if topK is None:
        topK = 20
    else:
        topK = int(topK)
    tags = jieba.analyse.extract_tags(com, topK=topK)
    print(",".join(tags))
    """