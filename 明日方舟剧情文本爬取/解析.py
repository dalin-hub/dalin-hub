# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 23:14:13 2021

@author: 24587
"""

import re
out=open("文本解析.txt","w",encoding="utf-8")
fin=open("明日方舟剧情.html","r",encoding="utf-8")
s=fin.read()
res=re.findall(r"\s*\[\s*name\s*=.*\].*\n",s)
for i in res:
    i=re.sub('\s*\[\s*name\s*=\s*"\s*',"",i)
    i=re.sub('\s*"\s*\]\s*',":",i)
    out.write(i)
out.close()
fin.close()