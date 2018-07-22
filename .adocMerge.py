#该脚本用于通过include语句，将多个adoc文件合并成一个

import re 

include_pattern=re.compile("(^include\:\:(.*?)\[\].*$)",re.M) #查找结果为嵌套列表[(express,path),]

RawIndex = open('./index.adoc','r').read()

entryList  = re.findall(include_pattern,RawIndex)

for exp,path  in entryList:
    print("find include:",path)
    with open(path,'r') as fp:
        RawIndex= re.sub(re.escape(exp),fp.read(),RawIndex)

with open('./README.adoc','w') as out:
    out.write(RawIndex)
    

