# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 10:34:20 2021

@author: 24587
"""

import re
class sect(object):
    def __init__(self):
        self.text=None
        self.name=None
        self.herf=[]
        self.title=[]

f=open("index.html",encoding="utf-8")
s=f.read()
section=re.findall("<th.*>.*\n.*\n.*\n.*\n.*\n",s)
section_list=[]
for i in section:
    sec=sect()
    sec.text=i
    section_name=re.search("<th.*>.*\n",i).group()
    section_name=re.sub("<th.*>","",section_name)
    sec.name=re.sub(r"\n","",section_name)
    section_list.append(sec)
for i in section_list:
    i.herf=re.findall('title\s*=\s*".*?"',i.text)
    i.title=re.findall(">[^>]*?</a>",i.text)
count=[]
a=0
for i in section_list:
    if len(i.herf)!=len(i.title):
        print(a)
        count.append(i.name)
    a+=1