# -*- coding: utf-8 -*-
## 调用要使用的包
import json
import random
import requests
import time
import pandas as pd
import os
from pyecharts import Bar,Geo,Line,Overlap
import jieba
import openpyxl
from scipy.misc import imread  # 这是一个处理图像的函数
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from collections import Counter
import pymysql
from functools import reduce
# import until.config as config
from until.config import sql_config


conn = pymysql.connect(**sql_config)
conn.autocommit(1)
cursor = conn.cursor()

def _remove_duplicate(dict_list):
    l4=[]
    l4.append(dict_list[0])
    for dict in dict_list:
        #print len(l4)
        k=0
        for item in l4:
            #print 'item'
            if dict[0] != item[0]:
                k=k+1
                #continue
            else:
                break
            if k == len(l4):
                l4.append(dict)
    return l4

try:
    # 创建数据库
    DB_NAME = 'tujia_data'
    cursor.execute('DROP DATABASE IF EXISTS %s' %DB_NAME)
    cursor.execute('CREATE DATABASE IF NOT EXISTS %s' %DB_NAME)
    conn.select_db(DB_NAME)
    
    #创建表
    TABLE_NAME = 'house'
    cursor.execute('CREATE TABLE %s(unitId varchar(45), cityId varchar(100), cityName varchar(45), unitName varchar(100), districtName varchar(45), houseType varchar(45), roomCountShortSummary varchar(45), area varchar(45), unitSummary varchar(100) )' %TABLE_NAME)
    
    # 批量插入纪录
    ## 设置headers和cookie
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
    'Connection': 'keep-alive', 'Accept': 'application/json, text/plain, */*', 'Content-Type': 'application/json'}
    cookies ='tujia.com_PortalContext_LongerRefUrl=https://m.tujia.com/; gr_user_id=33d128da-ce51-415c-9f34-1fab35da6727; tujia.com_PortalContext_GuestToken=b7787f83-c39f-463f-874d-baf1c322addc; tujia.com_PortalContext_GuestId=-823707296; tujia.com_MobileContext_ShowDownAppBar=False; tujia_out_site_referrerUrl=http%3A%2F%2Flocalhost%3A8080%2F; __utmc=196523689; tujia_out_site_landingUrl=https%3A%2F%2Fpassport1.fvt.tujia.com%2FH5Site%2FLoginPage%2F%3Fsrcurl%3Dhttp%253a%252f%252fm1.fvt.tujia.com%252fnosearch%252fm_menu; Hm_lvt_405c96e7f6bed44fb846abfe1f65c6f5=1535958994,1536569930,1536570220,1536577671; __utma=196523689.1142939252.1536570221.1536570221.1536577673.2; __utmz=196523689.1536577673.2.2.utmcsr=localhost:8080|utmccn=(referral)|utmcmd=referral|utmcct=/; gr_session_id_1fa38dc3b3e047ffa08b14193945e261=9720e875-85d1-45c2-85ff-ca6f4f18ab87; gr_session_id_1fa38dc3b3e047ffa08b14193945e261_9720e875-85d1-45c2-85ff-ca6f4f18ab87=true; tujia.com_PortalContext_UserId=0; tujia.com_PortalContext_RefUrl=https://m.tujia.com/; tujia.com_PortalContext_LandingUrl=http://www.tujia.com/api/pccity/CurrentCity/; tujia.com_PortalContext_GuestCount=0; tujia.com_PortalContext_BedCount=0; tujia.com_PortalContext_RoomCount=0; dialogActivityFlag=True; gr_cs1_9720e875-85d1-45c2-85ff-ca6f4f18ab87=user_id%3A0; tujia.com_PortalContext_Platform=PC; Qs_lvt_80931=1536828992; tujia.com_PortalContext_StartDate=2018-9-13; tujia.com_PortalContext_EndDate=2018-9-14; activitypopup=1; qimo_seosource_797098a0-b29d-11e5-b3b1-49764155fe50=%E5%85%B6%E4%BB%96%E7%BD%91%E7%AB%99; qimo_seokeywords_797098a0-b29d-11e5-b3b1-49764155fe50=%E6%9C%AA%E7%9F%A5; accessId=797098a0-b29d-11e5-b3b1-49764155fe50; bad_id797098a0-b29d-11e5-b3b1-49764155fe50=eeb7f081-b732-11e8-b72a-5da442cf4db0; nice_id797098a0-b29d-11e5-b3b1-49764155fe50=eeb7f082-b732-11e8-b72a-5da442cf4db0; manualclose=1; Qs_pv_80931=999952457880496400%2C2317986173465245700; tujia.com_PortalContext_DestinationId=48; Hm_lpvt_405c96e7f6bed44fb846abfe1f65c6f5=1536829030; pageViewNum=2'
    cookie = {}
    houses = []
    for line in cookies.split(';'):
        name, value = line.strip().split('=', 1)
        cookie[name] = value

    url= 'https://www.tujia.com/bingo/pc/search/searchUnit'
    data_={"conditions":[{"label":"北京","specialLabel":'null',"type":42,"value":"48","gType":0,"percentageUser":'null',"pingYin":'null',"hot":'null',"labelDesc":'null',"isSelected":False,"selected":False,"hotRecommend":'null'},{"label":"推荐排序","specialLabel":'null',"type":48,"value":"1","gType":4,"percentageUser":'null',"pingYin":'null',"hot":'null',"labelDesc":'null',"isSelected":False,"selected":False,"hotRecommend":'null'},{"label":"","specialLabel":'null',"type":47,"value":"2018-09-13,2018-09-14","gType":0,"percentageUser":'null',"pingYin":'null',"hot":'null',"labelDesc":'null',"isSelected":False,"selected":False,"hotRecommend":'null'}],"pageIndex":1,"pageSize":1,"returnAllConditions":False,"returnRedPacketInfo":True,"returnUnitTagBadgeInfo":False,"callCenter":False}
    html = requests.post(url, cookies=cookie, headers=header, data=json.dumps(data_)).content
    totalUnitCount = json.loads(html.decode('utf-8'))['data']['totalUnitCount']

    for i in range(0,10):
        print('第'+str(i+1)+'页,第'+str((i+1) * 50)+'项')
        # try:
        time.sleep(2) 
        data_={"conditions":[{"label":"北京","specialLabel":'null',"type":42,"value":"48","gType":0,"percentageUser":'null',"pingYin":'null',"hot":'null',"labelDesc":'null',"isSelected":False,"selected":False,"hotRecommend":'null'},{"label":"推荐排序","specialLabel":'null',"type":48,"value":"1","gType":4,"percentageUser":'null',"pingYin":'null',"hot":'null',"labelDesc":'null',"isSelected":False,"selected":False,"hotRecommend":'null'},{"label":"","specialLabel":'null',"type":47,"value":"2018-09-13,2018-09-14","gType":0,"percentageUser":'null',"pingYin":'null',"hot":'null',"labelDesc":'null',"isSelected":False,"selected":False,"hotRecommend":'null'}],"pageIndex":i,"pageSize":50,"returnAllConditions":False,"returnRedPacketInfo":True,"returnUnitTagBadgeInfo":False,"callCenter":False}
        html = requests.post(url, cookies=cookie, headers=header, data=json.dumps(data_)).content
        res = json.loads(html.decode('utf-8'))['data']['units']
        
        for item in res:
            houses.append((item['unitId'],item['cityId'],item['cityName'],item['unitName'],item['districtName'],item['houseType'],
                                    item['roomCountShortSummary'],item['area'],item['unitSummary']))
    houses = _remove_duplicate(houses)
    cursor.executemany('INSERT INTO house values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',houses)
    
    # 查询数据条目
    count = cursor.execute('SELECT * FROM %s' %TABLE_NAME)
    print('total records:' + str(cursor.rowcount))
    
    # 获取表名信息
    # desc = cursor.description
    # print("%s %3s" % (desc[0][0], desc[1][0]))

    # cursor.scroll(10,mode='absolute')
    # results = cursor.fetchall()
    # for result in results:
    #     print(result)
        
except:
    import traceback
    traceback.print_exc()
    # 发生错误时会滚
    conn.rollback()
finally:
    # 关闭游标连接
    cursor.close()
    # 关闭数据库连接
    conn.close()