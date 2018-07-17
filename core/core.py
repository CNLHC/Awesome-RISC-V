#!/usr/bin/python3
import requests
import json


def generateAdocTable(projects:list) -> str:
    out =\
""".Risc-V 开源核心
[cols=5,options="header"]
|===
|项目名称
|开源协议
|项目地址
|HDL
|star
    """
    for project in  projects:
        if project['github']:
            star=\
"""+++
<a class="github-button" href="%s" data-icon="octicon-star" data-show-count="true" aria-label="Star ntkme/github-buttons on GitHub">Star</a>
+++
"""%project["url"]
        else:
            star = "UNKNOWN"

        out+="""
|%s
|%s
|%s
|%s
|%s
"""%(project['name'], project['license'], project['url'],project['HDL'],star)
    out =out[0:-1]
    out +=\
"""
|==="""
    out +=\
"""
+++
<script async defer src="https://buttons.github.io/buttons.js"></script>
+++
"""
    return out




jsObj= json.load(open("./raw.json"))
with open('./coreTable.adoc','w') as fp:
    fp.write(generateAdocTable(jsObj))

