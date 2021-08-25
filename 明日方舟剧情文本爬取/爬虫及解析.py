# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 23:13:06 2021

@author: 24587
此脚本针对prts.wiki进行了明日方舟游戏剧情的爬取，使用的方法是用正则来匹配网页中的对话内容，需要借助经过预处理产生的section_list列表，
section_list：
    type:list
    elements:sect object
sect object:每一个sect代表一章的索引
    sect.text:从网页中的章节列表中爬到的内容
    sect.name:章名
    sect.title:章内的节名
    sect.herf:节名对应的url参数
"""

import requests
import urllib
import re
import time
from index_interpret import section_list
url1="http://prts.wiki/index.php?"
headers={"user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36 Edg/92.0.902.78"}
for i in section_list:
    out=open(i.name+".txt","w",encoding="utf-8")
    for j in range(len(i.herf)):
        s=re.search('".*"',i.herf[j]).group()
        s=re.sub('"',"",s)
        url=url1+"title="+s+"&action=edit"
        res=requests.get(url,headers=headers)
        text=res.content.decode()
        title=re.sub(">","",i.title[j])
        title=re.sub("</a","",title)
        out.write("\n"*2+title+"\n"*2)
        dialog=re.findall(r"\s*\[\s*name\s*=.*\].*\n",text)
        for k in dialog:
            k=re.sub('\s*\[\s*name\s*=\s*"\s*',"",k)
            k=re.sub('\s*"\s*\]\s*',":",k)
            out.write(k)
    out.close()
    time.sleep(1)
    
