# -*- coding: UTF-8 -*-
import csv
import json

x="""[
{
        "visits_count":109156000,
        "name":"收集 | 经典文学名句",
        "banner":"https://picb.zhimg.com/50/v2-a08bf4aab090bf138199e25a0207c2ed_720w.jpg?source=b1f6dc53",
        "logo":"https://pic2.zhimg.com/50/v2-00f8805ec1d10c26f09a8f6a878c77ed_720w.jpg?source=b1f6dc53",
        "tiny_banner":"https://pic3.zhimg.com/50/v2-c63880a848ac00031797de705593d62b_720w.jpg?source=b1f6dc53",
        "url_token":"shoujijingdianwen",
        "include_count":27
    },{
        "visits_count":221015823,
        "name":"成为「姐姐」的美一步",
        "banner":"https://pic1.zhimg.com/50/v2-707c6b3226a453168081150d663adbb8_720w.jpg?source=b1f6dc53",
        "logo":"https://pic2.zhimg.com/50/v2-d1daec2b01c92a9112f077ad77c4f113_720w.jpg?source=b1f6dc53",
        "tiny_banner":"https://pic3.zhimg.com/50/v2-c2659aab39fd12637a95c55c63921ab1_720w.jpg?source=b1f6dc53",
        "url_token":"beauty30",
        "include_count":21
    }]"""


json_file = open("data.json","r")
data = json.loads(json_file.read())


writer = csv.writer(open("data.csv","wb+"))
writer.writerow(["圆桌名","浏览次数","链接"])

for row in data['data']:
    writer.writerow([
        row['name'].encode('utf-8', errors='ignore'),
    row['visits_count'],
    "www.zhihu.com/roundtable/"+row['url_token']
    ])

