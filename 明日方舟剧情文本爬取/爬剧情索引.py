# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 10:21:34 2021

@author: 24587
"""

import requests
import re
url="http://prts.wiki/w/剧情一览"
headers={"user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36 Edg/92.0.902.78"}
res=requests.get(url,headers)
with open("index.html","w",encoding="utf-8") as f:
    f.write(res.content.decode())