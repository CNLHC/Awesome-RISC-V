import json


def generateAdoc(items:list):
    out = ''
    for item in items:
        hint = "地址" if item['downloadable'] else  "下载地址"
        out+=\
"""
%s %s[%s]
"""%(item['title'],item['url'],hint)
    return out




jsObj= json.load(open("./raw.json"))
with open('./paper.adoc','w') as fp:
    fp.write(generateAdoc(jsObj))




